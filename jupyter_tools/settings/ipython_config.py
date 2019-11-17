"""
An Example of Configuration file for ipython.
"""

c = get_config()
c.InteractiveShellApp.exec_lines = [
    "import pandas as pd",
    "import numpy as np",
    "import scipy as sp",
    "import statsmodels.api as sm",
    "import statsmodels.formula.api as smf",
    "import linearmodels as lm",
    "import matplotlib.pyplot as plt",
    "plt.style.use(['ggplot-c'])",  # use customized matplotlib theme
    "import seaborn as sns",
    "pd.options.display.max_rows = 10",
    "pd.options.display.float_format = '{:,.2f}'.format",
    "pd.set_option('max_colwidth', -1)",
    "pd.set_option('io.hdf.default_format','table')",
    "plt.rcParams['font.family'] = 'Meiryo'",
    "from tqdm import tqdm",
    "from labellines import labelLine, labelLines",
    "import altair as alt",
    "from numba import njit, prange, vectorize",
    "import keys",  # must add your customized api-keys file to your path first
]
c.IPKernelApp.matplotlib = 'inline'
c.InlineBackend.figure_format = 'retina'
c.InteractiveShell.ast_node_interactivity = "all"
c.InteractiveShellApp.exec_files = ["/Users/alalalalaki/GitHub/Guide2EconRA/python_tools/displays.py",
                                    "/Users/alalalalaki/GitHub/Guide2EconRA/python_tools/prints.py",
                                    "/Users/alalalalaki/GitHub/Guide2EconRA/python_tools/owari.py",
                                    "/Users/alalalalaki/GitHub/Guide2EconRA/python_tools/cleandata.py", ]
