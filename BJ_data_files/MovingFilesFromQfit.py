# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:10:00 2024

@author: henry
"""
"Thsi can only be ran on laptop because of the file directories."

import os
import shutil

source_dir = 'C:/ProgramData/qfit/cvdata'
target_dir = 'C:/Users/henry_ah1kl9o/OneDrive/Documents/GitHub/python_FNG/BJ_data_files'

for file_name in os.listdir(source_dir):
    if file_name.endswith('.csv'):
        shutil.move(os.path.join(source_dir, file_name), target_dir)
