import pandas as pd
import csv
from . import models

df = pd.read_csv('app/data/papp_kgslyngby.csv', sep=";")

def get_report(id):
    reports_df = pd.read_csv('app/data/reports.csv')
    print(reports_df.head())
    report = reports_df[reports_df['id'] == f'{id}']
    print(report)

def save_report(id, name, parking_areas, categories):
    with open('app/data/reports.csv', 'a') as file:
        writer=csv.writer(file, delimiter=';')
        writer.writerow([id, name, parking_areas, categories])

def get_all_reports():
    #df = pd.read_csv('app/data/reports.csv')
    #print(df)
    with open('app/data/reports.csv') as file:
        reports = []
        reader = csv.reader(file, delimiter = ';')
        next(reader)
        for row in reader:
            #reports.append(models.Report(row[0], row[1], row[2], row[3]))
            reports.append({'id':row[0], 'name':row[1], 'parking_areas':row[2], 'parking_categories':row[3]})
    return reports
 