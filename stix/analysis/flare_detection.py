#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Flare detection algorithm
    Procedure:
    1) smoothing the lowest energy bin lightcurve using a butterworth low-pass filter
    2) searching for local maxima in the smoothed lightcurve

"""

import os
import sys
sys.path.append('.')
from scipy import signal
import numpy as np
import math
import matplotlib
from matplotlib import pyplot as plt
from stix.core import stix_datatypes as sdt
from stix.core import mongo_db as db
from stix.core import stix_datetime
from stix.core import stix_logger
logger = stix_logger.get_logger()
matplotlib.use('Agg')

mdb = db.MongoDB()

SPID = 54118

terminal = False


def info(msg):
    if terminal:
        print(msg)
        return
    logger.info(msg)


def smooth(y, N=15):

    y_padded = np.pad(y, (N//2, N-1-N//2), mode='edge')
    y_smooth = np.convolve(y_padded, np.ones((N,))/N, mode='valid') 
    return y_smooth


def get_lightcurve_data(file_id, rebin=30):
    packets = mdb.select_packets_by_run(file_id, SPID)
    if not packets:
        info(f'No QL LC packets found for run {file_id}')
        return None
    lightcurves = {}
    unix_time = []
    for pkt in packets:
        packet = sdt.Packet(pkt)
        if not packet.isa(SPID):
            continue
        #fig = None

        scet_coarse = packet[1].raw
        scet_fine = packet[2].raw
        start_scet = scet_coarse + scet_fine / 65536.

        int_duration = (packet[3].raw + 1) * 0.1

        detector_mask = packet[4].raw
        pixel_mask = packet[6].raw

        num_lc = packet[17].raw

        compression_s = packet[8].raw
        compression_k = packet[9].raw
        compression_m = packet[10].raw

        num_lc_points = packet.get('NIX00270/NIX00271')[0]
        lc = packet.get('NIX00270/NIX00271/*.eng')[0]
        rcr = packet.get('NIX00275/*.raw')
        UTC = packet['header']['UTC']
        for i in range(len(lc)):
            if i not in lightcurves:
                lightcurves[i] = []
            lightcurves[i].extend(lc[i])
        unix_time.extend([
            stix_datetime.scet2unix(start_scet + x * int_duration)
            for x in range(num_lc_points[0])
        ])

    if not lightcurves:
        return None
    time=np.array(unix_time)
    lc=np.array(lightcurves[0])

    return {'time': np.array(unix_time), 'lc': np.array(lightcurves[0])}


def make_lightcurve_snapshot(data, docs, snapshot_path):
    '''
                '_id': first_id + i,
                'run_id': result['run_id'],
                'hidden': hidden,
                'peak_counts': result['peak_counts'][i],
                'peak_utc': result['peak_utc'][i],
                'peak_unix_time': result['peak_unix_time'][i],
    '''
    #print(flare_list)
    inserted_ids = docs['inserted_ids']
    #print(inserted_ids)

    for i, inserted_id in enumerate(inserted_ids):
        if inserted_id == None:
            continue
        _id = inserted_id
        #print('_id', inserted_id)
        min_height = docs['conditions']['min_height']

        start_unix = docs['start_unix'][i]
        end_unix = docs['end_unix'][i]
        flare_id=docs['flare_id'][i]
        margin = 300
        where = np.where((data['time'] > start_unix - margin)
                         & (data['time'] < end_unix + margin))
        unix_ts = data['time'][where]
        t_since_t0 = unix_ts - docs['peak_unix_time'][i]
        lc = data['lc'][where]
        peak_counts = docs['peak_counts'][i]
        

        fig = plt.figure(figsize=(6, 2))
        plt.plot(t_since_t0, lc, label="4-10 keV LC")
        plt.plot(t_since_t0,data['lc_smoothed'][where], label='1-min moving mean')
        T0 = stix_datetime.unix2utc(docs['peak_unix_time'][i])
        xmin = docs['start_unix'][i] - docs['peak_unix_time'][i]
        xmax = docs['end_unix'][i] - docs['peak_unix_time'][i]

        plt.plot([0],
                   [peak_counts],
                   marker='+',color='cyan', markersize=15)

        ylow = peak_counts - 1.1 * docs['properties']['prominences'][i]

        plt.vlines(xmin, ylow, peak_counts, linestyle='dashed', color='C3' )
        plt.vlines(xmax, ylow, peak_counts, linestyle='dashed', color='C3' )
        plt.text(xmin, 0.9*peak_counts, 'Start', color='C3')
        plt.text(0.8*xmax, 0.9*peak_counts, 'End', color='C3')
        baseline=docs['baseline']

        plt.hlines(docs['properties']['width_heights'][i],
                   xmin=xmin,
                   xmax=xmax,
                   linewidth=2,
                   color='C2')

        #plt.hlines(min_height,
        #           t_since_t0[0],
        #           t_since_t0[-1],
        #           linestyle='dotted',
        #           color='red',
        #           label="threshold")
        #plt.hlines(baseline,
        #           t_since_t0[0],
        #           t_since_t0[-1],
        #           linestyle='dotted',
        #           color='blue',
        #           label="baseline")



        plt.xlabel(f'T - T0 (s),  T0: {T0}')
        plt.ylabel('Counts / 4 s')
        plt.title(f'Flare #{flare_id}')
        filename = os.path.join(snapshot_path, f'flare_lc_{_id}_{flare_id}.png')
        fig.tight_layout()
        #print(filename)
        plt.savefig(filename, dpi=100)
        mdb.set_tbc_flare_lc_filename(_id, filename)
        plt.close()
        plt.clf()


def major_peaks(lefts, rights):
    #remove small peaks
    num = lefts.size
    major = [True] * num
    for i in range(num):
        a = (lefts[i], rights[i])
        for j in range(num):
            if i == j:
                continue
            b = (lefts[j], rights[j])

            if a[0] >= b[0] and a[1] <= b[1]:  #a in b
                major[i] = False
    return major


def search(run_id,
           peak_min_width=15,
           peak_min_distance=150,
           rel_height=0.9,
           snapshot_path='.'):

    data = get_lightcurve_data(run_id)

    print(f'deleting file {run_id}')

    mdb.delete_flare_candidates_for_file(run_id)

    if not data:
        info(f'No QL LC packets found for file {run_id}')
        return 0

    unix_time = data['time']
    lightcurve = data['lc']
    med = np.median(lightcurve)
    prominence = 2 * np.sqrt(med)
    noise_rms=np.sqrt(med)
    baseline=med

    height = med + 3 * np.sqrt(med)
    stat = mdb.get_nearest_qllc_statistics(unix_time[0], 500)
    if stat:
        if stat['std'][0] < 2 * math.sqrt(
                stat['median'][0]):  #valid background
            height = stat['median'][0] + 2 * stat['std'][0]
            baseline=stat['median'][0]
            prominence = 2 * stat['std'][0]
            noise_rms=  stat['std'][0]

    lc_smoothed=smooth(lightcurve)
    result = {}
    xpeaks, properties = signal.find_peaks(
        lc_smoothed,
        height=height,
        prominence=prominence,
        width=peak_min_width,
        rel_height=rel_height,  #T90 calculation
        distance=peak_min_distance)
    if xpeaks.size == 0:
        info(f'No peaks found for file {run_id}')
        return 0
    info('Number of peaks:{}'.format(xpeaks.size))
    conditions = {
        'peak_min_width': peak_min_width,
        'peak_min_distance': peak_min_distance,
        'rel_height': rel_height,
        'prominence': prominence,
        'bkg_statistics': stat,
        'min_height': height,
    }
    doc = {}
    peak_values = properties['peak_heights']
    peak_unix_times = unix_time[xpeaks]
    peaks_utc = [stix_datetime.unix2utc(x) for x in peak_unix_times]
    flare_ids=[stix_datetime.unix2datetime(x).strftime("%y%m%d%H%M")
            for x in peak_unix_times]

    majors = major_peaks(properties['left_ips'], properties['right_ips'])
    range_indexs = [(int(properties['left_ips'][i]),
                     int(properties['right_ips'][i]))
                    for i in range(xpeaks.size)]
    total_counts = [
        int(np.sum(lightcurve[r[0]:r[1]])) for r in range_indexs
    ]
    seconds_per_bin=4
    durations=np.array([(r[1]-r[0])*seconds_per_bin for r in range_indexs])
    cps=total_counts/durations

    total_signal_counts = []
    for i, (cnts, dur) in enumerate(zip(total_counts, durations)) :
        sig_cnts=cnts -dur*baseline/seconds_per_bin
        if sig_cnts<0:
            sig_cnts=cnts-dur*properties['width_heights'][i]/seconds_per_bin
        total_signal_counts.append(sig_cnts)
    
    doc = {
        'num_peaks': xpeaks.size,
        'peak_unix_time': peak_unix_times.tolist(),
        'peak_counts': peak_values.tolist(),
        'peak_utc': peaks_utc,
        'flare_id':flare_ids,
        'baseline':baseline,
        'noise_rms':noise_rms,
        'total_counts': total_counts,
        'total_signal_counts':total_signal_counts,
        'duration':durations.tolist(),
        'mean_cps':cps.tolist(),
        'conditions': conditions,
        'peak_width_bins': properties['widths'].tolist(),  #width of height
        'width_height':properties['width_heights'].tolist(),  # height of the width, background level
        'peak_prominence': properties['prominences'].tolist(),
        'start_unix': unix_time[properties['left_ips'].astype(int)].tolist(),
        'end_unix': unix_time[properties['right_ips'].astype(int)].tolist(),
        'is_major': majors,
        'run_id': run_id
    }

    mdb.save_flare_candidate_info(doc)
    doc['properties'] = properties
    data['lc_smoothed']=lc_smoothed
    make_lightcurve_snapshot(data, doc, snapshot_path)
    return xpeaks.size


def search_in_many(fid_start, fid_end, img_path='/data/flare_lc'):
    for i in range(fid_start, fid_end + 1):
        print(f'deleting files {i}')
        mdb.delete_flare_candidates_for_file(i)
    for i in range(fid_start, fid_end + 1):
        search(i, snapshot_path=img_path)


if __name__ == '__main__':
    import sys
    terminal = True
    if len(sys.argv) < 2:
        print('flare_detection file_number')
    elif len(sys.argv) == 2:
        res=search(int(sys.argv[1]), snapshot_path='/data/flare_lc')
        print('Number of peaks:', res)
    else:
        search_in_many(int(sys.argv[1]),
                       int(sys.argv[2]),
                       img_path='/data/flare_lc')
