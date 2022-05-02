import pandas as pd
from models import Report

df = pd.read_csv('../data/papp_kgslyngby.csv', sep=";")

print(df)


def create_report():
    return None