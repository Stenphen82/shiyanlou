# -*- coding:utf-8 -*-

import pandas as pd
from pandas import Series, DataFrame

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    df1=DataFrame({'Date': ['2008-12-31'], 'Open': [0], 'High': [0], 'Low': [0], 'Close': [0], 'Volume': [0]})
    data=pd.concat([df1,data])
    data.Date=pd.to_datetime(data.Date)
    data.set_index('Date',inplace=True)
    data_season=data.resample('3M').sum()
    volume_season=data_season.sort_values(by='Volume')

    return volume_season.Volume[-2]

if __name__=='__main__':
    quarter_volume()
    
