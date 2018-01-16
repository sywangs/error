#! /usr/bin/python
# coding:utf-8
# --------------------------------------------------------
# heatmap and pathflow
# Copyright (c) 2017 vmaxx
# Written by fang
# --------------------------------------------------------

import logging,os,sys
import lib.delete_moresql_class as deleteclass

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def run():

    codeRootdir = cur_file_dir()
    unique_obj = deleteclass.unique_sql(codeRootdir)

    unique_obj.db_see()


if __name__ == "__main__":
    run()
