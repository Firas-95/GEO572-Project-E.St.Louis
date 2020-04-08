# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:07:02 2020

@author: Pu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\Pu\Documents\GitHub\GEO572-Project-E.St.Louis\pumping\Pumpage_Data_ESL.xlsx')
dft = df.T
dft_pp = dft.iloc[7:,:]

# transform all the pumpage data into float type
dft_pp = pd.DataFrame(dft_pp,dtype=np.float)

# replace all 0 into nan
dft_pp = dft_pp.replace(0,np.nan)

# calculate the number of not-null for each year
print(dft_pp.T.info())
# print(type(dft_pp.iloc[0,12]))

# interpolation
# for gaps between two existing data, do linear interpolation
# for gaps after the last existing data, use backfill method
# for gaps before the first existing data, just leave them open
dft_pp1 = dft_pp.interpolate(method='linear', limit_direction='forward', axis=0)
dft.iloc[7:,:] = dft_pp1
# filled dataset
df_fill = dft.T
# print(dft_pp1.T.info())

year_list = range(1981,2020)
year_list_new = [str(x) for x in year_list]

# if all of the pumpage data is nan, then drop the entire row
df_fill_true = df_fill.dropna(axis=0,how='all',subset=year_list_new)

df_fill_true.to_excel('pumpage data output.xlsx')



#%%
plt.figure(figsize=(12,8))
# plot pumpage data of P_number = 402848
plt.title('p_number = 402848')
plt.xlabel('year')
plt.ylabel('pumpage rate (MGD)')
plt.plot(year_list, df_fill.iloc[44,7:], 'c-*', label='model ready')
plt.plot(year_list, df.iloc[44,7:], 'ro', label='original')
plt.legend()
plt.savefig('p number = 402848')
plt.show()
#%%
plt.figure(figsize=(12,8))
# plot pumpage data of P_number = 403158
plt.title('p_number = 403158')
plt.xlabel('year')
plt.ylabel('pumpage rate (MGD)')
plt.plot(year_list, df_fill.iloc[182,7:], 'c-*', label='model ready')
plt.plot(year_list, df.iloc[182,7:], 'ro', label='original')
plt.legend()
plt.savefig('p number = 403158')
plt.show()

#%%
plt.figure(figsize=(12,8))
# plot pumpage data of P_number = 402986
plt.title('p_number = 402986')
plt.xlabel('year')
plt.ylabel('pumpage rate (MGD)')
plt.plot(year_list, df_fill.iloc[168,7:], 'c-*', label='model ready')
plt.plot(year_list, df.iloc[168,7:], 'ro', label='original')
plt.legend()
plt.savefig('p number = 402986')
plt.show()

