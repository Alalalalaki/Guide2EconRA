"""
This code is used to plot a function with two variables
"""

import numpy as np
import matplotlib.pyplot as plt


def plot3D(x_min, x_max, y_min, y_max, x_n, y_n, z_func,
           x_label='x', y_label='y', z_label='z', zlim=None,
           figsize=(8, 6), cmap='summer', alpha=0.8, rotate=225):
    x_vals = np.linspace(x_min, x_max, x_n)
    y_vals = np.linspace(y_min, y_max, y_n)
    x_mesh, y_mesh = np.meshgrid(x_vals, y_vals, indexing='ij')
    try:
        z_vals = z_func(x_mesh, y_mesh)
    except ValueError:
        z_vals = np.zeros((x_n, y_n))
        for i in range(x_n):
            for j in range(y_n):
                z_vals[i, j] = z_func(x_vals[i], y_vals[j])
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    ax = fig.gca(projection='3d')
    ax.plot_surface(x_mesh, y_mesh, z_vals, cmap=cmap, alpha=alpha)  # winter
    ax.set(xlabel=x_label, ylabel=y_label, zlabel=z_label, zlim=zlim,)
    ax.zaxis.set_rotate_label(False)  # ?
    ax.view_init(ax.elev, rotate)  # view direction
    plt.close()
    return fig
