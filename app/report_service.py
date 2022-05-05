import pandas as pd
import csv
from . import models

df = pd.read_csv('app/data/papp_kgslyngby.csv', sep=";")

print(df)


def calculate_report():
    p1 = models.ParkingCategory("Belægningsgrad", "59%")
    p2 = models.ParkingCategory("Overtrædelsesprocent", "7%")

    parking_categories = []

    parking_categories.append(p1)
    parking_categories.append(p2)

    parking_areas = []

    parking_areas.append('Gyldendalsvej')

    new_report = models.Report("ReportName", parking_areas, parking_categories)
    return new_report

def save_report(id, name, parking_areas, categories):
    with open('app/data/reports.csv', 'a') as file:
        writer=csv.writer(file, delimiter=';')
        writer.writerow([id, name, parking_areas, categories])
 