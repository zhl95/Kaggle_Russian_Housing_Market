#!/usr/local/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-5-23 上午11:57
"""
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)

cmd = 'python train_test_preprocess.py'
os.system(cmd)
