# 10 mins tutorial on Pandas
# https://pandas.pydata.org/pandas-docs/stable/10min.html

import pandas as pd
import numpy as np
# import matplotlib as plt

a = [2, 3.]

print(a)

# PANDAS DATA OBJECT CREATION

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

# create an array of 6 dates starting from the one provided
dates = pd.date_range('20130101', periods=6)
print(dates)

# create a data frame -> table
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

a0 = [3, 3,
      2, 3]
print(a0)
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, alldtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)

df2.dtypes

df.head()


df.index

df.columns

df.values

df.describe()

df.T

df.sort_index(axis=1, ascending=False)

df.sort_values(by='B')


# create a categorical varable (string or enum)
# unordered:
print(pd.Categorical(["bikes", "bus", "car", "train"]))
# ordered:
print(pd.Categorical(["bikes", "bus", "car", "train"], ordered=True))

# ------------------------------------------------------

# SELECTION

# While standard Python / Numpy expressions for selecting and setting
# are intuitive and come in handy for interactive work, for production code,
# we recommend the optimized pandas data access methods,
# .at, .iat, .loc, .iloc and .ix.

# The axis labeling information in pandas objects serves many purposes:
#       Identifies data (i.e. provides metadata) using known indicators,
#       important for analysis, visualization, and interactive console display
#       Enables automatic and explicit data alignment
#       Allows intuitive getting and setting of subsets of the data set

print(df['A'])

print(df[0:3])

# get a cross section using a label
print(df.loc[dates[0]])

# Select on a multi-axis by label
print(df.loc[:, ['A', 'B']])

# Show label slicing, both endpoints are included
df.loc['20130102':'20130104', ['A', 'B']]

# Reduction in the dimensions of the returned object

df.loc['20130102', ['A', 'B']]


# ...

# ------------------------------------------------------

# PLOTTING

ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

ts.plot()
