## Python Tips

---

- Use both jupyter notebook and the editor. They work best in different situations. In particular, I find that while the former is helpful to do any random code scratch or test, the latter is necessary to write down any formal and reproducible code. 
  - The most commonly recommended editor is [vscode](https://code.visualstudio.com/).
  - You can find my tips on Jupyterlab [here](../jupyter/).
- Use [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to manage your python environment for different projects. The advance operation is to use virtual environment, e.g. [pipenv](https://pipenv.pypa.io/en/latest/), [virtualenv](https://virtualenv.pypa.io/en/latest/), etc..
- Use python packages (see below) that someone has built to make your life easier.
- Sometimes there are small piece of code that can make your life easier but are just too simple that no one would make it a formal package. The python files placed in the [util](/util) folder are some simple snippets that are such examples either homemade or stolen from the internet.
  - You can simply apply these snippets into your code.
  - Alternatively you can import them just like the one you installed through conda or pip. In order to do this, you need add the dir where you place your modules to `sys.path`. (see [here](https://stackoverflow.com/a/37008663) and [here](https://stackoverflow.com/a/12257807) if you don't know how to do it).
  - Moreover you can make some module to be executed automatically whenever you launch the python kernel in a Jupyter notebook.
  - Note that you can always try to write your own helpful wheels.

---

## Python Packages

### Econ

- [quantecon](https://github.com/QuantEcon/QuantEcon.py) / [interpolation](https://github.com/EconForge/interpolation.py)
- [pyblp](https://github.com/jeffgortmaker/pyblp) / [torchblp](https://github.com/gzervas/torchblp)
- [numecon](https://github.com/NumEconCopenhagen/NumEcon)
- [Estimagic](https://estimagic.readthedocs.io/en/latest/)
- [respy](https://github.com/OpenSourceEconomics/respy) / [grmpy](https://github.com/OpenSourceEconomics/grmpy) / [soepy](https://github.com/OpenSourceEconomics/soepy)
- [HARK](https://github.com/econ-ark/HARK)

### Econometrics / Statistics

- [statsmodels](https://www.statsmodels.org/stable/index.html)
- [linearmodels](https://bashtage.github.io/linearmodels/)
- [pingouin](https://pingouin-stats.org/)
- [fastreg](https://github.com/iamlemec/fastreg) / [pyfixest](https://github.com/s3alfisc/pyfixest)
- [specification_curve](https://specification-curve.readthedocs.io/en/latest/readme.html)
- [Stargazer](https://github.com/mwburke/stargazer)
- [spreg](https://github.com/pysal/spreg)
- [binscatter](https://github.com/esantorella/binscatter) / [binsreg](https://nppackages.github.io/binsreg/)
- [lifelines](https://github.com/CamDavidsonPilon/lifelines)
- [netrics](https://github.com/bryangraham/netrics)
- [SyntheticControlMethods](https://github.com/OscarEngelbrektson/SyntheticControlMethods)
- [pysynthdid](https://github.com/MasaAsami/pysynthdid)
- [difference-in-differences](https://github.com/bernardodionisi/differences)
- [CausalPy](https://github.com/pymc-labs/CausalPy) 
- [causallib](https://github.com/BiomedSciAI/causallib)

### Probabilistic Programming (Bayesian)

- [numpyro](https://github.com/pyro-ppl/numpyro)
- [pymc3](https://github.com/pymc-devs/pymc3)
- [ArviZ](https://github.com/arviz-devs/arviz)

### Fast Computation

- [numba](https://numba.pydata.org/)
- [jax](https://github.com/google/jax)
- [cupy](https://cupy.dev/)

### Plotting

- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [altair](https://altair-viz.github.io/)
- [matplotlib-label-lines](https://github.com/cphyc/matplotlib-label-lines)
- [adjustText](https://github.com/Phlya/adjustText)
- [pandas_alive](https://github.com/JackMcKew/pandas_alive)
- [folium](https://python-visualization.github.io/folium/)
- [geopandas](https://geopandas.org/)
- [graphviz](https://graphviz.readthedocs.io/en/stable/manual.html)
- [daft](https://github.com/daft-dev/daft)
- [networkx](https://networkx.org/documentation/latest/)
- [multiplex](https://nicholasmamo.github.io/multiplex-plot/index.html)
- [sane_tikz](https://github.com/negrinho/sane_tikz)

### Econ Data

- [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/index.html)
- [WBData](https://github.com/mwouts/world_bank_data)
- [bls](https://github.com/OliverSherouse/bls)
- [fredapi](https://github.com/mortada/fredapi)
- [jpstat](https://github.com/Alalalalaki/jpstat)

### Data - Clean

- [pandas](https://pandas.pydata.org/)
- [missingno](https://github.com/ResidentMario/missingno)
- [pandas_profiling](https://github.com/pandas-profiling/pandas-profiling)
- [fuzzymatcher](https://github.com/RobinL/fuzzymatcher)

### Data - Performance Issues

- [pyarrow](https://arrow.apache.org/docs/python/)
- [dask](https://dask.org/)
- [vaex](https://vaex.readthedocs.io/en/latest/)

### Dashboard / App

- [voila](https://github.com/voila-dashboards/voila)
- [panel](https://panel.holoviz.org/)
- [dash](https://dash.plotly.com/)
- [streamlit](https://github.com/streamlit/streamlit
  )

### Database

- [sqlite](https://docs.python.org/3/library/sqlite3.html)
- [Ibis](https://docs.ibis-project.org/)

### Web Scrapping

- [requests](https://requests.readthedocs.io/en/master/) / [requests-html](https://github.com/psf/requests-html)
- [selenium](https://selenium-python.readthedocs.io/)

---

## Random Notes I Find Useful

[Contributing to Pandas](https://pandas.pydata.org/docs/development/contributing.html) / [Contributing to NumPy](https://numpy.org/devdocs/dev/index.html)

[Hypermodern Python](https://cjolowicz.github.io/posts/) / [Hypermodern Python Cookiecutter](http://cookiecutter-hypermodern-python.readthedocs.io/) / [Create and Publish a Python Package with Poetry](https://johnfraney.ca/posts/2019/05/28/create-publish-python-package-poetry/) / [Python Packaging Notes](https://szj.io/tech/2020/07/12/python-packing-notes.html) / [Packaging Guide](https://github.com/OpenSourceEconomics/ose-packaging-guide#code-quality) / [Publish a package on PyPi using Poetry](https://www.brainsorting.dev/posts/publish-a-package-on-pypi-using-poetry/)

[Three examples of nonlinear least-squares fitting in Python with SciPy](https://hernandis.me/2020/04/05/three-examples-of-nonlinear-least-squares-fitting-in-python-with-scipy.html)

[Network Analysis Made Simple](https://github.com/ericmjl/Network-Analysis-Made-Simple)

[How to wean yourself off Stata and into Python](https://github.com/corybaird/Econometrics) / [Notes and python code for numerical optimization](https://github.com/corybaird/Numerical_Optimization) / [Intro to DSGE models using Python and Dynare](https://github.com/corybaird/DSGE_models)

---

## Non-Econ Stuffs

- [Introduction to Computational Literary Analysis](https://icla2020b.jonreeve.com/)
- [Programming for GIS: Teaching resources](https://github.com/andrea-ballatore/teaching-programming-for-gis)
- [Spatial Data Programming with Python](https://geobgu.xyz/py/#)
- [Bayesian Modeling and Computation in Python](https://bayesiancomputationbook.com/welcome.html)
- [Bayesian Computing Course](https://github.com/fonnesbeck/Bayes_Computing_Course)
- Melanie Walsh - [Introduction to Cultural Analytics & Python](https://github.com/melaniewalsh/Intro-Cultural-Analytics)

