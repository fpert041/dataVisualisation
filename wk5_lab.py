#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:12:50 2017

@author: pesa
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib% #inline
# the above commented line does not work in a script (at least not in Spyder)
# it may be different in other IDEs and definitely you should use it 
# in iPython environments such as jupyter notebooks
# here, I'm using the below imported method instead:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt5') #inline #qt5


df = pd.read_csv("/Users/pesa/Documents/UNI/dataVis/labs/corr.csv", index_col = 0);

# A scatterplot matrix (or pairs plot) visualises all pair-wise
# varialbe comparisons. These plots are useful for getting an overview
# of multiple variable correlations at the same time. Matplotlib does
# not have a built-in function to make scatterplot matrices, but they
# can easily be generated using Pandas or the Seaborn library.

ax = pd.plotting.scatter_matrix(df, alpha=0.5, diagonal='kde', 
                                figsize=(9,9), range_padding=0.4)

# Fix x-axis label alignment.
for i in range (0, len(ax)):
    ax[5,i].get_xaxis().set_label_coords(0.5, -0.35)
#
# Fix y-axis label alignment.
for i in range (0, len(ax)):
    ax[i,0].get_yaxis().set_label_coords(-0.3, 0.5)
    
#plt.show()


# EXAMPLE SHOWING matplotlib animation (you should not run it inline)

import matplotlib.animation as animation
def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                          repeat=False, init_func=init)
plt.show()