import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# import the pumpage data
df = pd.read_excel(r'C:\Users\Pu\Documents\GitHub\GEO572-Project-E.St.Louis\pumping\Pumpage_Data_ESL.xlsx')

# transform the unit into MGD
df_pump = df.iloc[:,7:]
df_pump = df_pump/10**6/365.25
df.iloc[:,7:] = df_pump


# calculate the sum of pumpage based on each facility
df_fac_pump = df.iloc[:,2:]
df_fac_pump = df_fac_pump.drop(['fac_well_num','depth_total_last_known','lam_x','lam_y'],axis=1)
df_fac_pump = df_fac_pump.groupby(['owner'], as_index=False).sum()

# print(df_fac_pump)
df_fac_pump_copy = df_fac_pump.copy()


def pump_modified_plot(irow):
    # define a function to make the plot of annual pumpage for each facility
    year_list = range(1981,2020)
    pump = df_fac_pump_copy.iloc[irow,1:]
    pump_new = df_fac_pump.iloc[irow,1:]
    plt.figure(figsize=(9,6),facecolor="white")
    plt.scatter(year_list,pump,label='original pumpage')
    plt.scatter(year_list,pump_new,label='outliers removed')
    plt.title('pumpage of' + ' ' + df_fac_pump_copy.iloc[irow,0])
    plt.ylabel('pumpage (MGD)')
    plt.xlabel('year')
    plt.legend()
    
# year_list = range(1981,2020)
# pump1 = df_fac_pump.iloc[0,1:]
# plt.figure(figsize=(9,6))
# plt.title('ALHAMBRA with outliers')
# plt.scatter(year_list,pump1)
# plt.ylabel('pumpage (MGD)')
# plt.xlabel('year')


for i in range(103):
    a = df_fac_pump.iloc[i,1:].mean()
    for j in range(1,39):
        # identify outliers and replace with nan
        if 10*df_fac_pump.iloc[i,j]<a or df_fac_pump.iloc[i,j]>10*a:
            df_fac_pump.iloc[i,j] = np.nan

# do interpolation and forward fill for gaps
df_fac_pump.iloc[:,1:] = df_fac_pump.iloc[:,1:].replace(0,np.nan)
df_fac_pump.iloc[:,1:] = df_fac_pump.iloc[:,1:].interpolate(method='linear', limit_direction='forward', axis=1)          

pump2_new = df_fac_pump.iloc[102,1:]
pump3_new = df_fac_pump.iloc[101,1:]


# create 5 plots to show the modified pumpage data for each facility
pump_modified_plot(0)
pump_modified_plot(29)
pump_modified_plot(83)
pump_modified_plot(102)
pump_modified_plot(103)
