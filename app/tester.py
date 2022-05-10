from os import sep
import pandas as pd

def get_report(id):
    df = pd.read_csv('data/reports.csv', sep=',')
    lyngby_df = pd.read_csv('data/papp_kgslyngby.csv', sep=';')

    time = "2022-01-01 00:00:05"
    total_spaces = []
    vehicle_count = []
    free_spaces = []

    report = df[df['id'] == id]
    parking_area_string = report.iloc[0].parking_areas
    parking_area_list = parking_area_string.split(',')
    for area in parking_area_list:
        area_data = lyngby_df[lyngby_df["garageCode"].str.contains(area) == True]
        time_interval = area_data[area_data["time"].str.contains(time) == True]
        total_spaces.append(int(time_interval.totalSpaces))
        vehicle_count.append(int(time_interval.vehicleCount))
        free_spaces.append(int(time_interval.freeSpaces))
    #return report.iloc[0]
    return total_spaces

print(get_report(1))
#get_report(1)