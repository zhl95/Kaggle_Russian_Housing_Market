#!/usr/local/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-5-24 下午9:05
"""
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)

import cPickle
import pandas as pd

# my own module
from conf.configure import Configure


def load_data():
    if not os.path.exists(Configure.processed_train_path):
        train = pd.read_csv(Configure.original_train_path)
    else:
        with open(Configure.processed_train_path, "rb") as f:
            train = cPickle.load(f)

    if not os.path.exists(Configure.processed_test_path):
        test = pd.read_csv(Configure.original_test_path)
    else:
        with open(Configure.processed_test_path, "rb") as f:
            test = cPickle.load(f)

    return train, test


def save_data(train, test):
    with open(Configure.processed_train_path, "wb") as f:
        cPickle.dump(train, f, -1)

    with open(Configure.processed_test_path, "wb") as f:
        cPickle.dump(test, f, -1)