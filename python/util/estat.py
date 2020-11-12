"""
This simple code is a "second-tier" wrapper for accessing eStat data through japandas.
An eStat key is needed.

Caution: the orignal pkg japandas is no longer working. This code needs a fixed version of japandas.
"""

__version__ = 0.0

import pandas as pd
import japandas as jpd

from API_KEYS import eStat as key
from snippets import z2h


def clean_list(df):
    df = df.copy()
    df = (df
          .applymap(z2h.str_z2h)
          .rename(columns={'統計表ID': 'ID', '調査年月': 'period'})
          .assign(period=lambda df: df.period.astype(int))
          )

    return df


def clean_data(df):
    df = df.copy()
    df = (df
          .applymap(z2h.str_z2h)
        #   .reset_index(drop=True)
          )
    return df


def DataRead(id_, ):
    """
    Read eStat datalist or data.
    """
    id_len = len(id_)
    if (id_len != 8) and (id_len != 10):
        raise ValueError('Length of id must be either 8 or 10.')

    data = jpd.DataReader(id_, 'estat', appid=key)

    # in case the data large than the limit 100_000 once
    n = 1
    while len(data) % 100_000 == 0:
        if n == 1:
            print('downloading', end=' ', flush=True)
        n = n + 100_000
        data_more = jpd.DataReader(id_, 'estat', appid=key, startPosition=n)
        data = pd.concat([data, data_more], sort=False, ignore_index=True)
        print('.', end=' ', flush=True)

    if id_len == 8:
        data = clean_list(data)
    else:
        data = clean_data(data)

    return data
