#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:21:30 2019

@author: aaronatkinson
"""

#import packages
import pandas as pd, glob, os


#Assign directory to change or us within directory
directory="/Users/aaronatkinson/Desktop/FoundationWorkUp"

#open files and create list - modify to point at directory
for filename in glob.glob('F1_Tcc_Clin_woMSI.txt'):
    print(filename)
    open(filename)
    df = pd.read_table(filename)
    print(df)
for filename in glob.glob('MSI_Foundation.txt'):
    print(filename)
    open(filename)
    df2 = pd.read_table(filename)
    print(df2)
    
df_merged = df.merge(df2, on='HCI', how='left')
print(df_merged)
df_merged.to_csv("MSI.txt", sep='\t', index=False)