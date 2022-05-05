import pandas as pd
import csv
from . import models

df = pd.read_csv('app/data/papp_kgslyngby.csv', sep=";")

def get_report(id):
    df = pd.read_csv('app/data/reports.csv', sep=',')
    report_df = df[df['id'] == id]
    report = pd.Series.to_dict(report_df.iloc[0])
    return report

def save_report(id, name, parking_areas, categories):
    with open('app/data/reports.csv', 'a') as file:
        writer=csv.writer(file, delimiter=',')
        string_p_areas = ','.join(parking_areas)
        string_categories = ','.join(categories)
        writer.writerow([str(id), name, string_p_areas, string_categories])

def get_all_reports():
    #df = pd.read_csv('app/data/reports.csv')
    #print(df)
    with open('app/data/reports.csv') as file:
        reports = []
        reader = csv.reader(file, delimiter = ',')
        next(reader)
        for row in reader:
            #reports.append(models.Report(row[0], row[1], row[2], row[3]))
            reports.append({'id':row[0], 'name':row[1], 'parking_areas':row[2], 'parking_categories':row[3]})
    return reports
 