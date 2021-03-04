"""
Useful plots in data anlysis
"""

import altair as alt

if __name__ != "__main__":
    __version__ = 0.1


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
