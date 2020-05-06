import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(r'C:\Users\Pu\Documents\GitHub\GEO572-Project-E.St.Louis\pumping\Pumpage_Data_ESL.xlsx')

df_pump = df.iloc[:,7:]
df_pump = df_pump/10**6/365.25

df.iloc[:,7:] = df_pump

df_fac_pump = df.iloc[:,2:]
df_fac_pump = df_fac_pump.drop(['fac_well_num','depth_total_last_known','lam_x','lam_y'],axis=1)
df_fac_pump = df_fac_pump.groupby(['owner'], as_index=False).sum()

year_list = range(1981,2020)
pump1 = df_fac_pump.iloc[0,1:]
pump2 = df_fac_pump.iloc[102,1:]
pump3 = df_fac_pump.iloc[101,1:]


for i in range(103):
    a = df_fac_pump.iloc[i,1:].mean()
    for j in range(1,39):
        if 10*df_fac_pump.iloc[i,j]<a or df_fac_pump.iloc[i,j]>10*a:
            df_fac_pump.iloc[i,j] = np.nan
            
# replace all 0-value as NaN
df_fac_pump.iloc[:,1:] = df_fac_pump.iloc[:,1:].replace(0,np.nan)
# linear interpolation
df_fac_pump.iloc[:,1:] = df_fac_pump.iloc[:,1:].interpolate(method='linear', limit_direction='forward', axis=1)

pump2_new = df_fac_pump.iloc[102,1:]
pump3_new = df_fac_pump.iloc[101,1:]


plt.figure(figsize=(9,6))
plt.scatter(year_list,pump3,label='original pumpage')
plt.scatter(year_list,pump3_new,label='outliers removed')
plt.title('pumpage of WOOD RIVER')
plt.ylabel('pumpage (MGD)')
plt.xlabel('year')
plt.legend()
plt.show()
