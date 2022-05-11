import pandas as pd
import csv
from . import models

df = pd.read_csv('app/data/papp_kgslyngby.csv', sep=";")

def get_report(id):
    df = pd.read_csv('app/data/reports.csv', sep=',')

    #Get the specific report from the csv file
    report = df[df['id'] == id]
    #Create list of parking areas from the report
    parking_area_string = report.iloc[0].parking_areas
    parking_area_list = parking_area_string.split(',')
    #Getting the name of the report
    report_name = report.iloc[0].to_dict()['name']
    #Calculate parking categories and apply them to each parking_area
    parking_areas = calculate_categories(parking_area_list)
    print(len(parking_areas))
    #Add the parking areas with the calculated categories to the report and return it
    new_report = models.Report(report_name, parking_areas)
    return new_report

def calculate_categories(parking_areas):
    print(parking_areas)
    lyngby_df = pd.read_csv('app/data/papp_kgslyngby.csv', sep=';')
    time = "2022-01-01 00:00:05"
    total_spaces = []
    vehicle_count = []
    free_spaces = []
    new_parking_areas = []
    for area in parking_areas:
        area_data = lyngby_df[lyngby_df["garageCode"].str.contains(area) == True]
        time_interval = area_data[area_data["time"].str.contains(time) == True]

        #Get the information needed to perform categories
        total_spaces.append(int(time_interval.totalSpaces))
        vehicle_count.append(int(time_interval.vehicleCount))
        free_spaces.append(int(time_interval.freeSpaces))

        #Create a parking category
        for i in range(len(total_spaces)):
            x = round((vehicle_count[i] / total_spaces[i] * 100), 2)
        parking_category = models.ParkingCategory('Belægningsgrad', x)
        new_parking_area = models.ParkingArea(area, parking_category)
        new_parking_areas.append(new_parking_area)
    return new_parking_areas


def save_report(id, name, parking_areas):
    with open('app/data/reports.csv', 'a') as file:
        writer=csv.writer(file, delimiter=',')
        string_p_areas = ','.join(parking_areas)
        writer.writerow([str(id), name, string_p_areas])

def get_all_reports():
    #df = pd.read_csv('app/data/reports.csv')
    #print(df)
    with open('app/data/reports.csv') as file:
        reports = []
        reader = csv.reader(file, delimiter = ',')
        next(reader)
        for row in reader:
            #reports.append(models.Report(row[0], row[1], row[2]))
            reports.append({'id':row[0], 'name':row[1], 'parking_areas':row[2]})
    return reports
 