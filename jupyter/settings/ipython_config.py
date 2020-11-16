"""
An Example of Configuration file for ipython.
"""

c = get_config()
c.InteractiveShellApp.exec_lines = [
    "import numpy as np",
    "import scipy as sp",
    "import pandas as pd",
    "pd.options.display.max_rows = 10",
    "pd.options.display.float_format = '{:,.2f}'.format",
    "pd.set_option('max_colwidth', -1)",
    "pd.set_option('io.hdf.default_format','table')",
    "import matplotlib.pyplot as plt",
    "import seaborn as sns",
    "plt.style.use(['ggplot-c'])",  # use some customized matplotlib theme
    "plt.rcParams['font.family'] = 'Meiryo'",
    "from labellines import labelLine, labelLines",
    "import altair as alt",
    "import statsmodels.api as sm",
    "import statsmodels.formula.api as smf",
    "import linearmodels as lm",
    "from tqdm import tqdm",
    "from numba import njit, prange, vectorize",
    "import API_KEYS",  # add your customized api-keys file to your path
    "from util import cleandata",
]
c.IPKernelApp.matplotlib = 'inline'
c.InlineBackend.figure_format = 'retina'
c.InteractiveShell.ast_node_interactivity = "all"
c.InteractiveShellApp.exec_files = [
                                    "/Users/alalalalaki/GitHub/Guide2EconRA/python/util/prints.py",
                                    "/Users/alalalalaki/GitHub/Guide2EconRA/python/util/owari.py",
                                    ]
# c.IPCompleter.greedy = True
