import sys
import os
sys.path.append('.')
from stix.core import mongo_db 
def delete_one(start_run, end_run=-1):
    runs=[]
    if end_run==-1:
        runs=[start_run]
    else:
        runs=range(start_run,end_run)
    print('runs to delete:{}'.format(str(runs)))
    ret=input('Are you sure to delete them ? Y/N: ')
    if ret=='Y':
        mdb = mongo_db.MongoDB()
        mdb.delete_runs(runs)
        print('deleted')


if __name__=='__main__':
    if len(sys.argv)==1:
        print("usage: ./delete_files_from_mongodb <run_begin> [run_end]")
    elif len(sys.argv)==2:
        delete_one(int(sys.argv[1]))
    elif len(sys.argv)==3:
        delete_one(int(sys.argv[1]), int(sys.argv[2]))
