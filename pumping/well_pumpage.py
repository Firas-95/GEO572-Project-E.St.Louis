import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def isNan(df, index, col):
    return np.isnan(df.iloc[index, col])


def plot_figure(index):
    plt.figure()
    df1.iloc[index, 7:].plot(style='x-r')
    df0.iloc[index, 7:].plot(style='ob')
    plt.legend(['model-ready', 'original'])
    plt.title('p number=' + str(df0.iloc[index, 0]))
    plt.xlabel('year')
    plt.ylabel('pumpage rate (MGD)')
    plt.show()


df0 = pd.read_excel('Pumpage_Data_ESL.xlsx')
df0 = df0.replace(0, np.nan)  # replace zeros with nan

df_pump = df0.iloc[:, 7:]
df_pump = pd.DataFrame(df_pump, dtype=np.float)
count_101 = 0  # case 1: number-nan-number
count_1001 = 0  # case 2: number-nan-nan-number
count_10001 = 0  # case 3: number-nan-nan-nan-number
count_110 = 0  # case 4: number-number-nan

for ind, row in df_pump.iterrows():
    for i in list(range(df_pump.shape[1]))[1:-1]:  # case 1
        if (isNan(df_pump, ind, i)) and (not isNan(df_pump, ind, i - 1)) and (
                not isNan(df_pump, ind, i + 1)):
            df_pump.iloc[ind, i] = 0.5 * (df_pump.iloc[ind, i - 1] + df_pump.iloc[ind, i + 1])
            count_101 += 1

    for j in list(range(df_pump.shape[1]))[1:-2]:  # case 2
        if (isNan(df_pump, ind, j)) and (not isNan(df_pump, ind, j - 1)) and (
                isNan(df_pump, ind, j + 1)) and (not isNan(df_pump, ind, j + 2)):
            df_pump.iloc[ind, j] = df_pump.iloc[ind, j - 1] + (df_pump.iloc[ind, j + 2] - df_pump.iloc[ind, j - 1]) / 3
            df_pump.iloc[ind, j + 1] = 0.5 * (df_pump.iloc[ind, j] + df_pump.iloc[ind, j + 2])
            count_1001 += 2

    for k in list(range(df_pump.shape[1]))[1:-3]:  # case 3
        if (isNan(df_pump, ind, k)) and (not isNan(df_pump, ind, k - 1)) and (
                isNan(df_pump, ind, k + 1)) and (isNan(df_pump, ind, k + 2)) and (not isNan(df_pump, ind, k + 3)):
            df_pump.iloc[ind, k] = df_pump.iloc[ind, k - 1] + (df_pump.iloc[ind, k + 3] - df_pump.iloc[ind, k - 1]) / 4
            df_pump.iloc[ind, k + 1] = df_pump.iloc[ind, k - 1] + (
                    df_pump.iloc[ind, k + 3] - df_pump.iloc[ind, k - 1]) / 2
            df_pump.iloc[ind, k + 2] = df_pump.iloc[ind, k + 3] - (
                    df_pump.iloc[ind, k + 3] - df_pump.iloc[ind, k - 1]) / 4
            count_10001 += 3

    for l in list(reversed(range(df_pump.shape[1])[2:])):  # case 4
        if (isNan(df_pump, ind, l)) and (not isNan(df_pump, ind, l - 1)) and (
                not isNan(df_pump, ind, l - 2)):
            df_pump.iloc[ind, l] = df_pump.iloc[ind, l - 1] + (
                    df_pump.iloc[ind, l - 1] - df_pump.iloc[ind, l - + 2])
            count_110 += 1

print('total times of interpolation:', count_101 + count_1001 + count_110 + count_10001)
df1 = pd.concat([df0.iloc[:, :7], df_pump], axis=1)
after = df1.iloc[:, 7:].count(axis=1)
plot_figure(182)
plot_figure(273)
plot_figure(363)
list_drop = []  # drop lines with no pumpage records
for ind, row in df1.iterrows():
    if df1.iloc[ind, 7:].isnull().values.all():
        list_drop.append(ind)
df1 = df1.drop(list_drop)

df1 = df1.set_index('p_num')  # set 'p_num' as the index
df1.to_csv("Modified_Pumpage_Data_ESL.csv")
