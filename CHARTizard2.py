#!/usr/bin/env python
# coding: utf-8

# In[42]:

########## capture rate and total stats for all pokemon #########


import pandas as pd
# import numpy as np
# from collections import Counter

def export(data):
  poke = pd.read_csv(data)
  pfilt = poke.filter(items=["name", "base_total"])
  return pfilt

