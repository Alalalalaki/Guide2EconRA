"""
This simple code is used to directly access eStat data through japandas.
You also need to set up a keys.py file to place your estat api key.
"""

import japandas as jpd
import keys
import pandas as pd


def clean_list(df):
    df = df.copy()
    df = (df
          .rename(columns={'統計表ID': 'ID', '調査年月': 'period'})
          .assign(period=lambda df: df.period.astype(int))
          )

    return df


def DataRead(id_, ):
    """
    Read eStat datalist or data.
    """
    id_len = len(id_)
    if (id_len != 8) and (id_len != 10):
        raise ValueError('Length of id must be either 8 or 10.')

    data = jpd.DataReader(id_, 'estat', appid=keys.jpd_key)

    # in case the data large than the limit 100_000 once
    n = 1
    while len(data) % 100_000 == 0:
        n = n + 100_000
        data_more = jpd.DataReader(id_, 'estat', appid=keys.jpd_key, startPosition=n)
        data = pd.concat([data, data_more], sort=False, ignore_index=True)
        print('.', end=' ')

    if id_len == 8:
        data = clean_list(data)

    return data
