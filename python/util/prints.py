"""
This code is used to print a pandas dataframe with customized length of rows and columns.
Ref: https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html

Note:
  - When setting as `exec_files` in `ipython_config`, the `prints` function `display` the DataFrame.
  - Alternatively when import the file, the `prints` function `print` the DataFrame.
"""

import pandas as pd

if __name__ != "__main__":
    __version__ = 0.1


def prints(x, r=None, c=None, w=None):
    """Display a DataFrame in Ipython by specified Column numbers and Row numbers.

    Parameters
    ----------
    x : pd.DataFrame or pd.Series

    r : int, optional
        No. of rows shown. By default None, display all rows
    c : int, optional
        No. of columns shown. By default None, display all columns
    w : int, optional
        Max column width. By default None
    """
    if isinstance(x, pd.DataFrame):
        with pd.option_context('display.min_rows', r,
                               'display.max_rows', r,
                               'display.max_columns', c,
                               'display.max_colwidth', w):
            if __name__ == "__main__":
                display(x)
            else:
                print(x)

    elif isinstance(x, pd.Series):
        with pd.option_context('display.min_rows', r,
                               'display.max_rows', r,
                               'display.max_colwidth', w):
            if __name__ == "__main__":
                display(x)
            else:
                print(x)

    else:
        raise ValueError('Input must be a pandas object.')
