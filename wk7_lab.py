#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 16:00:10 2017

TIME SERIES PYTHON/PANDAS EXAMPLE SCRIPT

Applications (there are many)
• business and finance
• analysis of stock price, costs, profit, units sold...
• organisational
• monitoring process or quality, workload projections
• government and policy making
• changes in economic, health, crime, statistics
• science and engineering
• signal processing, energy efficiency, cell mutation...
anything involving measurements over time

@author: pesa
"""

import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# read excel document by specifying sheet and columns to be used
# =============================================================================

sqkm = pd.read_excel('ons-mye-population-totals.xls', sheetname='MYE',
                      header=1, usecols='C:D, BI')

# remove completely empty rows
sqkm.dropna(how='all', inplace=True)

# just select London borough rows
sqkm = sqkm.iloc[0:33]
sqkm.rename(columns={'Area name': 'borough',
         'Inner or Outer London': 'location',
         'LAND AREA (Sq Km)': 'sqkm'},
         inplace=True
        )
sqkm['location']=sqkm['location'].str.lower()
print(sqkm.iloc[: , 0:5].head(4))

# print the sum of km^2 for inner and outer boroughs of London
#locSum = sqkm.groupby('location').sum()
#print(locSum.iloc[:,-1])

sqkm.set_index(['location'])
sqkm.groupby('location').sum()


print(sqkm.head())

# =============================================================================
# 
# =============================================================================

df = pd.read_excel('ons-mye-population-totals.xls',
                   sheet_name='MYE',
                   header=1, usecols='C:BG')
# remove completely empty rows
df.dropna(how='all', inplace=True)
# just select London borough rows
df = df.iloc[0:33]
df.rename({'Area name': 'borough',
'Inner or Outer London': 'location'},
axis='columns', inplace=True)
df['location'] = df['location'].str.lower()

df2 = df
df2.set_index(['location', 'borough'], inplace=True)

ts = df2.T

years = pd.date_range('1961', '2016', freq='AS-JUN') # AnnualStarting-June
print(years[0:33])

ts.index = years


# =============================================================================

#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'qt5')

# =============================================================================

from matplotlib.figure import SubplotParams as SPP

spp = SPP(left=None, bottom=None, right=0.7, 
                  top=None, wspace=None, hspace=None)

fig, ax = plt.subplots(figsize=(12,6), subplotpars=spp)

ax = ts['outer'].plot(ax=ax)

#handles, labels = ax.get_legend_handles_labels()

#ax.legend(handles, labels)
ax.legend(bbox_to_anchor=(1.0, 1.1))

# =============================================================================
# 
# =============================================================================


fig2, ax2 = plt.subplots(figsize=(12,6), subplotpars=spp)

ax2 = ts['outer', 'Ealing'].plot(ax=ax2)
ax2 = ts['outer', 'Barnet'].plot(ax=ax2)

#handles, labels = ax.get_legend_handles_labels()

#ax.legend(handles, labels)
ax2.legend(bbox_to_anchor=(1.0, 1.1))


fig3, ax3 = plt.subplots(figsize=(12,6), subplotpars=spp)

ax3 = ts['outer', 'Greenwich'].plot(ax=ax3)
ax3 = ts['inner', 'Lewisham'].plot(ax=ax3)

#handles, labels = ax.get_legend_handles_labels()

#ax.legend(handles, labels)
ax3.legend(bbox_to_anchor=(1.0, 1.1))

# =============================================================================
# 
# =============================================================================


fig4, ax4 = plt.subplots(figsize=(12,6), subplotpars=spp)
in_out = ts.groupby(level='location', axis=1).sum()
in_out.head()

title = 'Mid-year population estimates for inner and outer London' 
# note rubbish y-axis tick labels! 
ax4 = in_out[['inner', 'outer']].plot(ax=ax4, title=title) 


# =============================================================================
# 
# =============================================================================


plt.show()
