"""
This simple code is used to print a pandas dataframe with customized length of rows and columns.

Ref: https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
Set as default imported in Jupyter: add `c.InteractiveShellApp.exec_files = ["<your path>/prints.py"]` in ipython_config.py
"""

if __name__ == "__main__":
    import pandas as pd
    # from displays import display_dfs


def prints(x, r=None, c=None, w=-1):
    """Display a DataFrame in Ipython by specified Column numbers and Row numbers.

    Parameters
    ----------
    x : pd.DataFrame or pd.Series

    r : int, optional
        No. of rows shown. By default None, display all rows
    c : int, optional
        No. of columns shown. By default None, display all columns,
    w : int, optional
        Max column width. By default -1.
    """
    # m = pd.options.display.max_rows
    # n = pd.options.display.max_columns
    # w = pd.options.display.max_colwidth

    if isinstance(x, pd.DataFrame):

        with pd.option_context('display.min_rows', r, 'display.max_rows', r, 'display.max_columns', c, 'display.max_colwidth', w):
            if __name__ == "__main__":
                display(x)
            else:
                print(x)

    elif isinstance(x, pd.Series):
        with pd.option_context('display.min_rows', r, 'display.max_rows', r, 'display.max_colwidth', w):
            if __name__ == "__main__":
                display(x)
            else:
                print(x)

    # elif isinstance(x, display_dfs):

    #     with pd.option_context('display.min_rows', r, 'display.max_rows', r, 'display.max_columns', c, 'display.max_colwidth', w):
    #         display(x)

    else:
        raise ValueError('Input must be a pandas object.')
