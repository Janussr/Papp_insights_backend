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
    report_date = report.iloc[0].to_dict()['date']
    #Calculate parking categories and apply them to each parking_area
    parking_areas = calculate_categories(parking_area_list, report_date)
    #Add the parking areas with the calculated categories to the report and return it
    new_report = models.Report(report_name, parking_areas, report_date)
    return new_report

def calculate_categories(parking_areas, date):
    lyngby_df = pd.read_csv('app/data/papp_kgslyngby.csv', sep=';')
    total_spaces = []
    vehicle_count = []
    new_parking_areas = []

    for area in parking_areas:
        #Get data about each parking area on the specifie date
        area_data = lyngby_df[lyngby_df["garageCode"].str.contains(area) == True]
        time_interval = area_data[area_data["time"].str.contains(date) == True]

        #Group by vehicle_count and total_spaces and find the average vehicle count
        grouped_vehicle_count = time_interval.groupby("garageCode")['vehicleCount'].mean()
        grouped_total_spaces = time_interval.groupby("garageCode")['totalSpaces'].mean()
        
        #Get fetch the average vehicle count and total spaces from the groupBy Objects
        count = int(grouped_vehicle_count.get(key=area))
        vehicle_count.append(count)
        spaces = int(grouped_total_spaces.get(key=area))
        total_spaces.append(spaces)

        #Create parking category and add it to parking area
        for i in range(len(total_spaces)):
            x = (vehicle_count[i] / total_spaces[i] * 100)
        parking_category = models.ParkingCategory('Belægningsgrad', x)
        new_parking_area = models.ParkingArea(area, parking_category)
        new_parking_areas.append(new_parking_area)
    return new_parking_areas


def save_report(id, name, parking_areas, date):
    with open('app/data/reports.csv', 'a') as file:
        writer=csv.writer(file, delimiter=',')
        string_p_areas = ','.join(parking_areas)
        writer.writerow([str(id), name, string_p_areas, date])

def get_all_reports():
    with open('app/data/reports.csv') as file:
        reports = []
        reader = csv.reader(file, delimiter = ',')
        next(reader)
        for row in reader:
            reports.append({'id':row[0], 'name':row[1], 'parking_areas':row[2], 'date':row[3]})
    return reports
 