#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 23:46:43 2017

@author: pesa
"""

import pandas as pd
import matplotlib.pyplot as plt
#matplotlib% #inline
# the above commented line does not work in a script (at least not in Spyder)
# it may be different in other IDEs and definitely you should use it 
# in iPython environments such as jupyter notebooks
# here, I'm using the below imported method instead:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt5') #inline #qt5

df = pd.read_csv('coor.csv')

# The OO API is a hierarchically structured set of classes and
# methods. It requires code to be more explicit, which becomes more
# useful as visualisations become more complex. This example is
# arguably simpler in pyplot style.

# In OO-style, we are responsible for managing our own state, i.e. we
# need to define figure and axes variables explicitly.

# Create a figure object of size 9x6 inches, and an array of axes
# objects. The shape of the axes array is (2, 3): 2 rows, 3 columns.
fig, ax = plt.subplots(2,3, figsize=(9,6))

# Plot target vs a on the first axes object.
ax[0,0].scatter(df['target'],df['a'])
ax[0,0].set_xlabel('target') # NB the axis method is `set_xlabel()`
ax[0,0].set_ylabel('a')

# Plot target vs b on the second axes object.
ax[0, 1].scatter(df['target'], df['b'])
ax[0, 1].set_xlabel('target')
ax[0, 1].set_ylabel('b')

# Plot target vs c on the third axes object.
ax[0, 2].scatter(df['target'], df['c'])
ax[0, 2].set_xlabel('target')
ax[0, 2].set_ylabel('c')

# Plot target vs d on the fifth axes object.
ax[1, 1].scatter(df['target'], df['d'])
ax[1, 1].set_xlabel('target')
ax[1, 1].set_ylabel('d')

# Plot target vs e on the sixth axes object.
ax[1, 2].scatter(df['target'], df['e'])
ax[1, 2].set_xlabel('target')
ax[1, 2].set_ylabel('e')

# Increase the space between subplots.
fig.subplots_adjust(wspace=0.4, hspace=0.4)

# Delete the fourth axes because we don’t need it.
fig.delaxes(ax[1, 0])

# Show the plot.
plt.show()



