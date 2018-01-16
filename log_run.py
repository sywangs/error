#! /usr/bin/python
# coding:utf-8
# --------------------------------------------------------
# heatmap and pathflow
# Copyright (c) 2017 vmaxx
# Written by fang
# --------------------------------------------------------

import lib.log_class as logclass
import logging,os,sys
import lib.monitor_db_class as monitordbclass
import lib.error_email_class as errorEmailClass

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def run():
    codeRootdir = cur_file_dir()
    logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=codeRootdir+'/cache_/log/' + 'error' + '.event.log',
                        filemode='w')
    log_Obj = logclass.log(codeRootdir)
    status = log_Obj.parse_log()

    # monitordb_obj = monitordbclass.monitor_db(codeRootdir)
    # monitordb_obj.db_see()



if __name__ == "__main__":
    run()
