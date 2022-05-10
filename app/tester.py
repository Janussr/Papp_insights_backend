from os import sep
import pandas as pd
import models

def get_report(id):
    
    df = pd.read_csv('data/reports.csv', sep=',')
    lyngby_df = pd.read_csv('data/papp_kgslyngby.csv', sep=';')

    time = "2022-01-01 00:00:05"
    total_spaces = []
    vehicle_count = []
    free_spaces = []

    new_parking_areas = []

    report = df[df['id'] == id]
    parking_area_string = report.iloc[0].parking_areas
    parking_area_list = parking_area_string.split(',')
    for area in parking_area_list:
        #Narrow down datasets based on areas in report
        area_data = lyngby_df[lyngby_df["garageCode"].str.contains(area) == True]
        time_interval = area_data[area_data["time"].str.contains(time) == True]

        #Get the information needed to perform categories
        total_spaces.append(int(time_interval.totalSpaces))
        vehicle_count.append(int(time_interval.vehicleCount))
        free_spaces.append(int(time_interval.freeSpaces))

        #Create a parking category
        parking_category = models.ParkingCategory('Belægningsgrad', vehicle_count)

        #Create parking areas
        for i in range(len(parking_area_list)):
            new_parking_area = models.ParkingArea(i, parking_category)
            new_parking_areas.append(new_parking_area)

    new_report = models.Report('navn', new_parking_areas)

    #return report.iloc[0]
    return new_parking_areas[0].name

print(get_report(1))