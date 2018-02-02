# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:06:20 2018

@author: Lenovo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_df = pd.read_csv('train.csv')
pred_df = pd.read_csv('test.csv')

train_df.head(20)
train_df.info()
