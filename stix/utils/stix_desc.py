#!/usr/bin/python
#parameter  and SPID descriptions
#not used by the parser

PCF_DESC = {
    'NIX00001': 'TC Packet ID',
    'NIX00002': 'TC Packet Seq Control',
    'NIX00003': 'FID',
    'NIX00004': 'TC packet type',
    'NIX00005': 'TC packet subtype',
    'NIX00006': 'Received checksum',
    'NIX00007': 'Computed checksum',
    'NIX00008': 'Position incons. param.',
    'NIX00009': 'Value incons. param.',
    'NIX00010': 'Packet sequence flags',
    'NIX00011': 'Packet sequence count',
    'NIX00012': 'Current operation mode',
    'NIX00013': 'Target mode',
    'NIX00014': 'MID',
    'NIX00015': 'Start address',
    'NIX00016': 'Length - number bytes',
    'NIX00017': 'Received segment mask',
    'NIX00018': 'Expected segment mask',
    'NIX00019': 'FDIR function mask',
    'NIX00020': 'SID',
    'NIX00021': 'FDIR parameter',
    'NIX00022': 'FDIR parameter ID',
    'NIX00023': 'FDIR parameter value',
    'NIX00024': 'Memory operation',
    'NIX00025': 'Service Type',
    'NIX00026': 'Service Subtype',
    'NIX00027': 'Received length',
    'NIX00028': 'Expected packet length',
    'NIX00029': 'Version number',
    'NIX00030': 'Packet type',
    'NIX00031': 'Data field header flag',
    'NIX00032': 'CCSDS 2nd header flag',
    'NIX00033': 'PUS version',
    'NIX00034': 'FLASH operation',
    'NIX00035': 'LUT ID',
    'NIX00037': 'Unique data request numb',
    'NIX00038': 'Start Time - sub-seconds',
    'NIX00039': 'Tmin (rel) [1/10 sec]',
    'NIX00040': 'Tmax (rel) [1/10 sec]',
    'NIX00041': 'Tdiv unit [1/10 sec]',
    'NIX00042': 'Selftest ID',
    'NIX00043': 'Last executed state',
    'NIX00044': 'Selected MID - LoadASW',
    'NIX00045': 'Image MID - LoadASW',
    'NIX00046': 'Image pages - LoadASW',
    'NIX00047': 'Image CRC - LoadASW',
    'NIX00048': 'CRC buff FLASH - LoadASW',
    'NIX00049': 'Num of pages - ExecASW',
    'NIX00050': 'Stored CRC - ExecASW',
    'NIX00051': 'Calc CRC - ExecASW',
    'NIX00052': 'Sel MID - save ASW image',
    'NIX00053': 'Sel pages - save ASW ima',
    'NIX00054': 'TC ID oldest unprocess',
    'NIX00055': 'TC SSC oldest unprocess',
    'NIX00056': 'Received Ack flags (4b)',
    'NIX00057': 'StartASW state',
    'NIX00058': 'Invalid SID',
    'NIX00059': 'Heartbeat value',
    'NIX00060': 'Flare Message',
    'NIX00061': 'X Location',
    'NIX00062': 'Y Location',
    'NIX00063': 'Flare Duration',
    'NIX00064': 'Received FDIR mask',
    'NIX00065': 'Counts',
    'NIX00066': 'Requested page address',
    'NIX00067': 'Address after operation',
    'NIX00068': 'Allowed mask of FDIR',
    'NIX00069': 'System ID',
    'NIX00070': 'Operation ID',
    'NIX00071': 'Running test footprints',
    'NIX00072': 'Med value of trig acc',
    'NIX00073': 'Max value of trig acc',
    'NIX00074': 'Selected test footprints',
    'NIX00075': 'Start address in MID',
    'NIX00076': 'Attenuator motions',
    'NIX00077': 'End address in MID',
    'NIX00078': 'HK_ASP_PHOTOA0_V',
    'NIX00079': 'HK_ASP_PHOTOA1_V',
    'NIX00080': 'HK_ASP_PHOTOB0_V',
    'NIX00081': 'HK_ASP_PHOTOB1_V',
    'NIX00082': 'Length SAU',
    'NIX00083': 'MUL = 1',
    'NIX00084': 'MUL = 4',
    'NIX00085': 'FDIR function status',
    'NIX00086': 'Page with failed CRC chk',
    'NIX00087': 'Data processing level',
    'NIX00088': 'Summing value',
    'NIX00089': 'Number of samples',
    'NIX00090': 'ChA diode 0 voltage',
    'NIX00091': 'ChA diode 1 voltage',
    'NIX00092': 'ChB diode 0 voltage',
    'NIX00093': 'ChB diode 1 voltage',
    'NIX00094': 'Attenuator currents',
    'NIX00096': 'Limit value',
    'NIX00097': 'ID of HK line',
    'NIX00098': 'Actual value',
    'NIX00099': 'MID that was checked',
    'NIX00100': 'Detector number',
    'NIX00101': 'Mean - ASIC temperature',
    'NIX00102': 'Std dev ASIC temperature',
    'NIX00103': 'Number of structures',
    'NIX00104': 'Number of structures NxP',
    'NIX00105': 'Channel number',
    'NIX00106': 'Mean - ASIC ch',
    'NIX00107': 'Std dev - ASIC ADC ch',
    'NIX00108': 'Detected threshold',
    'NIX00109': 'Mean - ADC group',
    'NIX00110': 'Std dev - ADC group',
    'NIX00111': 'Error reason',
    'NIX00112': 'Selected MID',
    'NIX00113': 'MID - ASWimgHdr',
    'NIX00114': 'NumOfPages - ASWimgHdr',
    'NIX00115': 'CRC - ASWimgHdr',
    'NIX00116': 'Calculated CRC',
    'NIX00117': 'Size of ASW img to store',
    'NIX00119': 'Pixel ID',
    'NIX00120': 'SSID',
    'NIX00121': 'Start Time - seconds',
    'NIX00122': 'Duration',
    'NIX00123': 'Quiet Time',
    'NIX00124': 'Live Time',
    'NIX00125': 'Average temperature',
    'NIX00126': 'Movement type',
    'NIX00127': 'Initial flags',
    'NIX00128': 'End flags',
    'NIX00129': 'Main context file flag',
    'NIX00130': 'Backup context file flag',
    'NIX00131': 'Processor State Register',
    'NIX00132': 'Trap Base Register',
    'NIX00133': 'Program Counter',
    'NIX00134': 'Next Program Counter',
    'NIX00142': 'Received error code',
    'NIX00143': 'Received byte count',
    'NIX00144': 'CCSDS header',
    'NIX00145': 'Operation duration',
    'NIX00146': 'Sp - nr of compr sp pts',
    'NIX00147': 'SuSW Parameter ID',
    'NIX00148': 'SuSW Parameter subID',
    'NIX00149': 'SuSW Parameter data',
    'NIX00150': 'ASW Parameter ID',
    'NIX00151': 'ASW Parameter subID',
    'NIX00152': 'ASW Parameter data',
    'NIX00158': 'Compr spectral point',
    'NIX00159': 'Number of structures M',
    'NIX00160': 'SbSpect Mask',
    'NIX00161': 'FDIR stat msk HK temp ch',
    'NIX00162': 'FDIR stat msk HK volt ch',
    'NIX00166': 'Number of executed TC pa',
    'NIX00167': 'Number of sent TM packet',
    'NIX00168': 'Number of failed TM gene',
    'NIX00173': 'Mask of error chips',
    'NIX00175': 'ID of EDAC module',
    'NIX00176': 'New scrubbing rate',
    'NIX00177': 'Old scrubbing rate',
    'NIX00178': 'Counts leading to change',
    'NIX00179': 'Threshold exceeded',
    'NIX00180': 'Period of SEU checking',
    'NIX00181': 'HV line',
    'NIX00182': 'Original state',
    'NIX00183': 'New state',
    'NIX00184': 'Initialisation status',
    'NIX00185': 'Total number of files',
    'NIX00186': 'Number of bad blocks',
    'NIX00187': 'Number of error blocks',
    'NIX00188': 'Number of free blocks',
    'NIX00189': 'ATT movement',
    'NIX00190': 'SDRAM addr - part test',
    'NIX00191': 'SDRAM addr - full test',
    'NIX00192': 'SDRAM addr - patterntest',
    'NIX00193': 'FDIR function triggering',
    'NIX00194': 'Selected start file num',
    'NIX00195': 'Selected end file num',
    'NIX00196': 'Max file number to sel',
    'NIX00197': 'Data structure (from 0)',
    'NIX00199': 'Register mask',
    'NIX00200': 'Allowed min for par ID',
    'NIX00201': 'Allowed max for par ID',
    'NIX00202': "Expected len TC's data",
    'NIX00203': 'Req value to be set',
    'NIX00204': 'Recived len TCs data',
    'NIX00206': 'Selected config value',
    'NIX00207': 'Max subsystem ID avl',
    'NIX00208': 'System ID selected',
    'NIX00209': 'Subsystem ID selected',
    'NIX00210': 'Exceeded config limit',
    'NIX00215': 'Lower accumulator bound',
    'NIX00216': 'NumOfSummedAcc/SpPoint',
    'NIX00217': 'NumOfSpectralPoints',
    'NIX00218': 'Selected test bitmask',
    'NIX00222': 'Start file',
    'NIX00223': 'Flash block offset - s f',
    'NIX00224': 'End file',
    'NIX00225': 'Flash block offset - e f',
    'NIX00226': 'Num of processed files',
    'NIX00227': 'Bad blocks - before rec',
    'NIX00228': 'Bad blocks - after rec',
    'NIX00229': 'Err blocks - before rec',
    'NIX00230': 'Err blocks - after rec',
    'NIX00231': 'Free blocks - before rec',
    'NIX00232': 'Free blocks - after rec',
    'NIX00233': 'Fill blocks - before rec',
    'NIX00234': 'Fill blocks - after rec',
    'NIX00235': 'Position sensor AB',
    'NIX00236': 'Position sensor BC',
    'NIX00237': 'Motor 1 used',
    'NIX00238': 'Motor 2 used',
    'NIX00239': 'Num of QL iter checked',
    'NIX00240': 'Num of yellow flags',
    'NIX00241': 'New active detector mask',
    'NIX00242': 'Compr trigger acc 0',
    'NIX00243': 'Compr trigger acc 1',
    'NIX00244': 'Compr trigger acc 2',
    'NIX00245': 'Compr trigger acc 3',
    'NIX00246': 'Compr trigger acc 4',
    'NIX00247': 'Compr trigger acc 5',
    'NIX00248': 'Compr trigger acc 6',
    'NIX00249': 'Compr trigger acc 7',
    'NIX00250': 'Compr trigger acc 8',
    'NIX00251': 'Compr trigger acc 9',
    'NIX00252': 'Compr trigger acc 10',
    'NIX00253': 'Compr trigger acc 11',
    'NIX00254': 'Compr trigger acc 12',
    'NIX00255': 'Compr trigger acc 13',
    'NIX00256': 'Compr trigger acc 14',
    'NIX00257': 'Compr trigger acc 15',
    'NIX00258': 'Number of energy groups',
    'NIX00259': 'Number of data elements',
    'NIX00260': 'Compressed pixels counts',
    'NIX00261': 'Flux',
    'NIX00262': 'Number of detectors',
    'NIX00263': 'Real visibility com',
    'NIX00264': 'Imaginary visibility com',
    'NIX00265': 'Base pixel mask (RCR0)',
    'NIX00266': 'Enrg bin edge mask - low',
    'NIX00267': 'Compr combined trig acc',
    'NIX00268': 'Compr summed counts',
    'NIX00269': 'Closing time offset',
    'NIX00270': 'Number of energies',
    'NIX00271': 'Num of data pnts LC',
    'NIX00272': 'Compressed Lightcurves',
    'NIX00273': 'Num of data pnts TRIG',
    'NIX00274': 'Compressed Triggers',
    'NIX00275': 'Num of data pnts RCR',
    'NIX00276': 'RCR',
    'NIX00277': 'Num of data pnts BCKG',
    'NIX00278': 'Compressed Background',
    'NIX00279': 'Samp per variance val',
    'NIX00280': 'Num of data pnts VAR',
    'NIX00281': 'Compressed Variance',
    'NIX00282': 'Energy Mask',
    'NIX00283': 'Flare Location Z',
    'NIX00284': 'Flare Location Y',
    'NIX00285': 'UBSD counter',
    'NIX00286': 'PALD counter',
    'NIX00287': 'Start time coarse SCET',
    'NIX00288': 'End time coarse SCET',
    'NIX00289': 'Highest flare flag',
    'NIX00290': 'TM byte voilume',
    'NIX00291': 'Average Z location',
    'NIX00292': 'Average Y location',
    'NIX00293': 'Flare TM proc status',
    'NIX00294': 'Number of listed flares',
    'NIX00297': 'Config parameter value',
    'NIX00298': 'Config Parameter ID',
    'NIX00299': 'EID',
    'NIX00300': 'Test Footprints',
    'NIX00301': 'Success/failure flags',
    'NIX00303': 'Software version',
    'NIX00304': 'Previous mode',
    'NIX00305': 'Actual mode',
    'NIX00306': 'Mode transition reason',
    'NIX00307': 'CPU load',
    'NIX00308': 'HV PSU identification',
    'NIX00309': 'Flare strength',
    'NIX00311': 'Timer IRQ counter',
    'NIX00312': 'SPW IRQ counter',
    'NIX00313': 'ADC Read  IRQ counter',
    'NIX00323': 'CPU load in percentages',
    'NIX00324': 'Limit T1',
    'NIX00325': 'Limit T2',
    'NIX00326': 'Limit N1',
    'NIX00327': 'Limit N2',
    'NIX00328': 'Current N1',
    'NIX00329': 'Current N2',
    'NIX00333': 'Failed temperature senso',
    'NIX00334': 'Failed regulators',
    'NIX00336': 'Requested mode',
    'NIX00337': 'Detector IRQ counter',
    'NIX00338': 'Current time in ms',
    'NIX00339': 'Memory ID',
    'NIX00340': 'ATT move direction',
    'NIX00341': 'ATT motor used',
    'NIX00342': 'ATT position sensor',
    'NIX00344': 'Current working timeout',
    'NIX00345': 'Bitmask of det above lim',
    'NIX00346': 'Det - the highest rate',
    'NIX00347': 'Limit of the high rate',
    'NIX00348': 'Quadrants with OVC',
    'NIX00349': 'Actual current quadr 1',
    'NIX00350': 'Actual current quadr 2',
    'NIX00351': 'Actual current quadr 3',
    'NIX00352': 'Actual current quadr 4',
    'NIX00353': 'Limit of det quadr OVC',
    'NIX00354': 'Quadrant identification',
    'NIX00355': 'Temperature',
    'NIX00357': 'Counter - HV PSU failure',
    'NIX00361': 'Actual rate-det high rat',
    'NIX00362': 'Quart req for operation',
    'NIX00363': 'Powered quarters',
    'NIX00364': 'Grps req for operation',
    'NIX00365': 'Enabled groups',
    'NIX00375': 'Register 4 (SEL_TEST)',
    'NIX00383': 'Register 12 (ALIMON)',
    'NIX00385': 'Group number',
    'NIX00386': 'Failure transfer file',
    'NIX00387': 'Context segment counter',
    'NIX00388': 'LUT type',
    'NIX00389': 'Selected configuration',
    'NIX00390': 'Highest configuration',
    'NIX00391': 'Limit T3',
    'NIX00392': 'Actual quiet (NM) timeT3',
    'NIX00393': 'Actual value',
    'NIX00394': 'Limit value',
    'NIX00399': 'Number of time samples',
    'NIX00401': 'Rate control regime',
    'NIX00402': 'Measurement Time Stamp',
    'NIX00403': 'Number of substructures',
    'NIX00404': 'Starting time',
    'NIX00405': 'Integration duration',
    'NIX00406': 'Number science data samp',
    'NIX00407': 'Detectors mask',
    'NIX00408': 'Trigger accumulator 0',
    'NIX00409': 'Trigger accumulator 1',
    'NIX00410': 'Trigger accumulator 2',
    'NIX00411': 'Trigger accumulator 3',
    'NIX00412': 'Trigger accumulator 4',
    'NIX00413': 'Trigger accumulator 5',
    'NIX00414': 'Trigger accumulator 6',
    'NIX00415': 'Trigger accumulator 7',
    'NIX00416': 'Trigger accumulator 8',
    'NIX00417': 'Trigger accumulator 9',
    'NIX00418': 'Trigger accumulator 10',
    'NIX00419': 'Trigger accumulator 11',
    'NIX00420': 'Trigger accumulator 12',
    'NIX00421': 'Trigger accumulator 13',
    'NIX00422': 'Trigger accumulator 14',
    'NIX00423': 'Trigger accumulator 15',
    'NIX00436': 'Value of HK_DPU_1V5_V',
    'NIX00437': 'Value of HK_REF_2V5_V',
    'NIX00438': 'Value of HK_DPU_2V9_V',
    'NIX00441': 'Delta time in 0.1 sec',
    'NIX00442': 'Number of pixel sets, P',
    'NIX00443': 'Pixel set descr index',
    'NIX00445': 'SCET coarse time',
    'NIX00446': 'SCET fine time',
    'NIX00448': 'Num of PROM recoverable',
    'NIX00449': 'Num of SDRAM recoverable',
    'NIX00450': 'Num of CACHE recoverable',
    'NIX00451': 'Num of ROTBUF recoverabl',
    'NIX00452': 'Compr Spectrum E0',
    'NIX00453': 'Compr Spectrum E1',
    'NIX00454': 'Compr Spectrum E2',
    'NIX00455': 'Compr Spectrum E3',
    'NIX00456': 'Compr Spectrum E4',
    'NIX00457': 'Compr Spectrum E5',
    'NIX00458': 'Compr Spectrum E6',
    'NIX00459': 'Compr Spectrum E7',
    'NIX00460': 'Compr Spectrum E8',
    'NIX00461': 'Compr Spectrum E9',
    'NIX00462': 'Compr Spectrum E10',
    'NIX00463': 'Compr Spectrum E11',
    'NIX00464': 'Compr Spectrum E12',
    'NIX00465': 'Compr Spectrum E13',
    'NIX00466': 'Compr Spectrum E14',
    'NIX00467': 'Compr Spectrum E15',
    'NIX00468': 'Compr Spectrum E16',
    'NIX00469': 'Compr Spectrum E17',
    'NIX00470': 'Compr Spectrum E18',
    'NIX00471': 'Compr Spectrum E19',
    'NIX00472': 'Compr Spectrum E20',
    'NIX00473': 'Compr Spectrum E21',
    'NIX00474': 'Compr Spectrum E22',
    'NIX00475': 'Compr Spectrum E23',
    'NIX00476': 'Compr Spectrum E24',
    'NIX00477': 'Compr Spectrum E25',
    'NIX00478': 'Compr Spectrum E26',
    'NIX00479': 'Compr Spectrum E27',
    'NIX00480': 'Compr Spectrum E28',
    'NIX00481': 'Compr Spectrum E29',
    'NIX00482': 'Compr Spectrum E30',
    'NIX00483': 'Compr Spectrum E31',
    'NIX00484': 'Compr Trigger Accu',
    'NIX00485': 'Num of integr aft 1 samp',
    'NIX00486': 'Flash block (0-65535)',
    'NIX00487': 'Flash page (0-63)',
    'NIX00488': 'BSD box index',
    'NIX00489': 'IRQ Source Index',
    'NIXD0001': 'SW Version Number',
    'NIXD0002': 'CPU load',
    'NIXD0003': 'Archive Memory usage',
    'NIXD0004': 'IDPU identifier',
    'NIXD0005': 'Active SPW link',
    'NIXD0007': 'Compr Sch EACC S',
    'NIXD0008': 'Compr Sch EACC K',
    'NIXD0009': 'Compr Sch EACC M',
    'NIXD0010': 'Compr Sch ETRIG S',
    'NIXD0011': 'Compr Sch ETRIG K',
    'NIXD0012': 'Compr Sch ETRIG M',
    'NIXD0013': 'Emin (low energy bound)',
    'NIXD0014': 'Emax (low energy bound)',
    'NIXD0015': 'Energy division init',
    'NIXD0016': 'E1 (low bound)',
    'NIXD0017': 'E2 (high bound)',
    'NIXD0018': 'Enrg bin edge mask-up SG',
    'NIXD0019': 'Energy Unit - 1',
    'NIXD0021': 'SW running',
    'NIXD0022': 'Instrument number',
    'NIXD0023': 'Instrument mode',
    'NIXD0024': 'HK_PSU_TEMP_T',
    'NIXD0025': 'HK_DPU_PCB_T',
    'NIXD0026': 'HK_DPU_FPGA_T',
    'NIXD0027': 'HK_DPU_3V3_C',
    'NIXD0028': 'HK_DPU_2V5_C',
    'NIXD0029': 'HK_DPU_1V5_C',
    'NIXD0030': 'HK_DPU_SPW_C',
    'NIXD0031': 'HK_DPU_SPW0_V',
    'NIXD0032': 'HK_DPU_SPW1_V',
    'NIXD0035': 'HK_DPU_1V5_V',
    'NIXD0036': 'HK_REF_2V5_V',
    'NIXD0037': 'HK_DPU_2V9_V',
    'NIXD0038': 'HK_ASP_REF_2V5A_V',
    'NIXD0039': 'HK_ASP_REF_2V5B_V',
    'NIXD0040': 'HK_ASP_TIM01_T',
    'NIXD0041': 'HK_ASP_TIM02_T',
    'NIXD0042': 'HK_ASP_TIM03_T',
    'NIXD0043': 'HK_ASP_TIM04_T',
    'NIXD0044': 'HK_ASP_TIM05_T',
    'NIXD0045': 'HK_ASP_TIM06_T',
    'NIXD0046': 'HK_ASP_TIM07_T',
    'NIXD0047': 'HK_ASP_TIM08_T',
    'NIXD0048': 'HK_ASP_VSENSA_V',
    'NIXD0049': 'HK_ASP_VSENSB_V',
    'NIXD0050': 'HK_ATT_V',
    'NIXD0051': 'HK_ATT_T',
    'NIXD0052': 'HK_HV_01_16_V',
    'NIXD0053': 'HK_HV_17_32_V',
    'NIXD0054': 'DET_Q1_T',
    'NIXD0055': 'DET_Q2_T',
    'NIXD0056': 'DET_Q3_T',
    'NIXD0057': 'DET_Q4_T',
    'NIXD0058': 'HK_DET_C',
    'NIXD0059': 'Flare location',
    'NIXD0060': 'Non-thermal flare index',
    'NIXD0061': 'Thermal flare index',
    'NIXD0064': 'Attenuator motion flag',
    'NIXD0066': 'HV1 depolar in progress',
    'NIXD0067': 'HV2 depolar in progress',
    'NIXD0068': 'ATT AB flag - OPEN',
    'NIXD0069': 'ATT BC flag - CLOSED',
    'NIXD0070': 'En/Dis Detector Status',
    'NIXD0074': 'HV regulators mask',
    'NIXD0075': 'HK_ATT_C',
    'NIXD0077': 'TC(20,128) seq cnt',
    'NIXD0078': 'Rejected SpW packets',
    'NIXD0079': 'Received SpW packets',
    'NIXD0080': 'SPW1 - power status',
    'NIXD0081': 'SPW0 - power status',
    'NIXD0082': 'Q4 - power status',
    'NIXD0083': 'Q3 - power status',
    'NIXD0084': 'Q2 - power status',
    'NIXD0085': 'Q1 - power status',
    'NIXD0086': 'ASPECT B - power status',
    'NIXD0087': 'ASPECT A - power status',
    'NIXD0088': 'ATT M2 - moving',
    'NIXD0089': 'ATT M1 - moving',
    'NIXD0090': 'HV17-32 - enabled status',
    'NIXD0091': 'HV01-16 - enabled status',
    'NIXD0092': 'LV - enabled status',
    'NIXD0093': 'SPW open',
    'NIXD0094': 'LV powered',
    'NIXD0095': 'HV01-16 powered',
    'NIXD0096': 'HV17-32 powered',
    'NIXD0097': 'SPW 0 powered',
    'NIXD0098': 'SPW 1 powered',
    'NIXD0099': 'SPW 0 enabled',
    'NIXD0100': 'SPW 1 enabled',
    'NIXD0101': 'Compr Sch LC S',
    'NIXD0102': 'Compr Sch LC K',
    'NIXD0103': 'Compr Sch LC M',
    'NIXD0104': 'Compr Sch TRIG ACC S 30',
    'NIXD0105': 'Compr Sch TRIG ACC K 30',
    'NIXD0106': 'Compr Sch TRIG ACC M 30',
    'NIXD0107': 'Enrg bin edge mask-up 30',
    'NIXD0108': 'Compr Sch BCKG S',
    'NIXD0109': 'Compr Sch BCKG K',
    'NIXD0110': 'Compr Sch BCKG M',
    'NIXD0111': 'Enrg bin edge mask-up 31',
    'NIXD0112': 'Compr Sch TRIG ACC S',
    'NIXD0113': 'Compr Sch TRIG ACC K',
    'NIXD0114': 'Compr Sch TRIG ACC M',
    'NIXD0115': 'Compr Sch SPECTRUM S',
    'NIXD0116': 'Compr Sch SPECTRUM K',
    'NIXD0117': 'Compr Sch SPECTRUM M',
    'NIXD0118': 'Compr Sch VARIANCE S',
    'NIXD0119': 'Compr Sch VARIANCE K',
    'NIXD0120': 'Compr Sch VARIANCE M',
    'NIXD0126': 'Compr Sch CAL S',
    'NIXD0127': 'Compr Sch CAL K',
    'NIXD0128': 'Compr Sch CAL M',
    'NIXD0129': 'SbSpect1 No spect pts-1',
    'NIXD0130': 'SbSpect1 No sum chn-1',
    'NIXD0131': 'SbSpect1 lowest ch',
    'NIXD0132': 'SbSpect2 No spect pts-1',
    'NIXD0133': 'SbSpect2 No sum chn-1',
    'NIXD0134': 'SbSpect2 lowest ch',
    'NIXD0135': 'SbSpect3 No spect pts-1',
    'NIXD0136': 'SbSpect3 No sum chn-1',
    'NIXD0137': 'SbSpect3 lowest ch',
    'NIXD0138': 'SbSpect4 No spect pts-1',
    'NIXD0139': 'SbSpect4 No sum chn-1',
    'NIXD0140': 'SbSpect4 lowest ch',
    'NIXD0141': 'SbSpect5 No spect pts-1',
    'NIXD0142': 'SbSpect5 No sum chn-1',
    'NIXD0143': 'SbSpect5 lowest ch',
    'NIXD0144': 'SbSpect6 No spect pts-1',
    'NIXD0145': 'SbSpect6 No sum chn-1',
    'NIXD0146': 'SbSpect6 lowest ch',
    'NIXD0147': 'SbSpect7 No spect pts-1',
    'NIXD0148': 'SbSpect7 No sum chn-1',
    'NIXD0149': 'SbSpect7 lowest ch',
    'NIXD0150': 'SbSpect8 No spect pts-1',
    'NIXD0151': 'SbSpect8 No sum chn-1',
    'NIXD0152': 'SbSpect8 lowest ch',
    'NIXD0153': 'Detector ID - sci data',
    'NIXD0154': 'Energy ID - sci data',
    'NIXD0155': 'Detector ID',
    'NIXD0156': 'Pixel ID',
    'NIXD0157': 'S - SbSpect ID - 1',
    'NIXD0158': 'Pixel ID - sci data',
    'NIXD0159': 'Continuation bits',
    'NIXD0163': 'HKSelftest is exec stat',
    'NIXD0164': 'Memory ser exec stat fla',
    'NIXD0165': 'FDIR stat msk HK curr ch',
    'NIXD0166': 'Autonomous ASW boot stat',
    'NIXD0167': 'Memory load ena flag',
    'NIXD0168': 'Overruns for tasks',
    'NIXD0169': 'Watchdog state',
    'NIXD0302': 'WDT reason for reboot',
    'NIXD0303': 'Currently running IDPU',
    'NIXD0304': 'EDAC reason for reboot',
    'NIXD0358': 'SpW line',
    'NIXD0359': 'SpW internal failure',
    'NIXD0366': 'Register mask applied',
    'NIXD0367': 'Register 1 (ICOMP)',
    'NIXD0368': 'Register 2 (IREQ)',
    'NIXD0376': 'Register 5 (TPEAK)',
    'NIXD0377': 'Register 6 (I0)',
    'NIXD0378': 'Register 7 (RDELAY)',
    'NIXD0379': 'Register 8 (GAIN)',
    'NIXD0380': 'Register 9 (SPY)',
    'NIXD0381': 'Register 10 (VREF2P)',
    'NIXD0382': 'Register 11 (TUNE)',
    'NIXD0407': 'Pixel mask - detail',
    'NIXD0410': 'TH - Ch 0',
    'NIXD0411': 'TH - Ch 1',
    'NIXD0412': 'TH - Ch 2',
    'NIXD0413': 'TH - Ch 3',
    'NIXD0414': 'TH - Ch 4',
    'NIXD0415': 'TH - Ch 5',
    'NIXD0416': 'TH - Ch 6',
    'NIXD0417': 'TH - Ch 7',
    'NIXD0418': 'TH - Ch 8',
    'NIXD0419': 'TH - Ch 9',
    'NIXD0420': 'TH - Ch 10',
    'NIXD0421': 'TH - Ch 11',
    'NIXD0422': 'TH - Ch 12',
    'NIXD0423': 'TH - Ch 13',
    'NIXD0424': 'TH - Ch 14',
    'NIXD0425': 'TH - Ch 15',
    'NIXD0426': 'TH - Ch 16',
    'NIXD0427': 'TH - Ch 17',
    'NIXD0428': 'TH - Ch 18',
    'NIXD0429': 'TH - Ch 19',
    'NIXD0430': 'TH - Ch 20',
    'NIXD0431': 'TH - Ch 21',
    'NIXD0432': 'TH - Ch 22',
    'NIXD0433': 'TH - Ch 23',
    'NIXD0434': 'TH - Ch 24',
    'NIXD0435': 'TH - Ch 25',
    'NIXD0436': 'TH - Ch 26',
    'NIXD0437': 'TH - Ch 27',
    'NIXD0438': 'TH - Ch 28',
    'NIXD0439': 'TH - Ch 29',
    'NIXD0440': 'TH - Ch 30',
    'NIXD0441': 'TH - Ch 31',
    'NIXD0442': 'E1 (low bound for spec)',
    'NIXD0443': 'E2 (high bound for spec)',
    'NIXG0001': 'IDPU + reboot mask',
    'NIXG0009': 'SSID global 1',
    'NIXG0010': 'SSID global 2',
    'NIXG0011': 'SSID global 4',
    'NIXG0012': 'SSID global 5',
    'NIXG0013': 'SSID global 6',
    'NIXG0014': 'SSID global 7',
    'NIXG0015': 'SSID global 8',
    'NIXG0016': 'SSID global 9',
    'NIXG0017': 'SSID global 10',
    'NIXG0018': 'SSID global 11',
    'NIXG0019': 'SSID global 12',
    'NIXG0020': 'Flare - global',
    'NIXG0033': 'HW/SW status 1',
    'NIXG0034': 'HW/SW status 2',
    'NIXG0042': 'Energy bound',
    'NIXG0064': 'HK global 15',
    'NIXG0070': 'HW/SW status 3',
    'NIXG0071': 'HW/SW status 4',
    'NIXG0135': 'Boot status flags',
    'NIXG0160': 'Compression Schema',
    'NIXG0250': 'HK global 1',
    'NIXG0251': 'HK global 2',
    'NIXG0252': 'HK global 3',
    'NIXG0253': 'HK global 4',
    'NIXG0254': 'HK global 5',
    'NIXG0255': 'HK global 7',
    'NIXG0256': 'HK global 8',
    'NIXG0257': 'HK global 9',
    'NIXG0258': 'HK global 10',
    'NIXG0259': 'HK global 11',
    'NIXG0260': 'HK global 12',
    'NIXG0261': 'HK global 13',
    'NIXG0262': 'HK global 14',
    'NIXG0263': 'HK global 6',
    'NIXG0300': 'SbSpect1',
    'NIXG0301': 'SbSpect2',
    'NIXG0302': 'SbSpect3',
    'NIXG0303': 'SbSpect4',
    'NIXG0304': 'SbSpect5',
    'NIXG0305': 'SbSpect6',
    'NIXG0306': 'SbSpect7',
    'NIXG0307': 'SbSpect8',
    'NIXG0358': 'Spacewire status',
    'NIXG0366': 'Register mask applied',
    'NIXG0367': 'Reg ICOMP IREQ.',
    'NIXG0369': 'Register 3 (TH) 1',
    'NIXG0370': 'Register 3 (TH) 2',
    'NIXG0371': 'Register 3 (TH) 3',
    'NIXG0372': 'Register 3 (TH) 4',
    'NIXG0373': 'Register 3 (TH) 5',
    'NIXG0374': 'Register 3 (TH) 6',
    'NIXG0375': 'Register 3 (TH) 7',
    'NIXG0376': 'Reg 5-11 TH SelfTest',
    'NIXG0377': 'Register 3 (TH) 8',
    'NIXG0403': 'Calib structure',
    'NIXG0404': 'SSID global 3',
    'NIXG0405': 'SSID global 13',
    'NIXS0001': 'DPU_SPW_C criter',
    'NIXS0002': 'DPU_DET_C criter',
    'NIXS0003': 'ATT_C criteria',
    'ZZPAD008': 'Filler 8 bits',
    'ZZPAD016': 'Filler 16 bits',
    'ZZPAD024': 'Filler 24 bits',
    'ZZPAD032': 'Filler 32 bits'
}
SCOS_DESC = {
    'NIX00001':
    '16-bit copy of the Packet ID',
    'NIX00002':
    '16-bit copy of the Packet Sequence',
    'NIX00003':
    'Failure ID',
    'NIX00004':
    'Packet type from the received TC',
    'NIX00005':
    'Packet sub-type from the received TC',
    'NIX00006':
    'Received checksum',
    'NIX00007':
    'Calculated CRC',
    'NIX00008':
    'Position in byte of the first inconsistent parameter',
    'NIX00009':
    'Received value of the first inconsistent parameter',
    'NIX00010':
    'Packet sequence flags',
    'NIX00011':
    'Packet sequence count',
    'NIX00012':
    'Current operation mode',
    'NIX00013':
    'Target mode',
    'NIX00014':
    'MID',
    'NIX00015':
    'Start Address',
    'NIX00016':
    'Length - number of bytes in block',
    'NIX00017':
    'Received segment mask',
    'NIX00018':
    'Expected segment mask',
    'NIX00019':
    'Mask of FDIR function',
    'NIX00020':
    'Structure ID (SID)',
    'NIX00021':
    'FDIR parameter',
    'NIX00022':
    'FDIR parameter ID',
    'NIX00023':
    'Uploaded FDIR parameter value',
    'NIX00024':
    'Memory operation',
    'NIX00025':
    'Service Type',
    'NIX00026':
    'Service Subtype',
    'NIX00027':
    'Received length',
    'NIX00028':
    'Expected packet length',
    'NIX00029':
    'Version number',
    'NIX00030':
    'Packet type',
    'NIX00031':
    'Data field header flag',
    'NIX00032':
    'CCSDS secondary header flag',
    'NIX00033':
    'PUS version',
    'NIX00034':
    'FLASH operation state',
    'NIX00035':
    'LUT ID',
    'NIX00037':
    'Unique data request number S_h',
    'NIX00038':
    'Start Time - sub-seconds S_h',
    'NIX00039':
    'Tmin (relative) [1/10 seconds]',
    'NIX00040':
    'Tmax (relative) [1/10 seconds]',
    'NIX00041':
    'Tdivision unit [1/10 seconds]',
    'NIX00042':
    'Selftest bitmask',
    'NIX00043':
    'Last executed state',
    'NIX00044':
    'Selected MID from LoadASW module',
    'NIX00045':
    'Image MID from LoadASW module',
    'NIX00046':
    'Image pages from LoadASW module',
    'NIX00047':
    'Image CRC from LoadASW module',
    'NIX00048':
    'Calculated CRC (buffered FLASH) from LoadASW module',
    'NIX00049':
    'Number of pages from ExecuteASW module',
    'NIX00050':
    'Stored CRC from ExecuteASW module',
    'NIX00051':
    'Calculated CRC from ExecuteASW module',
    'NIX00052':
    'Selected MID to be save ASW imag',
    'NIX00053':
    'Selected pages to save as ASW image',
    'NIX00054':
    'TC Packet ID of the oldest unprocessed TC packet',
    'NIX00055':
    'TC Packet Sequence Control of the oldest unprocessed TC packet',
    'NIX00056':
    'Received Ack flags (4b)',
    'NIX00057':
    'StartASW state',
    'NIX00058':
    'Invalid SID',
    'NIX00059':
    'Heartbeat value - OBT Coarse Time',
    'NIX00060':
    'Flare Message 3,25 4',
    'NIX00061':
    'X Location',
    'NIX00062':
    'Y Location',
    'NIX00063':
    'Flare Duration 3,25',
    'NIX00064':
    'Received FDIR function mask',
    'NIX00065':
    'Counts',
    'NIX00066':
    'Requested page address',
    'NIX00067':
    'Address after operation',
    'NIX00068':
    'Allowed mask of FDIR function',
    'NIX00069':
    'System ID',
    'NIX00070':
    'Operation ID',
    'NIX00071':
    'Footprints to identify which tests are currently running.',
    'NIX00072':
    'Median value of trigger',
    'NIX00073':
    'Maximum value of trigger',
    'NIX00074':
    'Footprints to identify which tests have been selected, but '
    'cannot be executed. 0...not selected, 1...selected. (see 74)',
    'NIX00075':
    'Start address in tested MID',
    'NIX00076':
    'Total number of attenuator motions over the mission',
    'NIX00077':
    'End address in tested MID',
    'NIX00078':
    'Aspect Diode A0',
    'NIX00079':
    'Aspect Diode A1',
    'NIX00080':
    'Aspect Diode B0',
    'NIX00081':
    'Aspect Diode B1',
    'NIX00082':
    'Length of the reported data (in single addressable unit with '
    'count starting from zero)',
    'NIX00083':
    'MUL = 1',
    'NIX00084':
    'MUL = 4',
    'NIX00085':
    'FDIR function status',
    'NIX00086':
    'Page with failed CRC check',
    'NIX00087':
    'Data processing level',
    'NIX00088':
    'Summing value',
    'NIX00089':
    'Number of samples',
    'NIX00090':
    'ChA diode 0 voltage',
    'NIX00091':
    'ChA diode 1 voltage',
    'NIX00092':
    'ChB diode 0 voltage',
    'NIX00093':
    'ChB diode 1 voltage',
    'NIX00094':
    'Attenuator currents',
    'NIX00096':
    'Limit value of parameter that is out of bound',
    'NIX00097':
    'ID of HK line',
    'NIX00098':
    'Actual value of parameter out of bounds',
    'NIX00099':
    'MID that was checked',
    'NIX00100':
    'Detector number',
    'NIX00101':
    'Mean ASIC temperature',
    'NIX00102':
    'Std dev of the ASIC temperature',
    'NIX00103':
    'Group number',
    'NIX00104':
    'Number of structures (NxP), max. 682',
    'NIX00105':
    'Channel number',
    'NIX00106':
    'Mean of the ASIC ADC channel',
    'NIX00107':
    'Std dev of the ASIC ADC channel',
    'NIX00108':
    'Detected threshold',
    'NIX00109':
    'Mean of the ADC group',
    'NIX00110':
    'Std dev of the ADC group',
    'NIX00112':
    'Selected MID',
    'NIX00113':
    'MID from ASW image header',
    'NIX00114':
    'Number of pages from ASW image header',
    'NIX00115':
    'CRC from ASW image header',
    'NIX00116':
    'Calculated CRC',
    'NIX00117':
    'Size of ASW image to store',
    'NIX00119':
    'Pixel ID (4 bits)',
    'NIX00120':
    'SSID',
    'NIX00121':
    'Start Time - sec',
    'NIX00122':
    'Duratior',
    'NIX00123':
    'Quiet Time',
    'NIX00124':
    'Live Time',
    'NIX00125':
    'Average temperature',
    'NIX00126':
    'Movement type',
    'NIX00127':
    'Initial flags',
    'NIX00128':
    'End flags',
    'NIX00129':
    'Main context file flag',
    'NIX00130':
    'Backup context file flag',
    'NIX00131':
    'Processor State Register',
    'NIX00132':
    'Trap Base Register',
    'NIX00133':
    'Leon: Program Counter',
    'NIX00134':
    'Leon: Next Program Counter',
    'NIX00142':
    'Received error code',
    'NIX00143':
    'Received byte count',
    'NIX00144':
    'CCSDS header bytes received',
    'NIX00145':
    'Operation duration of SDRAM zeroing',
    'NIX00146':
    'Sp - Number of compressed spectral points',
    'NIX00147':
    'SuSW Parameter ID',
    'NIX00148':
    'SuSW Parameter subID',
    'NIX00149':
    'SuSW Parameter data',
    'NIX00150':
    'ASW Parameter ID',
    'NIX00151':
    'ASW Parameter subID',
    'NIX00152':
    'ASW Parameter data',
    'NIX00158':
    'Compressed spectral point',
    'NIX00159':
    'Number of structures M',
    'NIX00160':
    'Subspectrum Mask',
    'NIX00173':
    'Mask of error chips',
    'NIX00175':
    'ID of edac module whose scrubbing rate change',
    'NIX00176':
    'New scrubbing rate in effect',
    'NIX00177':
    'Old scrubbing rate that was changed',
    'NIX00178':
    'Counts leading to change of rate',
    'NIX00179':
    'Threshold that was exceeded (upper or lower',
    'NIX00180':
    'Period of single event upset checking used',
    'NIX00181':
    'HV line 0 1 to 16 1 17 to 32',
    'NIX00182':
    'Original state',
    'NIX00183':
    'New state',
    'NIX00184':
    'Initialisation status',
    'NIX00185':
    'Total number of files',
    'NIX00186':
    'Number of bad blocks',
    'NIX00187':
    'Number of error blocks',
    'NIX00188':
    'Number of free blocks',
    'NIX00189':
    'Attenuator movement',
    'NIX00190':
    'Address where SDRAM partial memory test failed',
    'NIX00191':
    'Address where SDRAM full memory test failed',
    'NIX00192':
    'Address where pattern memory test failed',
    'NIX00193':
    'FDIR function triggering TM(5,4)',
    'NIX00194':
    'Selected start file number',
    'NIX00195':
    'Selected end file number',
    'NIX00196':
    'Maximum file number to select',
    'NIX00197':
    'Data structure (counted from 0)',
    'NIX00199':
    'Register mask',
    'NIX00200':
    'Allowed minimum for the given parameter ID',
    'NIX00201':
    'Allowed maximum for the given parameter ID',
    'NIX00202':
    "Expected length of TC's data (without headers or CRC)",
    'NIX00203':
    'Requested value to be set',
    'NIX00204':
    'Received length of TCs data (without headers or CRC)',
    'NIX00206':
    'Selected configuration value',
    'NIX00207':
    'Maximum subsystem ID available',
    'NIX00208':
    'System ID selected',
    'NIX00209':
    'Subsystem ID selected',
    'NIX00210':
    'Exceeded configuration limit',
    'NIX00215':
    'Lower accumulator bound',
    'NIX00216':
    'Number of summed accumulators per spectral point',
    'NIX00217':
    'Number of spectral points',
    'NIX00218':
    'Selected test bitmask not available for current SW',
    'NIX00222':
    'Start file',
    'NIX00223':
    'Flash block offset - start file',
    'NIX00224':
    'End file',
    'NIX00225':
    'Flash block offset - end file',
    'NIX00226':
    'Number of processed files',
    'NIX00227':
    'Number of bad blocks before recovery attempts',
    'NIX00228':
    'Number of bad blocks after recovery attempts',
    'NIX00229':
    'Number of error blocks before recovery attempts',
    'NIX00230':
    'Number of error blocks after recovery attempts',
    'NIX00231':
    'Number of free blocks before recovery attempts',
    'NIX00232':
    'Number of free blocks after recovery attempts',
    'NIX00233':
    'Number of filled blocks before recovery attempts',
    'NIX00234':
    'Number of filled blocks after recovery attempts',
    'NIX00235':
    'Position sensor AB status',
    'NIX00236':
    'Position sensor BC status',
    'NIX00237':
    'Motor 1 used',
    'NIX00238':
    'Motor 2 used',
    'NIX00239':
    'number of QL iterations checked',
    'NIX00240':
    'number of yellow flags within Nbad iterations for detector to be '
    'red-flagged',
    'NIX00241':
    'New active detector mask',
    'NIX00242':
    'Compressed Trigger accumulator 0',
    'NIX00243':
    'Compressed Trigger accumulator 1',
    'NIX00244':
    'Compressed Trigger accumulator 2',
    'NIX00245':
    'Compressed Trigger accumulator 3',
    'NIX00246':
    'Compressed Trigger accumulator 4',
    'NIX00247':
    'Compressed Trigger accumulator 5',
    'NIX00248':
    'Compressed Trigger accumulator 6',
    'NIX00249':
    'Compressed Trigger accumulator 7',
    'NIX00250':
    'Compressed Trigger accumulator 8',
    'NIX00251':
    'Compressed Trigger accumulator 9',
    'NIX00252':
    'Compressed Trigger accumulator 10',
    'NIX00253':
    'Compressed Trigger accumulator 11',
    'NIX00254':
    'Compressed Trigger accumulator 12',
    'NIX00255':
    'Compressed Trigger accumulator 13',
    'NIX00256':
    'Compressed Trigger accumulator 14',
    'NIX00257':
    'Compressed Trigger accumulator 15',
    'NIX00258':
    'Number of energy groups',
    'NIX00259':
    'Number of data elements D',
    'NIX00260':
    'Compressed pixels counts',
    'NIX00261':
    'Flux',
    'NIX00262':
    'Number of detectors',
    'NIX00263':
    'Real visibility component',
    'NIX00264':
    'Imaginary visibility component',
    'NIX00265':
    'Base pixel mask (RCR0)',
    'NIX00266':
    'Energy bin edge mask - low boundary',
    'NIX00267':
    'Compressed combined trigger accumulator',
    'NIX00268':
    'Compressed summed counts',
    'NIX00269':
    'Closing time offset',
    'NIX00270':
    'Number of energies',
    'NIX00271':
    'Number of data points Lightcurves',
    'NIX00272':
    'Compressed lightcurves',
    'NIX00273':
    'Number of data points Triggers',
    'NIX00274':
    'Compressed triggers',
    'NIX00275':
    'Number of data points RCR',
    'NIX00276':
    'RCR',
    'NIX00277':
    'Number of data points Background',
    'NIX00278':
    'Compressed background',
    'NIX00279':
    'Samples per variance values',
    'NIX00280':
    'Number of samples Variance',
    'NIX00281':
    'Compressed Variance',
    'NIX00282':
    'Energy mask',
    'NIX00283':
    'Flare Location Z (arcmin)',
    'NIX00284':
    'Flare Location Y (arcmin)',
    'NIX00285':
    'UBSD counter',
    'NIX00286':
    'PALD counter',
    'NIX00287':
    'Start time coarse SCET',
    'NIX00288':
    'End time coarse SCET',
    'NIX00289':
    'Highest flare flag',
    'NIX00290':
    'TM byte volume',
    'NIX00291':
    'Average Z location',
    'NIX00292':
    'Average Y location',
    'NIX00293':
    'Flare TM processing status',
    'NIX00294':
    'Number of listed flares',
    'NIX00297':
    'Config parameter 236,16',
    'NIX00298':
    'Config parameter ID 236,16',
    'NIX00299':
    'EID',
    'NIX00300':
    'Footprints to identify which test has been executed 0-not '
    'executed, 1-executed.',
    'NIX00301':
    'Test result - success/failure flags',
    'NIX00303':
    'Software version',
    'NIX00304':
    'Previous mode',
    'NIX00305':
    'Actual mode',
    'NIX00306':
    'Mode transition reason',
    'NIX00307':
    'CPU load',
    'NIX00308':
    'HV PSU identification (Bit mask 0x01)',
    'NIX00309':
    'Flare strength',
    'NIX00311':
    'Timer IRQ counter',
    'NIX00312':
    'Space Wire IRQ counter',
    'NIX00313':
    'ADC Read IRQ counter',
    'NIX00323':
    'CPU load in percentages - CPU overload condition detected '
    'warning report',
    'NIX00324':
    'Limit T1',
    'NIX00325':
    'Limit T2',
    'NIX00326':
    'Limit N1',
    'NIX00327':
    'Limit N2',
    'NIX00328':
    'Current N1',
    'NIX00329':
    'Current N2',
    'NIX00333':
    'Failed temperature sensor',
    'NIX00334':
    'Failed regulators',
    'NIX00336':
    'Requested mode',
    'NIX00337':
    'Detector IRQ counter',
    'NIX00338':
    'Current time in ms',
    'NIX00339':
    'Memory ID',
    'NIX00340':
    'Direction of the attenuator move',
    'NIX00341':
    'Current status which motor was used',
    'NIX00342':
    'Status of attenuator position sensors',
    'NIX00344':
    'Current working timeout',
    'NIX00345':
    'Bitmask of detectors above the limit (32 detectors)',
    'NIX00346':
    'Identification of a detector with the highest rate',
    'NIX00347':
    'Limit of the high rate',
    'NIX00348':
    "Bitmask of quadrants with overcurrent detected (log. '1' ... "
    'overcurrent)',
    'NIX00349':
    'Actual current quadrant 1',
    'NIX00350':
    'Actual current quadrant 2',
    'NIX00351':
    'Actual current quadrant 3',
    'NIX00352':
    'Actual current quadrant 4',
    'NIX00353':
    'Limit of detectors quadrant overcurrent',
    'NIX00354':
    'Quadrant identification (1..4)',
    'NIX00355':
    'Temperature (actual, leading to generation of this event)',
    'NIX00357':
    'Counter of HV PSU failures since the instrument power-on',
    'NIX00361':
    'Actual rate of the detector with the highest rate',
    'NIX00362':
    'Quarters requested for operations',
    'NIX00363':
    'Powered quarters',
    'NIX00364':
    'Groups requested for operations',
    'NIX00365':
    'Enabled groups',
    'NIX00375':
    'Register 4 (SEL_TEST)',
    'NIX00383':
    'Register 12 (ALIMON)',
    'NIX00385':
    'Number of structures',
    'NIX00386':
    'Parameter indicating if failure occurred during enabling (1) or '
    'disabling (0) of file transfer to SSMM ie',
    'NIX00387':
    'Context segment counter of TC(22,3)',
    'NIX00388':
    'LUT type',
    'NIX00389':
    'Selected configuration',
    'NIX00390':
    'Highest configuration possible',
    'NIX00391':
    'Limit T3',
    'NIX00392':
    'Actual quiet (non-movement) time T3',
    'NIX00393':
    'Actual value of parameter out of bounds',
    'NIX00394':
    'Limit value of parameter that is out of bounds',
    'NIX00399':
    'Number of time samples',
    'NIX00401':
    'Rate control regime',
    'NIX00402':
    'SCET time stamp of the first sampl',
    'NIX00403':
    'Number of substructures',
    'NIX00404':
    'Starting time relative to timestamp in units of 1/10 seconds',
    'NIX00405':
    'Duration in units of 0.1',
    'NIX00406':
    'Number science data samples',
    'NIX00407':
    'Detectors mask',
    'NIX00408':
    'Trigger accumulator 0',
    'NIX00409':
    'Trigger accumulator 1',
    'NIX00410':
    'Trigger accumulator 2',
    'NIX00411':
    'Trigger accumulator 3',
    'NIX00412':
    'Trigger accumulator 4',
    'NIX00413':
    'Trigger accumulator 5',
    'NIX00414':
    'Trigger accumulator 6',
    'NIX00415':
    'Trigger accumulator 7',
    'NIX00416':
    'Trigger accumulator 8',
    'NIX00417':
    'Trigger accumulator 9',
    'NIX00418':
    'Trigger accumulator 10',
    'NIX00419':
    'Trigger accumulator 11',
    'NIX00420':
    'Trigger accumulator 12',
    'NIX00421':
    'Trigger accumulator 13',
    'NIX00422':
    'Trigger accumulator 14',
    'NIX00423':
    'Trigger accumulator 15',
    'NIX00436':
    'HK_DPU_1V5_V',
    'NIX00437':
    'HK_REF_2V5_V',
    'NIX00438':
    'HK_DPU_2V9_V',
    'NIX00441':
    'Delta time in 0.1 seconds',
    'NIX00442':
    'Number of pixel sets',
    'NIX00443':
    'Pixel set descriptor index',
    'NIX00445':
    'SCET coarse time',
    'NIX00446':
    'SCET fine time',
    'NIX00448':
    'Num of PROM recoverable',
    'NIX00452':
    'Compressed Spectrum (E = 0)',
    'NIX00453':
    'Compressed Spectrum (E = 1)',
    'NIX00454':
    'Compressed Spectrum (E = 2)',
    'NIX00455':
    'Compressed Spectrum (E = 3)',
    'NIX00456':
    'Compressed Spectrum (E = 4)',
    'NIX00457':
    'Compressed Spectrum (E = 5)',
    'NIX00458':
    'Compressed Spectrum (E = 6)',
    'NIX00459':
    'Compressed Spectrum (E = 7)',
    'NIX00460':
    'Compressed Spectrum (E = 8)',
    'NIX00461':
    'Compressed Spectrum (E = 9)',
    'NIX00462':
    'Compressed Spectrum (E = 10)',
    'NIX00463':
    'Compressed Spectrum (E = 11)',
    'NIX00464':
    'Compressed Spectrum (E = 12)',
    'NIX00465':
    'Compressed Spectrum (E = 13)',
    'NIX00466':
    'Compressed Spectrum (E = 14)',
    'NIX00467':
    'Compressed Spectrum (E = 15)',
    'NIX00468':
    'Compressed Spectrum (E = 16)',
    'NIX00469':
    'Compressed Spectrum (E = 17)',
    'NIX00470':
    'Compressed Spectrum (E = 18)',
    'NIX00471':
    'Compressed Spectrum (E = 19)',
    'NIX00472':
    'Compressed Spectrum (E = 20)',
    'NIX00473':
    'Compressed Spectrum (E = 21)',
    'NIX00474':
    'Compressed Spectrum (E = 22)',
    'NIX00475':
    'Compressed Spectrum (E = 23)',
    'NIX00476':
    'Compressed Spectrum (E = 24)',
    'NIX00477':
    'Compressed Spectrum (E = 25)',
    'NIX00478':
    'Compressed Spectrum (E = 26)',
    'NIX00479':
    'Compressed Spectrum (E = 27)',
    'NIX00480':
    'Compressed Spectrum (E = 28)',
    'NIX00481':
    'Compressed Spectrum (E = 29)',
    'NIX00482':
    'Compressed Spectrum (E = 30)',
    'NIX00483':
    'Compressed Spectrum (E = 31)',
    'NIX00484':
    'Compressed Trigger Accumulator',
    'NIX00485':
    'Number of integrations after 1st sample',
    'NIX00486':
    'Flash block (0-65535)',
    'NIX00487':
    'Flash page (0-63)',
    'NIX00488':
    'Bulk Science Data box index',
    'NIX00489':
    'Interrupt source index',
    'NIXD0001':
    'SW Version Number',
    'NIXD0002':
    'CPU load',
    'NIXD0003':
    'Archive Memory usage',
    'NIXD0004':
    'Identifier of IDPU',
    'NIXD0005':
    'Identifier of Active SpW link',
    'NIXD0007':
    'Compression schema EACC S-parameter',
    'NIXD0008':
    'Compression schema EACC K-parameter',
    'NIXD0009':
    'Compression schema EACC M-parameter',
    'NIXD0010':
    'Compression schema ETRIG S-parameter',
    'NIXD0011':
    'Compression schema ETRIG K-parameter',
    'NIXD0012':
    'Compression schema ETRIG M-parameter',
    'NIXD0013':
    'Emin (low energy bound)',
    'NIXD0014':
    'Emax (low energy bound)',
    'NIXD0015':
    'Energy division init - number of bins',
    'NIXD0016':
    'E1 (low bound)',
    'NIXD0017':
    'E2 (high bound)',
    'NIXD0018':
    'Energy bin edge mask - up boundary SPECTROGRAMS',
    'NIXD0021':
    'SW types - SuSW and ASW',
    'NIXD0022':
    'Instrument number',
    'NIXD0023':
    'Instrument mode',
    'NIXD0024':
    'PSU temperature',
    'NIXD0025':
    'IDPU temperature 1',
    'NIXD0026':
    'IDPU temperature 2',
    'NIXD0027':
    'IDPU 3.3V current',
    'NIXD0028':
    'IDPU 2.5V current',
    'NIXD0029':
    'IDPU 2.5V current',
    'NIXD0030':
    'IDPU SpW current',
    'NIXD0031':
    'IDPU SpW Voltage 0',
    'NIXD0032':
    'IDPU SpW Voltage',
    'NIXD0035':
    'ADC Self-check 1.5V Main',
    'NIXD0036':
    'ADC Self-check 2.5V',
    'NIXD0037':
    'IDPU 2.9V Supply Voltage',
    'NIXD0038':
    'Aspect ref A 2.5V',
    'NIXD0039':
    'Aspect ref B 2.5V',
    'NIXD0040':
    'Aspect temperature 1',
    'NIXD0041':
    'Aspect temperature 2',
    'NIXD0042':
    'Aspect temperature 3',
    'NIXD0043':
    'Aspect temperature 4',
    'NIXD0044':
    'Aspect temperature 5',
    'NIXD0045':
    'Aspect temperature 6',
    'NIXD0046':
    'Aspect temperature 7',
    'NIXD0047':
    'Aspect temperature 8',
    'NIXD0048':
    'Aspect sensor voltage A',
    'NIXD0049':
    'Aspect sensor voltage B',
    'NIXD0050':
    'Attenuator voltage',
    'NIXD0051':
    'Attenuator temperature',
    'NIXD0052':
    'HV PSU voltage 1',
    'NIXD0053':
    'HV PSU voltage 2',
    'NIXD0054':
    'Detectors temperature Q1',
    'NIXD0055':
    'Detectors temperature Q2',
    'NIXD0056':
    'Detectors temperature Q3',
    'NIXD0057':
    'Detectors temperature Q4',
    'NIXD0058':
    "All detectors' current",
    'NIXD0059':
    'Location status word',
    'NIXD0060':
    'Non-thermal flare index',
    'NIXD0061':
    'Thermal flare index',
    'NIXD0064':
    'Attenuator motion flag',
    'NIXD0066':
    'HV1 depolarization in progress',
    'NIXD0067':
    'HV2 depolarization in progress',
    'NIXD0068':
    'Attenuator AB position flag',
    'NIXD0069':
    'Attenuator BC position flag',
    'NIXD0070':
    'Enabled/Disabled Detector Status',
    'NIXD0074':
    'HV regulators mask on/off',
    'NIXD0075':
    'HK_ATT_C',
    'NIXD0077':
    'Sequence count of the last TC(20,128)',
    'NIXD0078':
    'Commands Rejected/Failed',
    'NIXD0079':
    'Commands Received',
    'NIXD0080':
    'Power status for SPW port 1',
    'NIXD0081':
    'Power status for SPW port 0',
    'NIXD0082':
    'Powered quarter Q4 status',
    'NIXD0083':
    'Powered quarter Q3 status',
    'NIXD0084':
    'Powered quarter Q2 status',
    'NIXD0085':
    'Powered quarter Q1 status',
    'NIXD0086':
    'Powered aspect channel B status',
    'NIXD0087':
    'Powered aspect channel A status',
    'NIXD0088':
    'Attenuator motor 2 moving',
    'NIXD0089':
    'Attenuator motor 1 moving',
    'NIXD0090':
    'HV 17-32 enabled status',
    'NIXD0091':
    'HV 01-16 enabled status',
    'NIXD0092':
    'LV enabled status',
    'NIXD0093':
    'SpW open',
    'NIXD0094':
    'LV powered',
    'NIXD0095':
    'HV01-16 powered',
    'NIXD0096':
    'HV17-32 powered',
    'NIXD0097':
    'SPW 0 powered',
    'NIXD0098':
    'SPW 1 powered',
    'NIXD0099':
    'SPW 0 enabled',
    'NIXD0100':
    'SPW 1 enabled',
    'NIXD0101':
    'Compression Schema Lightcurves S-parameter',
    'NIXD0102':
    'Compression schema Lightcurves K-parameter',
    'NIXD0103':
    'Compression schema Lightcurves M-parameter',
    'NIXD0104':
    'Compression Schema Trigger accum S-parameter SSID 30',
    'NIXD0105':
    'Compression schema Trigger accum K-parameter SSID 30',
    'NIXD0106':
    'Compression schema Trigger accum M-parameter SSID 30',
    'NIXD0107':
    'Energy bin edge mask - up boundary SSID 30',
    'NIXD0108':
    'Compression Schema Background S-parameter',
    'NIXD0109':
    'Compression schema Background K-parameter',
    'NIXD0110':
    'Compression schema Background M-parameter',
    'NIXD0111':
    'Energy bin edge mask - up boundary SSID 31',
    'NIXD0112':
    'Compression Schema Trigger accum S-parameter',
    'NIXD0113':
    'Compression schema Trigger accum K-parameter',
    'NIXD0114':
    'Compression schema Trigger accum M-parameter',
    'NIXD0115':
    'Compression Schema Spectrum accum S-parameter',
    'NIXD0116':
    'Compression schema Spectrum accum K-parameter',
    'NIXD0117':
    'Compression schema Spectrum accum M-parameter',
    'NIXD0118':
    'Compression Schema Variance S-parameter',
    'NIXD0119':
    'Compression schema Variance K-parameter',
    'NIXD0120':
    'Compression schema Variance M-parameter',
    'NIXD0126':
    'Compression Schema Calib accum S-parameter',
    'NIXD0127':
    'Compression schema Calib accum K-parameter',
    'NIXD0128':
    'Compression schema Calib accum M-parameter',
    'NIXD0129':
    'Subspectrum 1: number of spectral points - 1 (=N1)',
    'NIXD0130':
    'Subspectrum 1: number of summ chan in spect point-1',
    'NIXD0131':
    'Subspectrum 1: lowest channel in subspectrum',
    'NIXD0132':
    'Subspectrum 2: number of spectral points - 1 (=N2)',
    'NIXD0133':
    'Subspectrum 2: number of summ chan in spect point-1',
    'NIXD0134':
    'Subspectrum 2: lowest channel in subspectrum',
    'NIXD0135':
    'Subspectrum 3: number of spectral points - 1 (=N3)',
    'NIXD0136':
    'Subspectrum 3: number of summ chan in spect point-1',
    'NIXD0137':
    'Subspectrum 3: lowest channel in subspectrum',
    'NIXD0138':
    'Subspectrum 4: number of spectral points - 1 (=N4)',
    'NIXD0139':
    'Subspectrum 4: number of summ chan in spect point-1',
    'NIXD0140':
    'Subspectrum 4: lowest channel in subspectrum',
    'NIXD0141':
    'Subspectrum 5: number of spectral points - 1 (=N5)',
    'NIXD0142':
    'Subspectrum 5: number of summ chan in spect point-1',
    'NIXD0143':
    'Subspectrum 5: lowest channel in subspectrum',
    'NIXD0144':
    'Subspectrum 6: number of spectral points - 1 (=N6)',
    'NIXD0145':
    'Subspectrum 6: number of summ chan in spect point-1',
    'NIXD0146':
    'Subspectrum 6: lowest channel in subspectrum',
    'NIXD0147':
    'Subspectrum 7: number of spectral points - 1 (=N7)',
    'NIXD0148':
    'Subspectrum 7: number of summ chan in spect point-1',
    'NIXD0149':
    'Subspectrum 7: lowest channel in subspectrum',
    'NIXD0150':
    'Subspectrum 8: number of spectral points - 1 (=N8)',
    'NIXD0151':
    'Subspectrum 8: number of summ chan in spect point-1',
    'NIXD0152':
    'Subspectrum 8: lowest channel in subspectrum',
    'NIXD0153':
    'Detector ID - science data',
    'NIXD0154':
    'Energy ID - science data',
    'NIXD0155':
    'Detector ID',
    'NIXD0156':
    'Pixel ID',
    'NIXD0157':
    'S - Subspectrum ID - 1',
    'NIXD0158':
    'Pixel ID - science data',
    'NIXD0159':
    'Continuation bits',
    'NIXD0168':
    'First task that overrun allocated execution time. Frame and task '
    'number',
    'NIXD0302':
    'WDT reason for reboot',
    'NIXD0303':
    'Currently running IDPU',
    'NIXD0304':
    'EDAC reason for reboot',
    'NIXD0359':
    'SpW internal failure identification',
    'NIXD0366':
    'mask applied',
    'NIXD0367':
    'Register 1 (ICOMP)',
    'NIXD0368':
    'Register 2 (IREQ)',
    'NIXD0376':
    'Register 5 (TPEAK)',
    'NIXD0377':
    'Register 6 (I0)',
    'NIXD0378':
    'Register 7 (RDELAY)',
    'NIXD0379':
    'Register 8 (GAIN)',
    'NIXD0380':
    'Register 9 (SPY)',
    'NIXD0381':
    'Register 10 (VREF2P)',
    'NIXD0382':
    'Register 11 (TUNE)',
    'NIXD0407':
    'Pixel mask - detail',
    'NIXD0410':
    'TH - Ch 0',
    'NIXD0411':
    'TH - Ch 1',
    'NIXD0412':
    'TH - Ch 2',
    'NIXD0413':
    'TH - Ch 3',
    'NIXD0414':
    'TH - Ch 4',
    'NIXD0415':
    'TH - Ch 5',
    'NIXD0416':
    'TH - Ch 6',
    'NIXD0417':
    'TH - Ch 7',
    'NIXD0418':
    'TH - Ch 8',
    'NIXD0419':
    'TH - Ch 9',
    'NIXD0420':
    'TH - Ch 10',
    'NIXD0421':
    'TH - Ch 11',
    'NIXD0422':
    'TH - Ch 12',
    'NIXD0423':
    'TH - Ch 13',
    'NIXD0424':
    'TH - Ch 14',
    'NIXD0425':
    'TH - Ch 15',
    'NIXD0426':
    'TH - Ch 16',
    'NIXD0427':
    'TH - Ch 17',
    'NIXD0428':
    'TH - Ch 18',
    'NIXD0429':
    'TH - Ch 19',
    'NIXD0430':
    'TH - Ch 20',
    'NIXD0431':
    'TH - Ch 21',
    'NIXD0432':
    'TH - Ch 22',
    'NIXD0433':
    'TH - Ch 23',
    'NIXD0434':
    'TH - Ch 24',
    'NIXD0435':
    'TH - Ch 25',
    'NIXD0436':
    'TH - Ch 26',
    'NIXD0437':
    'TH - Ch 27',
    'NIXD0438':
    'TH - Ch 28',
    'NIXD0439':
    'TH - Ch 29',
    'NIXD0440':
    'TH - Ch 30',
    'NIXD0441':
    'TH - Ch 31',
    'NIXG0001':
    'EDAC reason for reboot (mask 0xC0) / WDT reason for reboot (mask '
    '0x3E) / Currently running IDPU (mask 0x01)',
    'NIXG0009':
    'SSID global 1',
    'NIXG0010':
    'SSID global 2',
    'NIXG0011':
    'SSID global 4',
    'NIXG0012':
    'SSID global 5',
    'NIXG0013':
    'SSID global 6',
    'NIXG0014':
    'SSID global 7',
    'NIXG0015':
    'SSID global 8',
    'NIXG0016':
    'SSID global 9',
    'NIXG0017':
    'SSID global 10',
    'NIXG0018':
    'SSID global 11',
    'NIXG0019':
    'SSID global 12',
    'NIXG0020':
    'Flare',
    'NIXG0033':
    'HW/SW status 1',
    'NIXG0034':
    'HW/SW status 2',
    'NIXG0042':
    'Energy bound',
    'NIXG0064':
    'HK global 15',
    'NIXG0070':
    'HW/SW status 3',
    'NIXG0071':
    'HW/SW status 4',
    'NIXG0135':
    'Boot status flags',
    'NIXG0160':
    'Compression Schema Calib accum',
    'NIXG0250':
    'Instrument state',
    'NIXG0251':
    'IDPU temperature',
    'NIXG0252':
    'IDPU current',
    'NIXG0253':
    'SpW voltage',
    'NIXG0254':
    'IDPU measurements',
    'NIXG0255':
    'Aspect voltages',
    'NIXG0256':
    'Aspect temperature',
    'NIXG0257':
    'Aspect sensors',
    'NIXG0258':
    'Attenuator sensors',
    'NIXG0259':
    'HV voltages',
    'NIXG0260':
    'Detectors temperature',
    'NIXG0261':
    'Mix1 HK SID 2',
    'NIXG0262':
    'Mix2 HK SID 2',
    'NIXG0300':
    'Subspectrum 1',
    'NIXG0301':
    'Subspectrum 2',
    'NIXG0302':
    'Subspectrum 3',
    'NIXG0303':
    'Subspectrum 4',
    'NIXG0304':
    'Subspectrum 5',
    'NIXG0305':
    'Subspectrum 6',
    'NIXG0306':
    'Subspectrum 7',
    'NIXG0307':
    'Subspectrum 8',
    'NIXG0358':
    'Spacewire status - one byte container',
    'NIXG0366':
    'Register mask applied',
    'NIXG0367':
    'Reg ICOMP IREQ.',
    'NIXG0369':
    'Register 3 (TH) 1',
    'NIXG0370':
    'Register 3 (TH) 2',
    'NIXG0371':
    'Register 3 (TH) 3',
    'NIXG0372':
    'Register 3 (TH) 4',
    'NIXG0373':
    'Register 3 (TH) 5',
    'NIXG0374':
    'Register 3 (TH) 6',
    'NIXG0375':
    'Register 3 (TH) 7',
    'NIXG0376':
    'Reg 5-11 TH SelfTest',
    'NIXG0377':
    'Register 3 (TH) 8',
    'NIXG0403':
    'Calibration structure',
    'NIXG0404':
    'SSID global 3',
    'NIXG0405':
    'SSID global 13',
    'NIXS0001':
    'DPU_SPW_C limit criteria',
    'NIXS0002':
    'DPU_DET_C limit critera',
    'NIXS0003':
    'ATT_C limits criteria',
    'PIX00001':
    'SID',
    'PIX00002':
    'Maximum Packet lengths and default periods',
    'PIX00003':
    'MID',
    'PIX00004':
    'Start Address',
    'PIX00005':
    'L - Length',
    'PIX00006':
    'Mask of SSIDs to enable',
    'PIX00007':
    'N - Context Data Structure',
    'PIX00008':
    'Context Octet',
    'PIX00009':
    'SC Onboard Time CUC',
    'PIX00010':
    'TM buffers to be erased',
    'PIX00011':
    'Parameter ID for service 236',
    'PIX00013':
    'Parameter ID - SuSW',
    'PIX00014':
    'Parameter SubID - SuSW',
    'PIX00015':
    'Parameter data - SuSW',
    'PIX00016':
    'Parameter ID - ASW',
    'PIX00017':
    'Parameter subID - ASW',
    'PIX00018':
    'Parameter data - ASW',
    'PIX00019':
    'Publishing interval - s',
    'PIX00020':
    'PALD counter value',
    'PIX00021':
    'SCET coarse time 1 - low',
    'PIX00022':
    'SCET coarse time 2 - up',
    'PIX00023':
    'Cummulant 1',
    'PIX00024':
    'Cummulant 2',
    'PIX00025':
    'SCET fine time 1 - low',
    'PIX00026':
    'SCET fine time 2 - up',
    'PIX00027':
    'MemTest - Start Address',
    'PIX00028':
    'MemTest - End Address',
    'PIX00029':
    'MemTest - Tested pattern',
    'PIX00030':
    'Start file',
    'PIX00031':
    'End file',
    'PIX00032':
    'File type',
    'PIX00033':
    'Spare number or copy number (used in case of multiple backup '
    'copies of same files)',
    'PIX00047':
    'Quiet time for calibration accumulators',
    'PIX00048':
    'Trigger value',
    'PIX00049':
    'Count limit',
    'PIX00050':
    'Number of readouts',
    'PIX00051':
    'Number of readouts for averaging',
    'PIX00052':
    'Latency delay timing From 1.28 with step 1.28 and to 20,48us',
    'PIX00053':
    'Channel mask',
    'PIX00054':
    'Average count',
    'PIX00055':
    'Integration time',
    'PIX00057':
    'Group mask',
    'PIX00058':
    'Data 8 bits',
    'PIX00059':
    'Data 32 bits',
    'PIX00060':
    'Delay between pulses',
    'PIX00061':
    'Number of pulses',
    'PIX00062':
    'Register mask 2 octets, enum 12 bit mask for the following '
    'registers 1-12',
    'PIX00070':
    'Data processing level',
    'PIX00071':
    'N box structures',
    'PIX00072':
    'Start Time - seconds',
    'PIX00073':
    'Start Time - sub-seconds',
    'PIX00074':
    'End Time - seconds',
    'PIX00075':
    'End Time - sub-seconds',
    'PIX00076':
    'Unique data request number',
    'PIX00077':
    'Tmin',
    'PIX00078':
    'Tmax',
    'PIX00079':
    'Tunit',
    'PIX00080':
    'Operation mode',
    'PIX00081':
    'Mode transition',
    'PIX00082':
    'System ID',
    'PIX00083':
    'Subsystem ID',
    'PIX00085':
    'Delay',
    'PIX00086':
    'SCET time start',
    'PIX00087':
    'SCET time end',
    'PIX00088':
    'Averaging',
    'PIX00089':
    'Parameter ID 236,6,1',
    'PIX00090':
    'Parameter ID 236,6,2',
    'PIX00091':
    'Parameter ID 236,6,3',
    'PIX00092':
    'Parameter ID 236,6,4',
    'PIX00093':
    'Parameter ID 236,6,5',
    'PIX00094':
    'Parameter ID 236,6,6',
    'PIX00095':
    'Parameter ID 236,6,7',
    'PIX00096':
    'Parameter ID 236,6,8',
    'PIX00107':
    'FDIR ID',
    'PIX00108':
    'Self-test ID',
    'PIX00120':
    'Parameter (236,6)',
    'PIX00121':
    'ASW image page size',
    'PIX00122':
    'TH - Ch 0',
    'PIX00123':
    'TH - Ch 1',
    'PIX00124':
    'TH - Ch 2',
    'PIX00125':
    'TH - Ch 3',
    'PIX00126':
    'TH - Ch 4',
    'PIX00127':
    'TH - Ch 5',
    'PIX00128':
    'TH - Ch 6',
    'PIX00129':
    'TH - Ch 7',
    'PIX00130':
    'TH - Ch 8',
    'PIX00131':
    'TH - Ch 9',
    'PIX00132':
    'TH - Ch 10',
    'PIX00133':
    'TH - Ch 11',
    'PIX00134':
    'TH - Ch 12',
    'PIX00135':
    'TH - Ch 13',
    'PIX00136':
    'TH - Ch 14',
    'PIX00137':
    'TH - Ch 15',
    'PIX00138':
    'TH - Ch 16',
    'PIX00139':
    'TH - Ch 17',
    'PIX00140':
    'TH - Ch 18',
    'PIX00141':
    'TH - Ch 19',
    'PIX00142':
    'TH - Ch 20',
    'PIX00143':
    'TH - Ch 21',
    'PIX00144':
    'TH - Ch 22',
    'PIX00145':
    'TH - Ch 23',
    'PIX00146':
    'TH - Ch 24',
    'PIX00147':
    'TH - Ch 25',
    'PIX00148':
    'TH - Ch 26',
    'PIX00149':
    'TH - Ch 27',
    'PIX00150':
    'TH - Ch 28',
    'PIX00151':
    'TH - Ch 29',
    'PIX00152':
    'TH - Ch 30',
    'PIX00153':
    'TH - Ch 31',
    'PIX00154':
    'Temperature limit',
    'PIX00155':
    'Number of corrections',
    'PIX00156':
    'TLUT element',
    'PIX00200':
    'Emin',
    'PIX00201':
    'Emax',
    'PIX00202':
    'Energy unit - 1',
    'PIX00203':
    'Detector number',
    'PIX00204':
    'Register mask applied',
    'PIX00205':
    'Register',
    'PIX00206':
    'Register',
    'PIX00208':
    'Register',
    'PIX00209':
    'Register',
    'PIX00210':
    'Register',
    'PIX00211':
    'Register',
    'PIX00212':
    'Register',
    'PIX00213':
    'Register',
    'PIX00214':
    'Register',
    'PIX00215':
    'Register',
    'PIX00216':
    'Register',
    'PIX00217':
    'Subspectrum 1 - number of spectral points - 1',
    'PIX00218':
    'Subspectrum 1 - number of summed channel in spectral point - 1',
    'PIX00219':
    'Subspectrum 1 - lowest channel in subspectrum',
    'PIX00220':
    'Subspectrum 2 - number of spectral points - 1',
    'PIX00221':
    'Subspectrum 2 - number of summed channel in spectral point - 1',
    'PIX00222':
    'Subspectrum 2 - lowest channel in subspectrum',
    'PIX00223':
    'Subspectrum 3 - number of spectral points - 1',
    'PIX00224':
    'Subspectrum 3 - number of summed channel in spectral point - 1',
    'PIX00225':
    'Subspectrum 3 - lowest channel in subspectrum',
    'PIX00226':
    'Subspectrum 4 - number of spectral points - 1',
    'PIX00227':
    'Subspectrum 4 - number of summed channel in spectral point - 1',
    'PIX00228':
    'Subspectrum 4 - lowest channel in subspectrum',
    'PIX00229':
    'Subspectrum 5 - number of spectral points - 1',
    'PIX00230':
    'Subspectrum 5 - number of summed channel in spectral point - 1',
    'PIX00231':
    'Subspectrum 5 - lowest channel in subspectrum',
    'PIX00232':
    'Subspectrum 6 - number of spectral points - 1',
    'PIX00233':
    'Subspectrum 6 - number of summed channel in spectral point - 1',
    'PIX00234':
    'Subspectrum 6 - lowest channel in subspectrum',
    'PIX00235':
    'Subspectrum 7 - number of spectral points - 1',
    'PIX00236':
    'Subspectrum 7 - number of summed channel in spectral point - 1',
    'PIX00237':
    'Subspectrum 7 - lowest channel in subspectrum',
    'PIX00238':
    'Subspectrum 8 - number of spectral points - 1',
    'PIX00239':
    'Subspectrum 8 - number of summed channel in spectral point - 1',
    'PIX00240':
    'Subspectrum 8 - lowest channel in subspectrum',
    'PIX00244':
    'Define bit reduction',
    'PIX00245':
    'Calibration quiet time',
    'PIX00246':
    'Calibration maximal duration',
    'PIX00248':
    'Detector mask',
    'PIX00249':
    'Pixel mask',
    'PIX00250':
    'Enable/disable formatting of cal acc',
    'PIX00251':
    'Subspectrum mask',
    'PIX00260':
    'Enable/disable continuous accumulation',
    'PIX00261':
    'LUT type',
    'PIX00262':
    'LUT ID',
    'PIX00289':
    'FDIR parameter ID',
    'PIX00290':
    'Parameter value (236,10)',
    'PIX00301':
    'Number of structures',
    'PIX00302':
    'X-coordinate',
    'PIX00303':
    'Y-coordinate',
    'PIX00304':
    'Observation coordinate',
    'PIX00305':
    'Number of elements to write',
    'PIX00306':
    'Value to write',
    'PIX00310':
    'DAC_min',
    'PIX00311':
    'DAC_max',
    'PIX00312':
    'DAC_step',
    'PIX00390':
    'Platform Data',
    'PIX00391':
    'EPD Instrument Data',
    'PIX00392':
    'EUI Instrument Data',
    'PIX00393':
    'MAG Instrument Data',
    'PIX00394':
    'METIS Instrument Data',
    'PIX00395':
    'PHI Instrument Data',
    'PIX00396':
    'RPW Instrument Data',
    'PIX00397':
    'SoloHI Instrument Data',
    'PIX00398':
    'SPICE Instrument Data',
    'PIX00399':
    'STIX Instrument Data',
    'PIX00400':
    'SWA Instrument Data',
    'PIX00402':
    'Pixel mask RCR state = 0',
    'PIX00403':
    'Pixel mask RCR state = 1',
    'PIX00404':
    'Pixel mask RCR state = 2, North flare',
    'PIX00405':
    'Pixel mask RCR state = 2, South flare',
    'PIX00406':
    'Pixel mask RCR state = 3, North flare, variation 1',
    'PIX00407':
    'Pixel mask RCR state = 3, North flare, variation 2',
    'PIX00408':
    'Pixel mask RCR state = 3, South flare, variation 1',
    'PIX00409':
    'Pixel mask RCR state = 3, South flare, variation 2',
    'PIX00410':
    'Pixel mask RCR state = 4, North flare, variation 1',
    'PIX00411':
    'Pixel mask RCR state = 4, North flare, variation 2',
    'PIX00412':
    'Pixel mask RCR state = 4, North flare, variation 3',
    'PIX00413':
    'Pixel mask RCR state = 4, North flare, variation 4',
    'PIX00414':
    'Pixel mask RCR state = 4, South flare, variation 1',
    'PIX00415':
    'Pixel mask RCR state = 4, South flare, variation 2',
    'PIX00416':
    'Pixel mask RCR state = 4, South flare, variation 3',
    'PIX00417':
    'Pixel mask RCR state = 4, South flare, variation 4',
    'PIX00418':
    'Pixel mask RCR state = 5',
    'PIX00419':
    'Pixel Mask RCR state = 6, variation 1',
    'PIX00420':
    'Pixel Mask RCR state = 6, variation 2',
    'PIX00421':
    'Pixel Mask RCR state = 7, variation 1',
    'PIX00422':
    'Pixel Mask RCR state = 7, variation 2',
    'PIX00423':
    'Pixel Mask RCR state = 7, variation 3',
    'PIX00424':
    'Pixel Mask RCR state = 7, variation 4',
    'PIX00425':
    'Pixel Mask RCR state = 0, background detector',
    'PIX00426':
    'Pixel Mask RCR state = 1, background detector',
    'PIX00427':
    'Pixel Mask RCR state = 2, background detector',
    'PIX00428':
    'Pixel Mask RCR state = 3, background detector',
    'PIX00429':
    'Pixel Mask RCR state = 4, background detector',
    'PIX00430':
    'Pixel Mask RCR state = 5, background detector',
    'PIX00431':
    'Pixel Mask RCR state = 6, background detector',
    'PIX00432':
    'Pixel Mask RCR state = 7, background detector',
    'PIX00433':
    'RCR - group mask',
    'PIX00434':
    'RCR - L0 trigger threshold for rising RCR by removing ATT',
    'PIX00435':
    'RCR - L1 trigger threshold for rising RCR by inserting ATT',
    'PIX00436':
    'RCR - L2 trigger threshold for rising RCR by increasing area',
    'PIX00437':
    'RCR - L3 trigger threshold for rising RCR by reducing area',
    'PIX00438':
    'RCR - B0 background detector trigger threshold',
    'PIX00439':
    'RCR regime 0 pointer to state',
    'PIX00440':
    'RCR regime 1 pointer to state',
    'PIX00441':
    'RCR regime 2 pointer to state',
    'PIX00442':
    'RCR regime 3 pointer to state',
    'PIX00443':
    'RCR regime 4 pointer to state',
    'PIX00444':
    'RCR regime 5 pointer to state',
    'PIX00445':
    'RCR regime 6 pointer to state',
    'PIX00446':
    'RCR regime 7 pointer to state',
    'PIX00447':
    'Minimal duration of EACC TRIG accumulation',
    'PIX00448':
    'Maximal duration of EACC TRIG accumulation',
    'PIX00449':
    'Maximal counts in EACC TRIG accumulation',
    'PIX00450':
    'SumEmask',
    'PIX00451':
    'SumDmask',
    'PIX00452':
    'Flare selector period - units of 10 min',
    'PIX00453':
    'Flare selector latency - units of 10 min',
    'PIX00454':
    'Flare selector enabled flag',
    'PIX00455':
    'Flare selector start time - in SCET seconds',
    'PIX00456':
    'Flare selector end time - in SCET seconds',
    'PIX00457':
    'Image interval - detector mask',
    'PIX00458':
    'Imaging interval - trim N-parameter',
    'PIX00459':
    'Imaging interval - Ftrim fraction',
    'PIX00460':
    'Imaging interval - enable BCKG subtraction',
    'PIX00461':
    'Spectrogram - enable BCKG subtraction',
    'PIX00462':
    'Spectrogram - pixel mask',
    'PIX00463':
    'Spectrogram - detector mask',
    'PIX00479':
    'Number of detector',
    'PIX00480':
    'Detector ID',
    'PIX00481':
    'Pixel ID',
    'PIX00482':
    'E0-low',
    'PIX00483':
    'E1-low',
    'PIX00484':
    'E2-low',
    'PIX00485':
    'E3-low',
    'PIX00486':
    'E4-low',
    'PIX00487':
    'E5-low',
    'PIX00488':
    'E6-low',
    'PIX00489':
    'E7-low',
    'PIX00490':
    'E8-low',
    'PIX00491':
    'E9-low',
    'PIX00492':
    'E10-low',
    'PIX00493':
    'E11-low',
    'PIX00494':
    'E12-low',
    'PIX00495':
    'E13-low',
    'PIX00496':
    'E14-low',
    'PIX00497':
    'E15-low',
    'PIX00498':
    'E16-low',
    'PIX00499':
    'E17-low',
    'PIX00500':
    'E18-low',
    'PIX00501':
    'E19-low',
    'PIX00502':
    'E20-low',
    'PIX00503':
    'E21-low',
    'PIX00504':
    'E22-low',
    'PIX00505':
    'E23-low',
    'PIX00506':
    'E24-low',
    'PIX00507':
    'E25-low',
    'PIX00508':
    'E26-low',
    'PIX00509':
    'E27-low',
    'PIX00510':
    'E28-low',
    'PIX00511':
    'E29-low',
    'PIX00512':
    'E30-low',
    'PIX00513':
    'E31-low',
    'PIX00514':
    'E31-upper',
    'PIX00519':
    'Data compression level',
    'PIX00520':
    'QL integration time',
    'PIX00521':
    'BG - num of QL integr',
    'PIX00522':
    'BG - enrg bin upper edge',
    'PIX00523':
    'BG - enrg bin lower edge',
    'PIX00524':
    'BG - algorithm enabled',
    'PIX00525':
    'BG - TM gen enable',
    'PIX00526':
    'BG - default bckg rng 1',
    'PIX00527':
    'BG - default bckg rng 2',
    'PIX00528':
    'BG - default bckg rng 3',
    'PIX00529':
    'BG - default bckg rng 4',
    'PIX00530':
    'BG - default bckg rng 5',
    'PIX00531':
    'BG - default bckg rng 6',
    'PIX00532':
    'BG - default bckg rng 7',
    'PIX00533':
    'BG - default bckg rng 8',
    'PIX00534':
    'BG - count compr scheme',
    'PIX00535':
    'BG - trig compr scheme',
    'PIX00536':
    'LC - num of QL integr',
    'PIX00537':
    'LC - enrg bin upper edge',
    'PIX00538':
    'LC - enrg bin lower edge',
    'PIX00539':
    'LC - TM gen enabled',
    'PIX00540':
    'LC - detector mask',
    'PIX00541':
    'LC - pixel mask',
    'PIX00542':
    'LC - count compr scheme',
    'PIX00543':
    'LC - trig compr scheme',
    'PIX00544':
    'VAR - detector mask',
    'PIX00545':
    'VAR - energy mask',
    'PIX00546':
    'VAR - pixel mask',
    'PIX00547':
    'VAR - TM gen enabled',
    'PIX00548':
    'VAR - compr scheme',
    'PIX00549':
    'SP - num of QL integr',
    'PIX00550':
    'SP - TM gen enabled',
    'PIX00551':
    'SP - pixel mask',
    'PIX00552':
    'SP - detector mask',
    'PIX00553':
    'SP - count compr scheme',
    'PIX00554':
    'SP - trig compr scheme',
    'PIX00555':
    'DF - num of QL integr',
    'PIX00556':
    'DF - energu mask',
    'PIX00557':
    'DF - NBAD',
    'PIX00558':
    'DF - KBAD',
    'PIX00559':
    'DF - CBAD',
    'PIX00560':
    'DF - NREP',
    'PIX00561':
    'FD - num of QL integr',
    'PIX00562':
    'FD - detector mask',
    'PIX00563':
    'FD - pixel mask',
    'PIX00564':
    'FD - thermal energy mask',
    'PIX00565':
    'FD - nThermal energy mask',
    'PIX00566':
    'FD - TM gen enabled',
    'PIX00567':
    'FD - KB',
    'PIX00568':
    'FD - timescale 1 - RCR 0 count factor',
    'PIX00569':
    'FD - timescale 1 - RCR 1 count factor',
    'PIX00570':
    'FD - timescale 1 - RCR 2 count factor',
    'PIX00571':
    'FD - timescale 1 - RCR 3 count factor',
    'PIX00572':
    'FD - timescale 1 - RCR 4 count factor',
    'PIX00573':
    'FD - timescale 1 - RCR 5 count factor',
    'PIX00574':
    'FD - timescale 1 - RCR 6',
    'PIX00575':
    'FD - timescale 1 - RCR 7',
    'PIX00576':
    'FD - timescale 2 - RCR 0',
    'PIX00577':
    'FD - timescale 2 - RCR 1 count factor',
    'PIX00578':
    'FD - timescale 2 - RCR 2 count factor',
    'PIX00579':
    'FD - timescale 2 - RCR 3 count factor',
    'PIX00580':
    'FD - timescale 2 - RCR 4 count factor',
    'PIX00581':
    'FD - timescale 2 - RCR 5 count factor',
    'PIX00582':
    'FD - timescale 2 - RCR 6',
    'PIX00583':
    'FD - timescale 2 - RCR 7 count factor',
    'PIX00584':
    'FD - Cfmin variable',
    'PIX00585':
    'FD - Krel variable',
    'PIX00586':
    'FD - Krel prime variable',
    'PIX00587':
    'FD - Krel double prime variable',
    'PIX00588':
    'FD - timescale 1 history',
    'PIX00589':
    'FD - timescale 2 history',
    'PIX00590':
    'FD - initial T CBC',
    'PIX00591':
    'FD - initial nT CBC',
    'PIX00592':
    'FD - threshold for T B1',
    'PIX00593':
    'FD - threshold for T C1',
    'PIX00594':
    'FD - threshold for T M1',
    'PIX00595':
    'FD - threshold for T X1',
    'PIX00596':
    'FD - thld - weak nT fl',
    'PIX00597':
    'FD - thld - strong nT fl',
    'PIX00598':
    'FL - num of QL integr',
    'PIX00599':
    'FL - detector mask',
    'PIX00600':
    'FL - energy mask',
    'PIX00601':
    'FL - V1',
    'PIX00602':
    'FL - V2',
    'PIX00603':
    'FL - K',
    'PIX00604':
    'FL - K prime',
    'PIX00605':
    'FL - K double prime',
    'PIX00606':
    'FL - K triple prime',
    'PIX00607':
    'FL - K0',
    'PIX00608':
    'FL - K1',
    'PIX00609':
    'FL - K2',
    'PIX00610':
    'FL - Dx',
    'PIX00611':
    'FL - Dy',
    'PIX00623':
    'Flare Magnitude Index - Threshold',
    'PIX00669':
    'Science channel ID',
    'PIX00693':
    'Upper boundary mask',
    'PIX00694':
    'Lower boundary mask',
    'PIX00741':
    'Min time bin width',
    'PIX00765':
    'Minimum counts for 1 image',
    'PIX00789':
    'Minimum counts for more than 1 images',
    'PIX00813':
    'Default compression level',
    'PIX00814':
    'Use BCKG detector for formatting',
    'PIX00815':
    'Use CFL detector for formatting',
    'PIX00816':
    'L0 pixel mask',
    'PIX00817':
    'L0 detector mask',
    'PIX00818':
    'L1 RCR 0 pixel mask',
    'PIX00819':
    'L1 RCR 1 pixel mask',
    'PIX00820':
    'L1 RCR 2 pixel mask',
    'PIX00821':
    'L1 RCR 3 pixel mask',
    'PIX00822':
    'L1 RCR 4 pixel mask',
    'PIX00823':
    'L1 RCR 5 pixel mask',
    'PIX00824':
    'L1 RCR 6 pixel mask',
    'PIX00825':
    'L1 RCR 7 pixel mask',
    'PIX00826':
    'L1 detector mask',
    'PIX00827':
    'L2 RCR 0, P1, pixel mask',
    'PIX00828':
    'L2 RCR 0, P2, pixel mask',
    'PIX00829':
    'L2 RCR 0, P3, pixel mask',
    'PIX00830':
    'L2 RCR 0, P4, pixel mask',
    'PIX00831':
    'L2 RCR 0, P5, pixel mask',
    'PIX00832':
    'L2 RCR 1, P1, pixel mask',
    'PIX00833':
    'L2 RCR 1, P2, pixel mask',
    'PIX00834':
    'L2 RCR 1, P3, pixel mask',
    'PIX00835':
    'L2 RCR 1, P4, pixel mask',
    'PIX00836':
    'L2 RCR 1, P5, pixel mask',
    'PIX00837':
    'L2 RCR 2, P1, pixel mask',
    'PIX00838':
    'L2 RCR 2, P2, pixel mask',
    'PIX00839':
    'L2 RCR 2, P3, pixel mask',
    'PIX00840':
    'L2 RCR 2, P4, pixel mask',
    'PIX00841':
    'L2 RCR 2, P5, pixel mask',
    'PIX00842':
    'L2 RCR 3, P1, pixel mask',
    'PIX00843':
    'L2 RCR 3, P2, pixel mask',
    'PIX00844':
    'L2 RCR 3, P3, pixel mask',
    'PIX00845':
    'L2 RCR 3, P4, pixel mask',
    'PIX00846':
    'L2 RCR 3, P5, pixel mask',
    'PIX00847':
    'L2 RCR 4, P1, pixel mask',
    'PIX00848':
    'L2 RCR 4, P2, pixel mask',
    'PIX00849':
    'L2 RCR 4, P3, pixel mask',
    'PIX00850':
    'L2 RCR 4, P4, pixel mask',
    'PIX00851':
    'L2 RCR 4, P5, pixel mask',
    'PIX00852':
    'L2 RCR 5, P1, pixel mask',
    'PIX00853':
    'L2 RCR 5, P2, pixel mask',
    'PIX00854':
    'L2 RCR 5, P3, pixel mask',
    'PIX00855':
    'L2 RCR 5, P4, pixel mask',
    'PIX00856':
    'L2 RCR 5, P5, pixel mask',
    'PIX00857':
    'L2 RCR 6, P1, pixel mask',
    'PIX00858':
    'L2 RCR 6, P2, pixel mask',
    'PIX00859':
    'L2 RCR 6, P3, pixel mask',
    'PIX00860':
    'L2 RCR 6, P4, pixel mask',
    'PIX00861':
    'L2 RCR 6, P5, pixel mask',
    'PIX00862':
    'L2 RCR 7, P1, pixel mask',
    'PIX00863':
    'L2 RCR 7, P2, pixel mask',
    'PIX00864':
    'L2 RCR 7, P3, pixel mask',
    'PIX00865':
    'L2 RCR 7, P4, pixel mask',
    'PIX00866':
    'L2 RCR 7, P5, pixel mask',
    'PIX00867':
    'L2 detector mask',
    'PIX00868':
    'L3 RCR 0, P1, pixel mask',
    'PIX00869':
    'L3 RCR 0, P2, pixel mask',
    'PIX00870':
    'L3 RCR 0, P3, pixel mask',
    'PIX00871':
    'L3 RCR 0, P4, pixel mask',
    'PIX00872':
    'L3 RCR 0, P5, pixel mask',
    'PIX00873':
    'L3 RCR 1, P1, pixel mask',
    'PIX00874':
    'L3 RCR 1, P2, pixel mask',
    'PIX00875':
    'L3 RCR 1, P3, pixel mask',
    'PIX00876':
    'L3 RCR 1, P4, pixel mask',
    'PIX00877':
    'L3 RCR 1, P5, pixel mask',
    'PIX00878':
    'L3 RCR 2, P1, pixel mask',
    'PIX00879':
    'L3 RCR 2, P2, pixel mask',
    'PIX00880':
    'L3 RCR 2, P3, pixel mask',
    'PIX00881':
    'L3 RCR 2, P4, pixel mask',
    'PIX00882':
    'L3 RCR 2, P5, pixel mask',
    'PIX00883':
    'L3 RCR 3, P1, pixel mask',
    'PIX00884':
    'L3 RCR 3, P2, pixel mask',
    'PIX00885':
    'L3 RCR 3, P3, pixel mask',
    'PIX00886':
    'L3 RCR 3, P4, pixel mask',
    'PIX00887':
    'L3 RCR 3, P5, pixel mask',
    'PIX00888':
    'L3 RCR 4, P1, pixel mask',
    'PIX00889':
    'L3 RCR 4, P2, pixel mask',
    'PIX00890':
    'L3 RCR 4, P3, pixel mask',
    'PIX00891':
    'L3 RCR 4, P4, pixel mask',
    'PIX00892':
    'L3 RCR 4, P5, pixel mask',
    'PIX00893':
    'L3 RCR 5, P1, pixel mask',
    'PIX00894':
    'L3 RCR 5, P2, pixel mask',
    'PIX00895':
    'L3 RCR 5, P3, pixel mask',
    'PIX00896':
    'L3 RCR 5, P4, pixel mask',
    'PIX00897':
    'L3 RCR 5, P5, pixel mask',
    'PIX00898':
    'L3 RCR 6, P1, pixel mask',
    'PIX00899':
    'L3 RCR 6, P2, pixel mask',
    'PIX00900':
    'L3 RCR 6, P3, pixel mask',
    'PIX00901':
    'L3 RCR 6, P4, pixel mask',
    'PIX00902':
    'L3 RCR 6, P5, pixel mask',
    'PIX00903':
    'L3 RCR 7, P1, pixel mask',
    'PIX00904':
    'L3 RCR 7, P2, pixel mask',
    'PIX00905':
    'L3 RCR 7, P3, pixel mask',
    'PIX00906':
    'L3 RCR 7, P4, pixel mask',
    'PIX00907':
    'L3 RCR 7, P5, pixel mask',
    'PIX00908':
    'L3 detector mask',
    'PIX00909':
    'L1, L2 count compression scheme',
    'PIX00910':
    'L1,L2,L3 trigger compression scheme',
    'PIX00911':
    'Spectrogram compression scheme',
    'PIX00912':
    'L3 visibility compression scheme',
    'PIX00913':
    'Calibration compression scheme',
    'PIX00914':
    'Variance compression scheme',
    'PIX00915':
    'Light curve counts compression scheme',
    'PIX00916':
    'QL spectrum counts compression scheme',
    'PIX00917':
    'BG monitor counts compression scheme',
    'PIX00918':
    'Common QL Trigger accumulator compression scheme',
    'PIX00919':
    'SP - Wait Cycles',
    'PIX00920':
    'Filesystem check - Bad block handling',
    'The auto':
    None,
    'This rep':
    None,
    'YIX54001':
    'Telecommand acceptance report - success',
    'YIX54002':
    'Illegal APID',
    'YIX54003':
    'Incomplete or invalid length',
    'YIX54004':
    'Incorrect checksum (CRC)',
    'YIX54005':
    'Illegal packet type',
    'YIX54006':
    'Illegal packet subtype',
    'YIX54007':
    'Illegal or inconsistent application data field',
    'YIX54008':
    'Illegal segment sequence flag',
    'YIX54009':
    'Illegal packet length with respect to type/subtype',
    'YIX54010':
    'Illegal CCSDS secondary header flag in TC Data Field Header',
    'YIX54012':
    'Illegal Ack value in TC Data Field Header',
    'YIX54013':
    'Telecommand execution completed report - success',
    'YIX54015':
    'Invalid operation mode transition requested',
    'YIX54016':
    'Accessing invalid MID',
    'YIX54017':
    'Attempting to write to protected memory, EEPROM',
    'YIX54019':
    'TC(237,19) failed to get paramete',
    'YIX54020':
    'FLASH memory write failed',
    'YIX54021':
    'Memory load operation failed due to invalid packet length '
    'propagated to MemLoad module after dynamic verification '
    'succeeded',
    'YIX54022':
    'Telecommanded SW reset failed - Application SW still running '
    'even if watchdog is no more being reloaded - watchdog is '
    'disabled or broken',
    'YIX54024':
    'List of user data selections is full',
    'YIX54026':
    'Disable Application Software Auto-start in TC(236,11) cannot be '
    'performed (boot failed or not called in 30s after boot report).',
    'YIX54028':
    'Invalid HK data report period in TC(3,129) (no parameters '
    'transmitted)',
    'YIX54029':
    'Memory load not enabled',
    'YIX54032':
    'Wrong dynamic length of received TC',
    'YIX54033':
    'Packet rejected due to full TC buffer (all subsequent packets '
    'were rejected until packet was acknowledged by TM(1,1)',
    'YIX54034':
    'Wrong current operation mode',
    'YIX54035':
    'System ID out of bounds when powering ON/OFF',
    'YIX54036':
    'Subsytem ID out of bounds when powering ON/OFF',
    'YIX54037':
    'Wrong systemID, subsytemID pair when configuring subsystems',
    'YIX54038':
    'Wrong configuration parameter',
    'YIX54040':
    'Requested operation failed',
    'YIX54041':
    'Formatting of calibration accumulators failed',
    'YIX54043':
    'Detector/pixel/ AD channel out of bounds',
    'YIX54044':
    'Subspectrum definition exceeds maximum number of calibration '
    'accumulators',
    'YIX54045':
    'ASIC Reset failed',
    'YIX54046':
    'Read ASIC temperature procedure failed',
    'YIX54047':
    'Setting ASIC latency failed',
    'YIX54048':
    'On demand ASIC ADC readout failed',
    'YIX54049':
    'ASIC baseline determination failed',
    'YIX54050':
    'ASIC dark channel determination failed',
    'YIX54051':
    'Threshold scan failed',
    'YIX54052':
    'ASIC ADC reading failed',
    'YIX54053':
    'Start of test pulse generation failed',
    'YIX54054':
    'Reading ASIC registers failed',
    'YIX54055':
    'Writing ASIC registers failed',
    'YIX54056':
    'Telecommanded self-tests failed',
    'YIX54058':
    'Detectors quadrant cannot be manipulated because LV is not '
    'powered on.',
    'YIX54059':
    'Attenuator cannot be manipulated because LV is not powered on',
    'YIX54060':
    'HV cannot be manipulated because LV is not powered on.',
    'YIX54061':
    'Configuration not executed, because attenuator execution is in '
    'progress.',
    'YIX54062':
    'Powered quarters do not correspond to quarters containing '
    'detectors or groups requested to be used',
    'YIX54063':
    'Enabled groups do not correspond to groups (containing '
    'detectors) requested to be used',
    'YIX54064':
    'Test/debug procedure cannot be executed due to already running '
    'different test procedure.',
    'YIX54065':
    'Illegal segment sequence flag',
    'YIX54066':
    'Failed to enable/disable file transfer to SSMM of service TC21',
    'YIX54067':
    'Failed to reset output data buffers, TC(21,128)',
    'YIX54068':
    'Failed to send context to on-board context management',
    'YIX54069':
    'Failed to process context from on-board context management',
    'YIX54070':
    'Failed to process TC(237,11) data compression scheme parameters',
    'YIX54071':
    'No data corresponding to the selection found.',
    'YIX54072':
    'LUT type out of bounds for TC(237,8)',
    'YIX54073':
    'LUT type out of bounds for TC(237,7)',
    'YIX54074':
    'Applying ELUT to FPGA failed',
    'YIX54075':
    'Wrong configuration selected for automatic transition to NOMINAL '
    'operation mode',
    'YIX54077':
    'TC(237,1) failed to set parameter',
    'YIX54078':
    'TC(237,2) invalid parameter sub-id',
    'YIX54079':
    'TC(237,2) failed to get parameter',
    'YIX54080':
    'TC service 3, invalid SID',
    'YIX54081':
    'TC236_7 - Enable FDIR failed',
    'YIX54082':
    'TC236_8 - Disable FDIR failed',
    'YIX54083':
    'TC236_10 - FDIR configuration failed due to wrong FDIR ID and/or '
    'FDIR parameter ID',
    'YIX54084':
    'TC 236_10 - FDIR configuration parameter is out of bounds',
    'YIX54085':
    'Memory operation failed',
    'YIX54086':
    'Memory operation interrupted',
    'YIX54087':
    'Timecode not received within 2s after TC(9,129)',
    'YIX54088':
    'Telecommand to load ASW image from FLASH to RAM failed',
    'YIX54089':
    'Telecommand to save ASW image from RAM to FLASH failed',
    'YIX54090':
    'Too long opration',
    'YIX54091':
    'TC(236,18) failed due to wrong FDIR mask or parameter type',
    'YIX54092':
    'Memory reading failed (valid for TC(6,5) and TC(6,9))',
    'YIX54093':
    'HW selftest cannot be executed, selftest already running',
    'YIX54094':
    'Memory selftest cannot be executed due to incorrect address '
    'range or addresses not aligned to 4B',
    'YIX54095':
    'Telecommand to execute ASW image from RAM failed',
    'YIX54096':
    'TC(236,3), TC(236,14) or TC(236,17) could not be executed, '
    'either autostart in progress or other operation is being '
    'executed',
    'YIX54097':
    'Attenuator control loop timeout',
    'YIX54098':
    'TC(238,1) faild, list of user selection request is full',
    'YIX54099':
    'TC(238,6) perform filesystem check failed',
    'YIX54100':
    'TC(237,8) storing LUT in filesystem failed',
    'YIX54101':
    'Regular housekeeping telemetry reports SID 1',
    'YIX54102':
    'Regular housekeeping telemetry reports SID 2',
    'YIX54103':
    'Heartbeat TM(3,25) - SID=4',
    'YIX54104':
    'TC(237,8) saving LUT Ids in ParamMgmt as current id failed',
    'YIX54105':
    'TC(237,10) updating RCR parameters failed',
    'YIX54106':
    'Incorrect detector ID or register mask',
    'YIX54107':
    'TC(237,18) failed to set parameter',
    'YIX54108':
    'TC(237,19) invalid parameter sub-id',
    'YIX54110':
    'X-ray L0 auto',
    'YIX54111':
    'X-ray L1 auto',
    'YIX54112':
    'X-ray L2 auto',
    'YIX54113':
    'X-ray L3 auto',
    'YIX54114':
    'X-ray L0 user',
    'YIX54115':
    'X-ray L1 user',
    'YIX54116':
    'X-ray L2 user',
    'YIX54117':
    'X-ray L3 user',
    'YIX54118':
    'QL summed light curves',
    'YIX54119':
    'QL background monitor',
    'YIX54120':
    'QL detector specific spectra',
    'YIX54121':
    'Variance',
    'YIX54122':
    'Flare flag and location',
    'YIX54124':
    'Background spectrum for calibration',
    'YIX54125':
    'Aspect',
    'YIX54126':
    'User data selections report',
    'YIX54127':
    'Filesystem check report',
    'YIX54128':
    'SuSW Parameter report TM',
    'YIX54129':
    'STIX ASW Parameter report',
    'YIX54130':
    'Report threshold scan',
    'YIX54131':
    'Report ASIC temperature',
    'YIX54132':
    'Report on-demand ASIC ADC readout',
    'YIX54133':
    'Report ASIC baseline',
    'YIX54134':
    'Report channel dark current',
    'YIX54135':
    'Report ASIC ADC read',
    'YIX54137':
    'Report ASIC register read',
    'YIX54138':
    'Report stored attenuator data',
    'YIX54140':
    'Subsys config rep',
    'YIX54141':
    'STIX FDIR parameter reported',
    'YIX54142':
    'Spectrogram auto',
    'YIX54143':
    'Spectrogram user',
    'YIX54144':
    'TM mgmt status and flare list',
    'YIX54239':
    'Context file(s) not found',
    'YIX54240':
    'QL detector failure identification',
    'YIX54241':
    'Wrong correlation between attenuator position sensor and motor '
    'movement',
    'YIX54242':
    'FSW received AhbRx callback from BSW drivers. This callback is '
    'invoked when error(s) on the AMBA AHB (bus). To clear the error '
    'condition, the SpaceWire interface should be restarted',
    'YIX54243':
    'In case of RamUtils_initSDRAM fails due to timeout, this event '
    'is sent along the TM(5,3)',
    'YIX54244':
    'In case there was reboot due to watchdog and/or due to SW going '
    'to trap from NOMINAL operation mode, STIX requests that after '
    'ASW is booted (and initialised) the S/C executes an on-board '
    'control procedure to switch STIX again into NOMINAL operation '
    'mode.',
    'YIX54245':
    'SRAM memory check failed for the first time in a row, requiring '
    'reboot according to STIX-FDIR-REQ 010',
    'YIX54246':
    'Internal spacewire failure or link error flagged by the driver',
    'YIX54248':
    'Packet CCSDS header did not conform to required values',
    'YIX54249':
    'Received packet was too long, exceeding 252B',
    'YIX54250':
    'Received packet was too short, it did not have necessary length '
    '(16B) to contain CCSDS header (4B), TC Source packet header '
    '(6B), data field header (4B) and CRC (2B)',
    'YIX54251':
    'Packet rejected due to corruption of packet indicated by SpW',
    'YIX54252':
    'Failed to execute predefined autonomous selftest using state '
    'machine after boot report was sent.',
    'YIX54253':
    'SpW communication restored',
    'YIX54255':
    'Acknowledge of successful correction of content of ASIC '
    'registers by FDIR task',
    'YIX54256':
    'Start up SW booted successfully and STIX is ready to receive '
    'telecommands',
    'YIX54257':
    'Application SW booted and STIX is ready to receive telecommands',
    'YIX54258':
    'Reported after any mode transition, both autonomous and '
    'telecommanded',
    'YIX54259':
    'Application SW starting. The STIX instrument is during '
    'Application SW start not receiving TCs',
    'YIX54260':
    'Telecommanded Instrument memory test and hardware operability '
    'test started.',
    'YIX54261':
    'Telecommanded Instrument memory test and hardware operability '
    'test succeeded.',
    'YIX54262':
    'Telecommanded Instrument memory test and hardware operability '
    'test started.',
    'YIX54263':
    'Telecommanded Instrument memory test and hardware operability '
    'test succeeded.',
    'YIX54264':
    'Event message that CPU is not overloaded anymore',
    'YIX54265':
    'Attenuator operation restored after suspension due to too '
    'frequent usage',
    'YIX54266':
    'High voltage power supply unit recovered from failure',
    'YIX54267':
    'Successful recovery of SEU in front end quarter',
    'YIX54268':
    'Spacewire time code reception restored after a period when it '
    'was missing',
    'YIX54270':
    'LUT not found',
    'YIX54271':
    'Inconsistent page address before and after FLASH  filesystem '
    'operation',
    'YIX54272':
    'Too many IRQs detected or spurious IRQs detected',
    'YIX54276':
    'EDAC algorithm for modification of scrubbing rate report',
    'YIX54277':
    'STIX Info - HV depolarisation status changed',
    'YIX54278':
    'CPU overload condition detected warning report',
    'YIX54279':
    'Attenuator cannot be moved because request for attenuator motion '
    'is too frequent',
    'YIX54280':
    'X-ray detector provided signalling of single-event upset (SEU is '
    'detected internally in appropriate quarter)',
    'YIX54281':
    'Filesystem initialisation finished',
    'YIX54282':
    'No reception of Spacewire time code for a given period of time',
    'YIX54285':
    'Periodic ASIC register verification procedure found mismatch',
    'YIX54286':
    'Start up SW booted successfully, but some tests of boot up '
    'self-test failed.',
    'YIX54287':
    'Application SW booted and STIX is ready to receive telecommands',
    'YIX54288':
    'Reported in case of invalid or rejected mode transition',
    'YIX54289':
    'Telecommanded Instrument memory test and hardware operability '
    'test failed.',
    'YIX54290':
    'Telecommanded Instrument memory test and hardware operability '
    'test failed.',
    'YIX54291':
    'Too many IRQs detected or spurious IRQs detected',
    'YIX54293':
    'Filesystem CRC error',
    'YIX54295':
    'Watchdog either did not reboot when warm reset was initiated, or '
    'refresh timer does not change',
    'YIX54299':
    'Autonomous warm reset initiated as recovery from the STIX '
    'failure',
    'YIX54300':
    'Repeated problem while booting ASW image, first problem is '
    'responded by TM(5,2) 0x4001. Afterwards, ASW image MID is moved '
    'in order of A1, B1, A2, B2.',
    'YIX54301':
    'Failure of attenuator motor detected',
    'YIX54302':
    'One or more detectors provide extremely high rate of X-ray '
    'events based on noisy pixel detection algorithm',
    'YIX54303':
    'Overcurrent detected for one or more detector quadrants. The '
    'quadrants with overcurrent are powered off. The limits for the '
    'overcurrent depend on number of quarters that are enabled',
    'YIX54304':
    'Critical temperature detected for detector quadrant. Detectors '
    'not powered (switched OFF), instrument is not in nominal '
    'operation (the affected detectors quadrant is not available for '
    'X-ray data acquisition). STIX to SAFE',
    'YIX54305':
    'Failure of the high voltage power supply unit. This is based on '
    'the voltage measurement and exceeding HV PSU FDIR limits. After '
    'issuing this report, STIX would transition to SAFE mode',
    'YIX54306':
    'X-ray detector provided signalling of single-event upset (SEU is '
    'detected internally by Caliste) Continue normal operation '
    '(SRS-ASW-050)',
    'YIX54307':
    'Failure of HK monitored line because monitored voltage, current '
    'or temperature is out of HW limits',
    'YIX54309':
    'HK parameter values are invalid. The HK failure is detected by '
    'checking "ADC Self-check Value 1.5V" and "REF_2V5_V - ADC '
    'Self-check Value 2.5V". STIX to SAFE. Failure is determined '
    'using BSW function HK_selfTest()',
    'YIX54310':
    'If an overcurrent on a non-switchable voltage line is detected '
    'immediate power down is issued. Power up is possible only after '
    'ground intervention',
    'YIX54312':
    'Either autonomous execution of ASW image or TC for ASW image '
    'load/save/execute failed',
    'YIX54313':
    'Monitoring TM informing that FDIR protection was enabled. As per '
    'STIX-FDIR-REQ 015',
    'YIX54314':
    'Service 20 not received for 30s, preparing for shutdown',
    'YIX54315':
    'SW failure of HK monitored line',
    'YIX54316':
    'SDRAM memory failure during StartASW procedure',
    'YIX54317':
    'Case of both PSUs on, therefore both IDPU "on". The FSW shall '
    'enter SAFE mode, or stay in BOOT, followed by generation of this '
    'event report',
    'YIX54318':
    'Function \'RamUtils_initSDRAM" generated timeout',
    'YIX54319':
    'Calling function \'Flash_reset" generated error',
    'YIX54320':
    'Memory Dump Report MAIN:EEPROM',
    'YIX54321':
    'Memory Dump Report MAIN:SRAM',
    'YIX54322':
    'Memory Dump Report MAIN:SDRAM',
    'YIX54323':
    'Memory Dump Report MAIN:Flash A',
    'YIX54324':
    'Memory Dump Report MAIN:Flash B',
    'YIX54325':
    'Memory Dump Report MAIN:ASW image A1',
    'YIX54326':
    'Memory Dump Report MAIN:ASW image A2',
    'YIX54327':
    'Memory Dump Report MAIN:ASW image B1',
    'YIX54328':
    'Memory Dump Report MAIN:ASW image B2',
    'YIX54329':
    'Memory Check Report',
    'YIX54330':
    'Connection Test Report',
    'YIX54331':
    'Context Report from User',
    'YIX54333':
    'EEPROM',
    'YIX54334':
    'SRAM',
    'YIX54335':
    'SDRAM',
    'YIX54336':
    'FLASH A',
    'YIX54337':
    'FLASH B',
    'YIX54338':
    'ASW image A1',
    'YIX54339':
    'ASW image A2',
    'YIX54340':
    'ASW image B1',
    'YIX54341':
    'ASW image B2',
    'YIX54342':
    'Masked detectors for given registers were not corrected by ASI '
    'verification period and registers are still mismatched',
    'YIX54343':
    'LUT upload failed for TC(237,7)',
    'YIX54344':
    'Autonomous application of LUT failed',
    'YIX54346':
    'TC(237,9) updating QL parameters failed',
    'YIX54356':
    'Running test procedure was interrupted',
    'YIX54358':
    'STIX Warning - Async memory operation interrupted',
    'YIX54361':
    'Rotating Buffer is being zeroed after EDAC was turned on',
    'YIX54362':
    'Rotating Buffer has been zeroed and EDAC is ready',
    'YIX54929':
    'SDRAM initialisation pattern memory test  faile',
    'ZIX03005':
    'Enable HK parameter report generation',
    'ZIX03006':
    'Disable HK parameter report generation',
    'ZIX03129':
    'Update HK Report Generation Period',
    'ZIX06005':
    'Dump Memory',
    'ZIX06009':
    'Check Memory',
    'ZIX0602A':
    'Load Memory',
    'ZIX0602B':
    'Load Memory',
    'ZIX09129':
    'Accept Time Synchronisation',
    'ZIX17001':
    'Perform Connection Test',
    'ZIX20128':
    'Information Distribution to User (STIX)',
    'ZIX21001':
    'Enable Science Data Transfer to SSMM',
    'ZIX21002':
    'Disable Science Data Transfer to SSMM',
    'ZIX21128':
    'Reset Science Data Output Buffer',
    'ZIX22001':
    'Request User to Report Context',
    'ZIX22003':
    'Accept Context',
    'ZIX36001':
    'STIX Mode transition',
    'ZIX36002':
    'STIX Instrument warm reset',
    'ZIX36003':
    'Load Application SW image to RAM',
    'ZIX36004':
    'Power ON a STIX subsystem',
    'ZIX36005':
    'Power OFF a STIX subsystem',
    'ZIX36007':
    'Enable FDIR function',
    'ZIX36008':
    'Disable FDIR function',
    'ZIX36009':
    'Configure FDIR function',
    'ZIX36010':
    'Configure FDIR function',
    'ZIX36011':
    'Disable Application Software Auto-start',
    'ZIX36012':
    'Enable Memory Load',
    'ZIX36013':
    'Disable Memory Load',
    'ZIX36014':
    'Execute ASW image from SDRAM',
    'ZIX36015':
    'Read STIX subsystem configuration',
    'ZIX36017':
    'Save Application SW image from RAM to FLASH',
    'ZIX36018':
    'Read STIX subsystem configuration',
    'ZIX36020':
    'Request RAM pattern memory test',
    'ZIX36601':
    'Subsystem config-IDPU',
    'ZIX36602':
    'Subsystem config-Dets',
    'ZIX36603':
    'Subsystem config-Aspect',
    'ZIX36604':
    'Subsystem config-Atten.',
    'ZIX36605':
    'Subsystem config-PSU',
    'ZIX36606':
    'Subsystem config-SuSW',
    'ZIX36607':
    'Subsystem config-ASW',
    'ZIX36608':
    'Subsystem config-Su+A',
    'ZIX37001':
    'Load SuSW parameter',
    'ZIX37002':
    'Report SuSW parameter',
    'ZIX37003':
    'Initiate reset and restart calibration accumulation',
    'ZIX37004':
    'Enable/disable formatting of calibration accumulation',
    'ZIX37005':
    'Truncate calibration accumulation',
    'ZIX37006':
    'Enable/disable continuous accumulation',
    'ZIX37008':
    'Apply LUT',
    'ZIX37009':
    'Update QL parameters',
    'ZIX37010':
    'Update RCR parameters',
    'ZIX37011':
    'Update data compression parameters',
    'ZIX37013':
    'Flare processing parameters',
    'ZIX37014':
    'Configure TM publishing interval',
    'ZIX37015':
    'Set new value of PALD counter',
    'ZIX37016':
    'Configure TM corridor upper limit',
    'ZIX37017':
    'Override publishing of flare data',
    'ZIX37018':
    'STIX Load ASW parameter',
    'ZIX37019':
    'STIX Report ASW parameter',
    'ZIX37701':
    'Detector/pixel upper temperature correction to AD',
    'ZIX37702':
    'Detector/pixel lower temperature correction to AD',
    'ZIX37703':
    'Energy channel boundaries',
    'ZIX37704':
    'Flare location determination table',
    'ZIX37705':
    'Division between thermal and non-thermal ene',
    'ZIX37706':
    'Thermal energy bins for image interval determinations',
    'ZIX37707':
    'Non Thermal energy bins for image interval determinations',
    'ZIX37708':
    'Thermal Flare Mag Index',
    'ZIX37709':
    'non Thermal Flare Mag Index',
    'ZIX37710':
    'Minimum thermal integration time for image interval det',
    'ZIX37711':
    'Minimum non thermal integration time for image interval det',
    'ZIX37712':
    'Minimum thermal counts for an image for image int det',
    'ZIX37713':
    'Minimum non thermal counts for an image for image int det',
    'ZIX37714':
    'Minimum thermal counts for more images for image int det',
    'ZIX37715':
    'Minimum non thermal counts for more images for image int det',
    'ZIX37716':
    'Total Flare Mag Index',
    'ZIX37717':
    'Thermal Energy bins for Spectrogram determination',
    'ZIX37718':
    'Non-thermal Energy bins for Spectrogram determination',
    'ZIX37719':
    'Minimum thermal integration time for image interval det',
    'ZIX37720':
    'Minimum thermal integration time for image interval det',
    'ZIX37721':
    'Minimum non thermal counts for an image for Spectrogram',
    'ZIX37722':
    'Minimum non thermal counts for an image for Spectrogram',
    'ZIX37723':
    'Minimum thermal counts for more images for Spectrogram',
    'ZIX37724':
    'Minimum thermal counts for more images for Spectrogram',
    'ZIX38001':
    'Select data for download',
    'ZIX38002':
    'Report of the unprocessed data data selections',
    'ZIX38004':
    'Clear the list of user data selections',
    'ZIX38005':
    'Free data in the archive memory',
    'ZIX38006':
    'Perform filesystem check',
    'ZIX38008':
    'Request list of X ray data chunks',
    'ZIX38010':
    'Request Aspect burst data',
    'ZIX39001':
    'Reset ASIC',
    'ZIX39002':
    'Read ASIC temperature',
    'ZIX39004':
    'Set ASIC latency delay',
    'ZIX39005':
    'Execute on-demand ASIC ADC readout',
    'ZIX39007':
    'Determine ASIC baseline',
    'ZIX39009':
    'Determine channel dark current',
    'ZIX39011':
    'Perform threshold scan',
    'ZIX39013':
    'Perform ASIC ADC read',
    'ZIX39015':
    'Generate test pulses',
    'ZIX39017':
    'Perform ASIC register read',
    'ZIX39019':
    'Perform ASIC register write',
    'ZIX39020':
    'Download stored data from attenuator'
}
SPID_DESC = {
    54001: 'STIX TC ACC SUCCESS',
    54002: 'STIX TC ACC FLR - Illegal APID',
    54003: 'STIX TC ACC FLR - Incomplete or invalid length',
    54004: 'STIX TC ACC FLR - Incorrect checksum (CRC)',
    54005: 'STIX TC ACC FLR - Illegal packet type',
    54006: 'STIX TC ACC FLR - Illegal packet subtype',
    54007: 'STIX TC ACC FLR - Illegal or inconsistent application data fie',
    54008: 'STIX TC ACC FLR - Illegal segmented sequence flag',
    54009: 'STIX TC ACC FLR - Illegal packet length wrt type/subtype',
    54010: 'STIX TC ACC FLR - Illegal source/packet data header const',
    54012: 'STIX TC ACC FLR - Illegal ACK value in TC DFH',
    54013: 'STIX TC EXEC SUCCESS',
    54015: 'TBC STIX TC EXEC FLR - Invalid operation mode transition req',
    54016: 'STIX TC EXEC FLR - Accessing invalid MID',
    54017: 'STIX TC EXEC FLR - Writing to protected memory, EEPROM',
    54019: 'STIX TC EXEC FLR - Invalid start addr or length TC(6-2,5or9)',
    54020: 'STIX TC EXEC FLR - FLASH memory write failed',
    54021: 'STIX TC EXEC FLR - Memory load operation failed - inv pack len',
    54022: 'TBC STIX TC EXEC FLR - TC SW reset failed - ASW still running',
    54024: 'TBC STIX TC EXEC FLR - List of user data selections is full',
    54026: 'STIX TC EXEC FLR - Disable ASW Auto-start cannot be performed',
    54028: 'STIX TC EXEC FLR - Invalid HK data report period in TC(3,129)',
    54029: 'STIX TC EXEC FLR - Memory load not enabled',
    54032: 'STIX TC EXEC FLR - Wrong dynamic length of received TC',
    54033: 'STIX TC EXEC FLR - Packet rejected due to full TC buffer',
    54034: 'STIX TC EXEC FLR - Wrong current operation mode',
    54035: 'STIX TC EXEC FLR - System ID OOB when powering ON/OFF',
    54036: 'STIX TC EXEC FLR - Subsystem ID OOB when powering ON/OFF',
    54037: 'STIX TC EXEC FLR - Wrong systemID / subsytemID pair when conf',
    54038: 'STIX TC EXEC FLR - Wrong configuration parameter',
    54040: 'STIX TC EXEC FLR - Requested operation failed',
    54041: 'STIX TC EXEC FLR - Formatting of calibration accus failed',
    54043: 'STIX TC EXEC FLR - Detector/pixel/ AD channel OOB',
    54044: 'STIX TC EXEC FLR - Subspectrum def exc max num of calib acc',
    54045: 'STIX TC EXEC FLR - ASIC Reset failed',
    54046: 'STIX TC EXEC FLR - Read ASIC temperature procedure failed',
    54047: 'STIX TC EXEC FLR - Setting ASIC latency failed',
    54048: 'STIX TC EXEC FLR - On demand ASIC ADC readout failed',
    54049: 'STIX TC EXEC FLR - ASIC baseline determination failed',
    54050: 'STIX TC EXEC FLR - ASIC dark channel determination failed',
    54051: 'STIX TC EXEC FLR - Threshold scan failed',
    54052: 'STIX TC EXEC FLR - ASIC ADC reading failed',
    54053: 'STIX TC EXEC FLR - Start of test pulse generation failed',
    54054: 'STIX TC EXEC FLR - Reading ASIC registers failed',
    54055: 'STIX TC EXEC FLR - Writing ASIC registers failed',
    54056: 'STIX TC EXEC FLR - Telecommanded self-tests failed',
    54058: 'STIX TC EXEC FLR - Det Q: LV is not powered on',
    54059: 'STIX TC EXEC FLR - Attenuator: LV is not powered on',
    54060: 'STIX TC EXEC FLR - HV: LV is not powered on',
    54061: 'STIX TC EXEC FLR - No config: Attenuator execution in progress',
    54062: 'STIX TC EXEC FLR - Requested quarters (Det or Grp) not powered',
    54063: 'STIX TC EXEC FLR - Requested quarters (Det or Grp) not enabled',
    54064: 'STIX TC EXEC FLR - Already running different test procedure',
    54065: 'STIX TC ACC FLR - Illegal segment sequence flag',
    54066: 'STIX TC EXEC FLR - En/dis file transfer to SSMM - TC21',
    54067: 'STIX TC EXEC FLR - Reset output data buffers - TC(21,128)',
    54068: 'STIX TC EXEC FLR - Send context to on-board context mgmt',
    54069: 'STIX TC EXEC FLR - Process context from on-board context mgmt',
    54070: 'STIX TC EXEC FLR - Process TC(237,11) data compression scheme',
    54071: 'STIX TC EXEC FLR - Invalid time or energy interval selected',
    54072: 'STIX TC EXEC FLR - LUT type OOB for TC(237,8)',
    54073: 'STIX TC EXEC FLR - LUT type OOB for TC(237,7)',
    54074: 'STIX TC EXEC FLR - Applying ELUT to FPGA failed',
    54075: 'STIX TC EXEC FLR - Wrong conf for auto transition to NOMINAL',
    54077: 'STIX TC EXEC FLR - TC(237,1) failed to set parameter',
    54078: 'STIX TC EXEC FLR - TC(237,2) invalid parameter sub-id',
    54079: 'STIX TC EXEC FLR - TC(237,2) failed to get parameter',
    54080: 'STIX TC EXEC FLR - TC Service 3 - invalid SID',
    54081: 'STIX TC EXEC FLR - TC(236,7) - Enable FDIR failed',
    54082: 'STIX TC EXEC FLR - TC(236,8) - Disable FDIR failed',
    54083: 'STIX TC EXEC FLR - TC(236,10) - FDIR conf failed - wrong ID',
    54084: 'STIX TC EXEC FLR - TC(236,10) FDIR conf param is OOB',
    54085: 'STIX TC EXEC FLR - Memory operation failed',
    54086: 'STIX TC EXEC FLR - Time sync, TC(9,129), already in progress',
    54087: 'STIX TC EXEC FLR - No Timecode within 2s after TC(9,129)',
    54088: 'STIX TC EXEC FLR - TC to load ASW img fr FLASH to RAM failed',
    54089: 'STIX TC EXEC FLR -TC to save ASW img fr RAM to FLASH failed',
    54090: 'STIX TC EXEC FLR - Attenuator data acquisition loop timeout',
    54091: 'STIX TC EXEC FLR - TC(236,18) failed - wrong FDIR mask /par type',
    54092: 'STIX TC EXEC FLR - Memory reading failed (TC(6,5) or TC(6,9))',
    54093: 'STIX TC EXEC FLR - HW selftest cannot be exec, already running',
    54094: 'STIX TC EXEC FLR - Memory selftest cannot be exec - address',
    54095: 'STIX TC EXEC FLR - TC to exec ASW image from RAM failed',
    54096: 'STIX TC EXEC FLR - TC236 - 3, 14 or 17 not executed',
    54097: 'STIX TC EXEC FLR - Attenuator control loop timeout',
    54098: 'STIX TC EXEC FLR - List of user selection request is full',
    54099: 'STIX TC EXEC FLR - Filesystem check failed',
    54100: 'STIX TC EXEC FLR - Storing LUT in filesystem failed',
    54101: 'STIX HK report - SID 1',
    54102: 'STIX HK report - SID 2',
    54103: 'STIX HK report - SID 4',
    54104: 'STIX TC EXEC FLR - Saving LUT Ids in ParamMgmt as current failed',
    54105: 'STIX TC EXEC FLR - Problem applying TLUT',
    54106: 'STIX TC EXEC FLR - Incorrect detector ID or register mask',
    54107: 'STIX TC EXEC FLR - Failed to set parameter',
    54108: 'STIX TC EXEC FLR - Invalid parameter sub-id',
    54109: 'STIX TC EXEC FLR - Failed to get parameter',
    54110: 'STIX Science Data Transfer - X-ray L0 auto',
    54111: 'STIX Science Data Transfer - X-ray L1 auto',
    54112: 'STIX Science Data Transfer - X-ray L2 auto',
    54113: 'STIX Science Data Transfer - X-ray L3 auto',
    54114: 'STIX Science Data Transfer - X-ray L0 user',
    54115: 'STIX Science Data Transfer - X-ray L1 user',
    54116: 'STIX Science Data Transfer - X-ray L2 user',
    54117: 'STIX Science Data Transfer - X-ray L3 user',
    54118: 'STIX Science Data Transfer - QL summed light curves',
    54119: 'STIX Science Data Transfer - QL background monitor',
    54120: 'STIX Science Data Transfer - QL detector specific spectra',
    54121: 'STIX Science Data Transfer - QL Variance',
    54122: 'STIX Science Data Transfer - Flare flag and location',
    54124: 'STIX Science Data Transfer - Bckg spectrum for calibration',
    54125: 'STIX Science Data Transfer - Aspect',
    54126: 'STIX Archive Memory Mgmt - User data selections report',
    54127: 'STIX Filesystem check report',
    54128: 'STIX SuSW Parameter report',
    54129: 'STIX ASW Parameter report',
    54130: 'STIX Threshold scan report',
    54131: 'STIX ASIC temperature report',
    54132: 'STIX On-demand ASIC ADC readout report',
    54133: 'STIX ASIC baseline report',
    54134: 'STIX Channel dark current report',
    54135: 'STIX ASIC ADC read report',
    54137: 'STIX ASIC register read report',
    54138: 'STIX Stored attenuator data report',
    54140: 'STIX Subsysystem configuration report',
    54141: 'STIX FDIR parameter reported',
    54142: 'STIX Science Data Transfer - Spectrogram auto',
    54143: 'STIX Science Data Transfer - Spectrogram user',
    54144: 'STIX Science Data Transfer - TM mgmt status and flare list',
    54239: 'STIX Error - Context file(s) not found',
    54240: 'STIX Warning - QL detector failure identification',
    54241: 'STIX Warning - Wrong corr - ATT pos sens vs motor mov',
    54242: 'STIX Warning - AhbRx callback - SpW closed and reinitialised',
    54243: 'STIX Hi Sev Error - STIX req power cycle - SDRAM init timeout',
    54244: 'STIX Hi Sev Error - STIX requesting exec nominal sequence',
    54245: 'STIX Error - SRAM memory check failed',
    54246: 'STIX Warning - Spacewire link error',
    54248: 'STIX Warning - Packet rejected - incorrect CCSDS',
    54249: 'STIX Warning - Packet rejected - too many bytes received',
    54250: 'STIX Warning - Packet rejected - not enough bytes received',
    54251: 'STIX Warning - Packet rejected - corruption indicated by SpW',
    54252: 'STIX Warning - Auto selftest exec on state-machine failed',
    54253: 'STIX Warning - SpW communication restored',
    54255: 'STIX Info - ASIC verif proc correction of regs successful',
    54256: 'STIX Info - Start-up SW boot success',
    54257: 'STIX Info - Application SW boot success',
    54258: 'STIX Info - Mode transition success',
    54259: 'STIX Info - Application SW starting progress report',
    54260: 'STIX Info - TC instrument HW self-test started - SuSW',
    54261: 'STIX Info - TC instrument HW self-test success - SuSW',
    54262: 'STIX Info - TC instrument HW self-test started - ASW',
    54263: 'STIX Info - TC instrument HW self-test success - ASW',
    54264: 'STIX Info - CPU overload condition recovered',
    54265: 'STIX Info - Attenuator operation restored',
    54266: 'STIX Info - HV PSU failure recovered',
    54267: 'STIX Info - SEU in detector recovered',
    54268: 'STIX Info - SpaceWire Time code reception restored',
    54270: 'STIX Warning - LUT not found',
    54271: 'STIX Warning - Incosistent pg addr before and after FLASH fs opr',
    54272: 'STIX Warning - Too many IRQs',
    54273: 'STIX Info - SDRAM init pattern memory test started',
    54274: 'STIX Info - SDRAM init pattern memory test succes',
    54275: 'STIX Info - SDRAM zeroing for EDAC config finished',
    54276: 'STIX Info - EDAC alg for mod of scrubb rate',
    54277: 'STIX Info - HV depolarisation status changed',
    54278: 'STIX Warning - CPU overload condition detected',
    54279: 'STIX Warning - Attenuator operation interrupted - used too freq',
    54280: 'STIX Warning - SEU in detector',
    54281: 'STIX Info - Filesystem initialisation finished',
    54282: 'STIX Warning - SpaceWire Time code reception lost',
    54285: 'STIX Warning - ASIC verif proc found mismatching registers',
    54286: 'STIX Error - Start-up SW boot',
    54287: 'STIX Error - Application SW boot',
    54288: 'STIX Error - Mode transition failure',
    54289: 'STIX Error - TC instrument HW self-test (SuSW)',
    54290: 'STIX Error - TC instrument HS self-test (ASW)',
    54291: 'STIX Error - Too many IRQs',
    54292: 'STIX Error - SDRAM init pattern memory test',
    54293: 'STIX Warning - Filesystem CRC error',
    54295: 'STIX Error - Watchdog failure detected',
    54299: 'STIX Error - Warm reset initiated',
    54300: 'STIX Error - Repeated problem with booting ASW image',
    54301: 'STIX Error - Attenuator motor failure',
    54302: 'STIX Error - Extremely high X-ray events data rate',
    54303: 'STIX Error - Detectors quadrant overcurrent',
    54304: 'STIX Error - Critical temperature of detectors quadrant detected',
    54305: 'STIX Error - HV PSU failure',
    54306: 'STIX Error - SEU in detector persistent',
    54307: 'STIX Error - HW failure of HK monitored line',
    54309: 'STIX Error - HK acquisition',
    54310: 'STIX Hi Sev Error - STIX requesting immediate power down',
    54311: 'STIX Warning - EDAC: detected recoverable SEU',
    54312: 'STIX Warning - ASW image operation failed',
    54313: 'STIX Info - FDIR protection enabled',
    54314: 'STIX Info - Preparing for shutdown',
    54315: 'STIX Error - SW failure of HK monitored line',
    54316: 'STIX Error - SDRAM memory failure during StartASW procedure',
    54317: 'STIX Error - Both PSUs are powered on',
    54318: 'STIX Error - SDRAM initialisation timeout',
    54319: 'STIX Error - FLASH reset error',
    54320: 'STIX Memory Dump Report - MAIN:EEPROM',
    54321: 'STIX Memory Dump Report - MAIN:SRAM',
    54322: 'STIX Memory Dump Report - MAIN:SDRAM',
    54323: 'STIX Memory Dump Report - MAIN:FLASH_A',
    54324: 'STIX Memory Dump Report - MAIN:FLASH_B',
    54325: 'STIX Memory Dump Report - MAIN:ASW_IMAGE_A1',
    54326: 'STIX Memory Dump Report - MAIN:ASW_IMAGE_A2',
    54327: 'STIX Memory Dump Report - MAIN:ASW_IMAGE_B1',
    54328: 'STIX Memory Dump Report - MAIN:ASW_IMAGE_B2',
    54329: 'STIX Memory Check Report',
    54330: 'STIX Connection Test Report',
    54331: 'STIX Context Report from User',
    54332: 'STIX Memory Dump Report - FULL MEM ACCESS',
    54333: 'STIX Memory Dump Report - RED:EEPROM',
    54334: 'STIX Memory Dump Report - RED:SRAM',
    54335: 'STIX Memory Dump Report - RED:SDRAM',
    54336: 'STIX Memory Dump Report - RED:FLASH_A',
    54337: 'STIX Memory Dump Report - RED:FLASH_B',
    54338: 'STIX Memory Dump Report - RED:ASW_IMAGE_A1',
    54339: 'STIX Memory Dump Report - RED:ASW_IMAGE_A2',
    54340: 'STIX Memory Dump Report - RED:ASW_IMAGE_B1',
    54341: 'STIX Memory Dump Report - RED:ASW_IMAGE_B2',
    54342: 'STIX Error - ASIC verif failed (correc mismatch regs of ASICs)',
    54343: 'STIX TC EXEC FLR - LUT upload failed for TC(237,7)',
    54344: 'STIX Warning - Autonomous LUT apply failed',
    54345: 'STIX TC EXEC FLR - RCR parameter update failed for TC(237,10)',
    54346: 'STIX TC EXEC FLR - QL parameter update failed for TC(237,9)',
    54347: 'STIX TC EXEC FLR - Unable to read memory',
    54348: 'STIX TC EXEC FLR - Unable to write memory',
    54349: 'STIX TC EXEC FLR - Unable to read FLASH page in block',
    54350: 'STIX TC EXEC FLR - Unable to erase block',
    54351: 'STIX TC EXEC FLR - Unable to write page',
    54352: 'STIX Warning - No data found for BSD box',
    54353: 'STIX Warning - BSD user request failed',
    54354: 'STIX TC EXEC FLR - Start time gte end time',
    54355: 'STIX TC EXEC FLR - Too many selftests pending',
    54356: 'STIX TC EXEC FLR - Invalid number for avg',
    54357: 'STIX Warning - Test procedure Interupted',
    54358: 'STIX Warning - Async memory operation interrupted',
    54359: 'STIX Warning - Attenuator already in operation',
    54360: 'STIX Warning - Cannot move attenuator because LV is off',
    54361: 'STIX Info - EDAC zeroing of Rotating Buffer started',
    54362: 'STIX Info - EDAC zeroing of Rotating Buffer finished'
}


def get_packet_desc(name):
    try:
        return SPID_DESC[name]
    except KeyError:
        return ''


def get_parameter_desc(name, which=1):
    if which == 3:
        pcf_des = ''
        scos_des = ''
        seperator = ' - '
        try:
            pcf_des = PCF_DESC[name]
        except KeyError:
            seperator = ''
        try:
            scos_des = SCOS_DESC[name]
        except KeyError:
            seperator = ''
        return pcf_des + seperator + scos_des
    elif which == 2:
        try:
            return SCOS_DESC[name]
        except KeyError:
            pass
        try:
            return PCF_DESC[name]
        except KeyError:
            return ''
    else:
        try:
            return PCF_DESC[name]
        except KeyError:
            pass
        try:
            return SCOS_DESC[name]
        except KeyError:
            return ''
