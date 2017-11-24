# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
# %matplotlib  inline
# get_ipython().run_line_magic('matplotlib', 'qt')

df = pd.read_csv('/Users/pesa/Documents/UNI/dataVis/labs/corr.csv')
df.head()


df.plot.scatter('a', 'target')
df.plot.scatter('b', 'target')
df.plot.scatter('c', 'target')
df.plot.scatter('d', 'target')
df.plot.scatter('e', 'target')

sns.regplot(df['target'], df['a'])

sns.lmplot(x='target', y='d', data = df, fit_reg = True)

plt.figure()
plt.title("Correlation index")
plt.xlabel("class")
plt.ylabel("targets")
plt.plot(df)
#plt.xlim([0, 51])
plt.show()
