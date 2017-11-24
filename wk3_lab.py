"""import csv into pandas, counts & display histograms."""

# 10 mins tutorial on Pandas
# https://pandas.pydata.org/pandas-docs/stable/10min.html

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create datframe (pandas)
df_height = pd.read_csv('height_data.csv', index_col=0)
df_transport = pd.read_csv('transport_data.csv', index_col=0)

# use the below commands to check loaded dataframe
df_height.head()
df_transport.head() # note how this data is rough! It needs to be counted

# Visualise Hight data

df_height.plot.hist(alpha=0.5)

df_height.plot.density()
df_height.plot.box()


# Visualise Transport data

trans_count = df_transport.transport.value_counts()
print(trans_count)
ax = trans_count.plot.bar(rot=0)

plt.hist(trans_count)

s = pd.Series([6, 6, 7, 5])
print(s.describe())


plt.show()



# ----------------------------------------------------------
