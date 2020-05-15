# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
# import the pumpage data
df = pd.read_excel('Pumpage_Data_ESL.xlsx')

# transform the unit into MGD
df_pump = df.iloc[:, 7:]
df_pump = df_pump / 10 ** 6 / 365.25
df.iloc[:, 7:] = df_pump

# replace all 0 value to be nan and drop a row if all pumpage is nan
df.replace(0, np.nan)
year_list = range(1981, 2020)
year_list_str = [str(i) for i in year_list]
# print(year_list_str)
list_drop = []  # drop lines with no pumpage records
for ind, row in df.iterrows():
    if df.iloc[ind, 7:].isnull().values.all():
        list_drop.append(ind)
df = df.drop(list_drop)
# df = df.dropna(axis=0,how='all',subset=year_list_str)
# reset index
df = df.reset_index(drop=True)

# calculate the sum of pumpage based on each facility
df_fac_pump = df.iloc[:, 2:]
df_fac_pump = df_fac_pump.drop(['fac_well_num', 'depth_total_last_known', 'lam_x', 'lam_y'], axis=1)
df_fac_pump = df_fac_pump.groupby(['owner'], as_index=False).sum()

print(df_fac_pump)
df_fac_pump_copy = df_fac_pump.copy()


def pump_modified_plot(irow, df1, df_fac_pump_copy):
    year_list = range(1981, 2020)
    for j in range(103):
        if df_fac_pump_copy.iloc[j, 0] == df1.iloc[irow, 0]:
            break
    pump = df_fac_pump_copy.iloc[j, 1:]
    pump_new = df1.iloc[irow, 1:]
    plt.figure(figsize=(9, 6), facecolor="white")

    plt.scatter(year_list, pump, marker="x", s=26, label='Original pumpage')
    plt.scatter(year_list, pump_new, c="red",label='Outliers removed')
    plt.title('Pumpage of' + ' ' + df_fac_pump_copy.iloc[j, 0], fontsize=18, fontweight="bold")
    plt.ylabel('Pumpage (MGD)', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.xlim(1980, 2020)
    plt.ylim(-0.5, 1.05 * np.max(pump))
    plt.legend(fontsize=14)
    plt.show()


for i in range(102):
    a = df_fac_pump.iloc[i, 1:].mean()
    for j in range(1, 39):
        # identify outliers and replace with nan
        if 10 * df_fac_pump.iloc[i, j] < a or df_fac_pump.iloc[i, j] > 10 * a:
            df_fac_pump.iloc[i, j] = np.nan

# do interpolation and forward fill for gaps
df_fac_pump.iloc[:, 1:] = df_fac_pump.iloc[:, 1:].replace(0, np.nan)
df_fac_pump.iloc[:, 1:] = df_fac_pump.iloc[:, 1:].interpolate(method='linear', limit_direction='forward', axis=1)
list_drop = []  # drop lines with no pumpage records in facility level
for ind, row in df_fac_pump.iterrows():
    if df_fac_pump.iloc[ind, 1:].isnull().values.all():
        list_drop.append(ind)
df1 = df_fac_pump.drop(list_drop)
df1 = df1.reset_index(drop=True)
# print(df1.head())

# import the modified data into a csv file
# df1.to_csv('modified_facility_pump.csv')

# 5 facilities with greatest demand
pump_modified_plot(19, df1, df_fac_pump_copy)
pump_modified_plot(30, df1, df_fac_pump_copy)
pump_modified_plot(11, df1, df_fac_pump_copy)
pump_modified_plot(70, df1, df_fac_pump_copy)
pump_modified_plot(75, df1, df_fac_pump_copy)
