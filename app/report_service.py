import pandas as pd
from . import models

#df = pd.read_csv('data/papp_kgslyngby.csv', sep=";")

#print(df)


def create_report():
    p1 = models.ParkingCategory("Belægningsgrad", "59%")
    p2 = models.ParkingCategory("Overtrædelsesprocent", "7%")

    parking_categories = []

    parking_categories.append(p1)
    parking_categories.append(p2)

    parking_areas = []

    parking_areas.append('Gyldendalsvej')

    new_report = models.Report("ReportName", parking_areas, parking_categories)
    return new_report
