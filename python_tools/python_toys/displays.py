"""
This simple code is used to display two or more pandas dataframes simulatenously.

ref:
https://stackoverflow.com/questions/38783027/jupyter-notebook-display-two-pandas-tables-side-by-side
https://jakevdp.github.io/PythonDataScienceHandbook/03.06-concat-and-append.html

Set as default: add c.InteractiveShellApp.exec_files = ["<your path>/displays.py"] in ipython_config.py
"""


class display_dfs_all:
    """Display HTML representation of multiple DataFrames

    ----------
    display_dfs(df1, df2, pd.concat([df1, df2]), ...)

    # Display all columns and rows. Don't use for large data.
    ----------
    """

    def __init__(self, *args):
        if len(args) < 2:
            raise ValueError('There must be at least 2 DataFrames.')
        for i in args:
            if not isinstance(i, pd.DataFrame):
                raise ValueError('Inputs must be DataFrames.')
        self.args = args

    def _repr_html_(self):
        return ''.join([df.to_html() for df in self.args]).replace('table', 'table style="display:inline"')


class display_dfs_all_:
    """ Display HTML representation of multiple DataFrames with or without name and index

    Parameters:
    ----------
    dfs: List of DataFrames. e.g. [df1, df2, pd.concat([df1, df2]), ...]
    names: List of the name of DataFrames
    index: If show index of DataFrames. True or False

    # Can add more df.to_html(*args) like index if necessary
    # Display all columns and rows. Don't use for large data.
    ----------
   """

    def __init__(self, dfs, names=None, index=True):
        if not isinstance(dfs, list):
            raise ValueError('Input must be a list of DataFrames.')
        self.dfs = dfs
        self.names = names
        self.index = index

    def _repr_html_(self):
        # style = """<div style="float: left; padding: 5px;"><p style='font-family:"Courier New", Courier, monospace'>"""
        if self.names:
            if len(self.names) != len(self.dfs):
                raise ValueError(
                    f'Shape of names {len(self.names)} != Shape of dfs {len(self.dfs)}')
            else:
                html_str = ''.join([df.to_html(index=self.index).replace('<thead>', f'<caption>{name}</caption><thead>')
                                    for df, name in zip(self.dfs, self.names)])\
                    .replace('table', 'table style="display:inline"')  # <caption>{style}{name}</caption><thead>
        else:
            html_str = ''.join([df.to_html(index=self.index) for df in self.dfs]
                               ).replace('table', 'table style="display:inline"')
        return html_str


class display_dfs(object):
    """Display HTML representation of multiple DataFrames and names but truncated
    ----------
    display_dfns('df1', 'df2', 'pd.concat([df1, df2])', ...)

    # Name is df names
    # No. of columns and rows displayed followed defualt setting
    ----------
    """
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""

    def __init__(self, *args):
        if len(args) < 2:
            raise ValueError('There must be at least 2 DataFrames.')
        for i in args:
            if not isinstance(i, str):
                raise ValueError('Inputs must be Strings (names of DataFrames).')
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(i, eval(i)._repr_html_()) for i in self.args)

    def __repr__(self):
        return '\n\n'.join(i + '\n' + repr(eval(i)) for i in self.args)

    def shape(self):
        """ Return max of row and column no. """
        r = max([eval(i).shape[0] for i in self.args])
        c = max([eval(i).shape[1] for i in self.args])
        return r, c
