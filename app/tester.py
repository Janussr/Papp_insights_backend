from os import sep
import pandas as pd

def get_report(id):
    df = pd.read_csv('data/reports.csv', sep=',')
    report = df[df['id'] == id]
    return report.iloc[0]