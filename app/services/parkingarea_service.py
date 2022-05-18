import pandas as pd

df = pd.read_csv('app/data/papp_kgslyngby.csv', sep=';')

def all_parking_areas():
    unique_garageCodes = df['garageCode'].unique()
    
    values_list = list(unique_garageCodes)

    return values_list