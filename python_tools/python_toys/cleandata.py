"""
Function factory for data cleaning
"""


def clean_column_name(df, n):
    """
    combine the top n rows to be the column name
    """
    column = df.iloc[:n, :]
    column = column.fillna('').apply(lambda x: '_'.join(
        x.astype(str).drop_duplicates().values))
    df = df.iloc[n:, :].reset_index(drop=True)
    df.columns = column
    return df
