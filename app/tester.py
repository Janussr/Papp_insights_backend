import pandas as pd

def get_report(id):
    reports_df = pd.read_csv('data/reports.csv', delimiter=';')
    reports_df.set_index('id')
    print(f'{id}')
    report = reports_df[reports_df['id'] == f'{id}']
    #print(report)

get_report(1)