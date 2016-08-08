
import pandas as p
import numpy as np
import sys
from collections import OrderedDict

COLUMNS = [
    'value_date',
    'ref_num',
    'type',
    'amount',
    'currency',
    'event_date',
    'counterparty_account',
    'counterparty',
    'note1',
    'note2'
]

def read_raw_csv(filepaths):
    '''Read a csv file from argenta'''

    data = p.DataFrame()
    for filepath in filepaths[1:]:
        df = p.read_csv(filepath, sep=';', skiprows=2, 
                names=COLUMNS, index_col=0, decimal=',', thousands='.',
                dayfirst=True, parse_dates=[0,5], encoding="ISO-8859-1")
        data = data.append(df)
    data.sort_index(inplace=True)
    return data

def read_csv(filepath):
    d = p.read_csv(filepath)
    d.value_date = p.to_datetime(d.value_date)
    d.event_date = p.to_datetime(d.event_date)
    d = d.set_index('event_date')
    return d

mhc = OrderedDict([
    ('Total', np.sum), 
    ('Mean', np.mean), 
    ('Min', np.min),
    ('Max', np.max), 
    ('Median', np.median)
    ])

def annual_costs(d):
    costs = d[d['amount']<0]
    costs = costs['amount']
    return costs.groupby(p.TimeGrouper(freq='A')).agg(mhc)

def annual_credit(d):
    costs = d[d['amount']>0]
    costs = costs['amount']
    return costs.groupby(p.TimeGrouper(freq='A')).agg(mhc)

def monthly_costs(d):
    costs = d[d['amount']<0]
    costs = costs['amount']
    return costs.groupby(p.TimeGrouper(freq='M')).agg(mhc)

def monthly_credit(d):
    costs = d[d['amount']>0]
    costs = costs['amount']
    return costs.groupby(p.TimeGrouper(freq='M')).agg(mhc)
