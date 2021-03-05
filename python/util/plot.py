"""
Useful plots in data anlysis
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

if __name__ != "__main__":
    __version__ = 0.1


def plot_scatter_with_text(
        data, x, y, z, hue=None, style=None,
        text_condition=None, text_adjust=False, adjust_precision=0.1):
    """
    Use seaborn, matplotlib and adjustText to plot scatter with text
    """
    data = data.copy().reset_index(drop=True)
    ax = sns.scatterplot(data=data, x=x, y=y, hue=hue, style=style)
    if isinstance(text_condition, pd.Series):
        data = data[text_condition].reset_index(drop=True)
    texts = [ax.annotate(text, (data.loc[i, x], data.loc[i, y])) for i, text in enumerate(data[z].values)]
    if text_adjust:
        from adjustText import adjust_text
        adjust_text(texts, precision=adjust_precision)
    return ax


def plot_interactive_lines(data, x, y, hue, alpha=0.2, point_size=15, line_size=1.5):
    """
    Use altair to plot multiple lines with interactive selection
    """
    highlight = alt.selection(type='single', fields=[hue], on='mouseover', nearest=True, bind='legend')
    selection = alt.selection_multi(fields=[hue], on='mouseover', bind='legend')
    base = alt.Chart(data).encode(
        x=x,
        y=y,
        color=hue,
        tooltip=[hue],
    )
    points = base.mark_circle().encode(
        opacity=alt.condition(selection, alt.value(1), alt.value(alpha)),
        size=alt.condition(~highlight, alt.value(point_size), alt.value(point_size*2))
    ).add_selection(highlight)
    lines = base.mark_line().encode(
        opacity=alt.condition(selection, alt.value(1), alt.value(alpha)),
        size=alt.condition(~highlight, alt.value(line_size), alt.value(line_size*2))
    ).add_selection(selection)
    return lines + points

