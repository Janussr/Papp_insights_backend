from os import sep
import pandas as pd

def get_report(id):
    df = pd.read_csv('data/reports.csv', sep=',')
    report = df['id'].str.contains(id) == True
    print(report)

get_report(1)