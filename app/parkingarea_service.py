import pandas as pd
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

df = pd.read_csv('data/papp_kgslyngby.csv', sep=';')

def all_parking_areas():
    unique_garageCodes = df['garageCode'].unique()
    
    values_list = list(unique_garageCodes)

    return values_list