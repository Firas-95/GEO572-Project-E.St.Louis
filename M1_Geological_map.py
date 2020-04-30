

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep

def inter(x, L1, L2, L3, L4, L5, title): 
    spl1 = splrep(x, L1, k=3)
    spl2 = splrep(x, L2, k=3)
    spl3 = splrep(x, L3, k=2)
    spl4 = splrep(x, L4, k=2)
    spl5 = splrep(x, L5, k=2)
    xnew = np.linspace(x.min(),x.max(),300)
    L1_smooth = splev(xnew, spl1)
    L2_smooth = splev(xnew, spl2)
    L3_smooth = splev(xnew, spl3)
    L4_smooth = splev(xnew, spl4)
    L5_smooth = splev(xnew, spl5)
    plt.plot(xnew, L1_smooth, color='black', label='Surface')
    plt.plot(xnew, L2_smooth, color='lightcoral', label='fine-grained')
    plt.fill_between(xnew, L1_smooth, L2_smooth, hatch='.', color='lightcoral', alpha=0.4)
    plt.plot(xnew, L3_smooth, color='green', label='coarse-grained')
    plt.fill_between(xnew, L2_smooth, L3_smooth, hatch='o', color='green', alpha=0.25)
    plt.plot(xnew, L4_smooth, color='blue', label='very coarse-grained')
    plt.fill_between(xnew, L3_smooth, L4_smooth, hatch='O', color='blue', alpha=0.1)
    #plt.plot(xnew, L5_smooth, color='brown', label='rock-bed')
    #plt.fill_between(xnew, L4_smooth, L5_smooth, hatch='X', color='brown', alpha=0.4)
    for i in range(len(x)):
        plt.vlines(x[i], L1[i]+20, L4[i]-20, colors='purple',linestyle='--')
    plt.title(title)
    plt.xlabel('Distance [Mile]')
    plt.ylabel('Elevation AMSL [ft]')
    plt.legend(loc='best')
    plt.grid(which='both', linestyle='--')
    plt.show()
#%% North-South well logs 1
# 38.8679°N  -90.1243°E
d = 0
elev = 422.65  
belev = 280
log = elev - np.array([0, 35, 110, 117])
# 38.71889°N -90.14772°E
d1 = d + 10.37
elev1 = 419.62 
belev1 = 310
log1 = elev1 - np.array([0, 70, 80, 109])
# 38.69646°N -90.14629°E
d2 = d1 + 1.55
elev2 = 421.29 
belev2 = 310 
log2 = elev2 - np.array([0, 30, 74, 106])
# 38.66475°N -90.14377°E
d3 = d2 + 2.2
elev3 = 418.37 
belev3 = 305
log3 = elev3 - np.array([0, 4, 40, 88])
# 38.64030°N -90.14139°E
d4 = d3 + 1.69
elev4 = 400.37 
belev4 = 280
log4 = elev4 - np.array([0, 32, 80, 100])
# 38.61171°N -90.14466°E
d5 = d4 + 1.98
elev5 = 415.01
belev5 = 290
log5 = elev5 - np.array([0, 20, 100, 123])
#  Lon: -90.1404 / Lat: 38.5554
d6 = d5 + 3.9
elev6 = 405.82 
belev6 = 300
log6 = elev6 - np.array([0, 15, 30, 107])
# Lon: -90.1374 / Lat: 38.5405
d7 = d6 + 1.04
elev7 = 418.18
belev7 = 320
log7  = elev7 - np.array([0, 40, 80, 89]) 
# Lon: -90.1367 / Lat: 38.5222
d8 = d7 + 1.27
elev8 = 458.58 
belev8 = 340
log8  = elev8 - np.array([0, 108, 108, 108]) 
#9 Lon: -90.1278 / Lat: 38.4868
d9 = d8 + 2.49
elev9 = 560.97   
belev9 = 400
log9 = elev9 - np.array([0, 145, 145, 145])
''' plotting the data '''
x = np.array([d, d1, d2, d3, d4, d5, d6, d7, d8, d9])
L1 = [log[0], log1[0], log2[0], log3[0], log4[0], log5[0], log6[0], log7[0], log8[0], log9[0]]
L2 = [log[1], log1[1], log2[1], log3[1], log4[1], log5[1], log6[1], log7[1], log8[1], log9[1]]
L3 = [log[2], log1[2], log2[2], log3[2], log4[2], log5[2], log6[2], log7[2], log8[2], log9[2]]
L4 = [log[3], log1[3], log2[3], log3[3], log4[3], log5[3], log6[3], log7[3], log8[3], log9[3]]
L5 = [belev, belev1, belev2, belev3, belev4, belev5, belev6, belev7, belev8, belev9]

plt.plot(x, L1, 'o-', color='black', label='Surface')
plt.plot(x, L2, color='lightcoral', label='fine-grained')
plt.fill_between(x, L1, L2, hatch='.', color='lightcoral', alpha=0.4)
plt.plot(x, L3, color='green', label='coarse-grained')
plt.fill_between(x, L2, L3, hatch='o', color='green', alpha=0.25)
plt.plot(x, L4, color='blue', label='very coarse-grained')
plt.fill_between(x, L3, L4, hatch='O', color='blue', alpha=0.1)
plt.plot(x, L5, 'o-', color='brown', label='rock-bed')
plt.fill_between(x, L4, L5, hatch='/', color='brown', alpha=0.5)
for i in range(len(x)):
    plt.vlines(x[i], L1[i]+20, L4[i]-20, colors='purple',linestyle='--')
plt.text(15, 550, 'South --->', bbox=dict(facecolor='white', alpha=0.5), fontsize = 14)
plt.title('North-South profile 1')
plt.xlabel('Distance [Mile]')
plt.ylabel('Elevation AMSL [ft]')
plt.legend(loc='best')
plt.grid(which='both', linestyle='--')
plt.show()
''' for interpolated plot '''
#inter(x, L1, L2, L3, L4, L5, 'Interpolated North-South profile 1')

#%% North-South well logs 2
#1 Lon: -90.0647 / Lat: 38.8474
d1 = 0
elev1 = 442.18
belev1 = 280
log1 = elev1 - np.array([0, 23, 80, 141])
#2 Lon: -90.0633 / Lat: 38.8218
d2 = d1 + 1.77
elev2 = 426.24
belev2 = 320
log2 = elev2 - np.array([0, 8, 57, 104])
#3 Lon: -90.0634 / Lat: 38.8065
d3 = d2 + 1.06
elev3 = 427.06
belev3 = 309
log3 = elev3 - np.array([0, 30, 105, 109])
#4 Lon: -90.0564 / Lat: 38.7600
d4 = d3 + 3.24
elev4 = 422.84
belev4 = 304
log4 = elev4 - np.array([0, 31, 66, 94])
#5 Lon: -90.0617 / Lat: 38.7267
d5 = d4 + 2.32
elev5 = 416.31
belev5 = 300
log5 = elev5 - np.array([0, 3, 18, 97])
#6 Lon: -90.0628 / Lat: 38.7046
d6 = d5 + 1.53
elev6 = 419.31
belev6 = 300
log6 = elev6 - np.array([0, 10, 45, 117])
#7 Lon: -90.0568 / Lat: 38.6798
d7 = d6 + 1.74
elev7 = 419.16
belev7 = 275
log7  = elev7 - np.array([0, 20, 70, 95]) 
#8 Lon: -90.0516 / Lat: 38.6442
d8 = d7 + 2.48
elev8 = 414.21
belev8 = 300 
log8 = elev8 - np.array([0, 20, 30, 100])
#9 Lon: -90.0634 / Lat: 38.6262
d9 = d8 + 1.4
elev9 = 421.32
belev9 = 300
log9 = elev9 - np.array([0, 10, 60, 118])
#10 Lon: -90.0647 / Lat: 38.5509
d10 = d9 + 5.21 
elev10 = 524.02  
belev10 = 360
log10 = elev10 - np.array([0, 131, 131, 131])
#11 Lon: -90.0617 / Lat: 38.498
d11 = d10 + 3.65
elev11 =  539.43  
belev11 = 300
log11 = elev10 - np.array([0, 194, 194, 194])

''' plotting the data '''
x = np.array([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11])
L1 = [log1[0], log2[0], log3[0], log4[0], log5[0], log6[0], log7[0], log8[0], log9[0], log10[0], log11[0]]
L2 = [log1[1], log2[1], log3[1], log4[1], log5[1], log6[1], log7[1], log8[1], log9[1], log10[1], log11[1]]
L3 = [log1[2], log2[2], log3[2], log4[2], log5[2], log6[2], log7[2], log8[2], log9[2], log10[2], log11[2]]
L4 = [log1[3], log2[3], log3[3], log4[3], log5[3], log6[3], log7[3], log8[3], log9[3], log10[3], log11[3]]
L5 = [belev1, belev2, belev3, belev4, belev5, belev6, belev7, belev8, belev9, belev10, belev11]

plt.plot(x, L1, 'o-', color='black', label='Surface')
plt.plot(x, L2, color='lightcoral', label='fine-grained')
plt.fill_between(x, L1, L2, hatch='.', color='lightcoral', alpha=0.4)
plt.plot(x, L3, color='green', label='coarse-grained')
plt.fill_between(x, L2, L3, hatch='o', color='green', alpha=0.25)
plt.plot(x, L4, color='blue', label='very coarse-grained')
plt.fill_between(x, L3, L4, hatch='O', color='blue', alpha=0.1)
plt.plot(x, L5, 'o-', color='brown', label='rock-bed')
plt.fill_between(x, L4, L5, hatch='/', color='brown', alpha=0.5)
for i in range(len(x)):
    plt.vlines(x[i], L1[i]+20, L4[i]-20, colors='purple',linestyle='--')
plt.text(8, 525, 'South --->', bbox=dict(facecolor='white', alpha=0.5), fontsize = 14)
plt.title('North-South profile 2')
plt.xlabel('Distance [Mile]')
plt.ylabel('Elevation AMSL [ft]')
plt.legend(loc='best')
plt.grid(which='both', linestyle='--')
plt.show()
''' for interpolated plot '''
#inter(x, L1, L2, L3, L4, L5, 'Interpolated North-South profile 2')

#%% North-South well logs 3
#1 38.8631°N -90.0031°E 
d1 = 0
elev1 = 462.70
belev1 = 400
log1 = elev1 - np.array([0, 67, 67, 67])
#2 38.8485°N -90.001138°E 
d2 = d1 + 1.02
elev2 = 464.16
belev2 = 380
log2 = elev2 - np.array([0, 45, 45, 45])
#3 Lon: -90.0112 / Lat: 38.8125
d3 = d2 + 2.54
elev3 = 436.39 
belev3 = 325
log3 = elev3 - np.array([0, 30, 105, 109])
#4 Lon: -90.0123 / Lat: 38.7969
d4 = d3 + 1.08
elev4 = 492.48 
belev4 = 360
log4 = elev4 - np.array([0, 13, 67, 108])
#5 Lon: -90.0175 / Lat: 38.7603
d5 = d4 + 2.55 
elev5 =  424.77 
belev5 = 320
log5 = elev5 - np.array([0, 11, 65, 71])
#6 Lon: -90.0132 / Lat: 38.7310
d6 = d5 + 2.04
elev6 =  432.02 
belev6 = 300
log6 = elev6 - np.array([0, 18, 67, 100])
#7 Lon: -90.0144 / Lat: 38.6961
d7 = d6 + 2.41 
elev7 = 427.75 
belev7 = 320
log7  = elev7 - np.array([0, 34, 66, 87]) 
#8 Lon: -90.0220 / Lat: 38.6619
d8 = d7 + 2.4
elev8 = 422.58 
belev8 = 320 
log8 = elev8 - np.array([0, 28, 73, 104])
#9 Lon: -90.0224 / Lat: 38.6555
d9 = d8 + 0.44
elev9 = 426.83  
belev9 = 320
log9 = elev9 - np.array([0, 20, 33, 50])
#10 Lon: -90.0086 / Lat: 38.6002
d10 = d9 +  3.89
elev10 = 592.52 
belev10 = 360
log10 = elev10 - np.array([0, 1, 53, 58])
#11 Lon: -90.0200 / Lat: 38.5679
d11 = d10 + 2.32
elev11 =  527.48 
belev11 = 350
log11 = elev10 - np.array([0, 7, 95, 95])
#12 Lon: -90.0169 / Lat: 38.5628
d12 = d11 + 0.39
elev12 =  536.49 
belev12 = 360
log12 = elev11 - np.array([0, 14, 96, 96])
''' plotting the data '''
x = np.array([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12])
L1 = [log1[0], log2[0], log3[0], log4[0], log5[0], log6[0], log7[0], log8[0], log9[0], log10[0], log11[0], log12[0]]
L2 = [log1[1], log2[1], log3[1], log4[1], log5[1], log6[1], log7[1], log8[1], log9[1], log10[1], log11[1], log12[1]]
L3 = [log1[2], log2[2], log3[2], log4[2], log5[2], log6[2], log7[2], log8[2], log9[2], log10[2], log11[2], log12[2]]
L4 = [log1[3], log2[3], log3[3], log4[3], log5[3], log6[3], log7[3], log8[3], log9[3], log10[3], log11[3], log12[3]]
L5 = [belev1, belev2, belev3, belev4, belev5, belev6, belev7, belev8, belev9, belev10, belev11, belev12]

plt.plot(x, L1, 'o-', color='black', label='Surface')
plt.plot(x, L2, color='lightcoral', label='fine-grained')
plt.fill_between(x, L1, L2, hatch='.', color='lightcoral', alpha=0.4)
plt.plot(x, L3, color='green', label='coarse-grained')
plt.fill_between(x, L2, L3, hatch='o', color='green', alpha=0.25)
plt.plot(x, L4, color='blue', label='very coarse-grained')
plt.fill_between(x, L3, L4, hatch='O', color='blue', alpha=0.1)
plt.plot(x, L5, 'o-', color='brown', label='rock-bed')
plt.fill_between(x, L4, L5, hatch='/', color='brown', alpha=0.5)
for i in range(len(x)):
    plt.vlines(x[i], L1[i]+20, L4[i]-20, colors='purple',linestyle='--')
plt.text(8, 590, 'South --->', bbox=dict(facecolor='white', alpha=0.5), fontsize = 14)
plt.title('North-South profile 3')
plt.xlabel('Distance [Mile]')
plt.ylabel('Elevation AMSL [ft]')
plt.legend(loc='best')
plt.grid(which='both', linestyle='-')
plt.show()
''' for interpolated plot '''
#inter(x, L1, L2, L3, L4, L5, 'Interpolated North-South profile 3')
#%% East-West well logs 1
#lat 38.79507 long -89.936776
d1 = 0
elev1 = 544.69  
belev1 = 400
log1 = elev1 - np.array([0, 47, 47, 47])
# lat 38.780996 long -89.992784
d2 = d1 + 3.17
elev2 = 558.92 
belev2 = 370
log2 = elev2 - np.array([0, 65, 65, 65])
# lat 38.781611 long -90.025417 ( not correct )
d3 = d2 + 1.76
elev3 =  427.98 
belev3 = 315
log3 = elev3 - np.array([0, 30, 105, 109])
#lat 38.793222 long -90.042076
d4 = d3 + 1.2
elev4 = 440.76
belev4 = 310
log4 = elev4 - np.array([0, 55, 112, 114])
# lat 38.795661 long -90.072879
d5 = d4 + 1.67 
elev5 = 424.13   
belev5 = 280
log5 = elev5 - np.array([0, 24, 64, 76])
#lat 38.798891 long -90.104544
d6 = d5 + 1.72
elev6 = 430.26 
belev6 = 300
log6 = elev6 - np.array([0, 55, 72, 100])
# lat 38.790515 long -90.126005
d7 = d6 + 1.29 
elev7 = 419.42 
belev7 = 320
log7  = elev7 - np.array([0, 22, 47, 83]) 
# lat 38.775139 long -90.151185
d8 = d7 + 1.72
elev8 = 423.27  
belev8 = 305
log8 = elev8 - np.array([0, 21, 96, 114])

''' plotting the data '''
x = np.array([d1, d2, d3, d4, d5, d6, d7, d8])
L1 = [log1[0], log2[0], log3[0], log4[0], log5[0], log6[0], log7[0], log8[0]]
L2 = [log1[1], log2[1], log3[1], log4[1], log5[1], log6[1], log7[1], log8[1]]
L3 = [log1[2], log2[2], log3[2], log4[2], log5[2], log6[2], log7[2], log8[2]]
L4 = [log1[3], log2[3], log3[3], log4[3], log5[3], log6[3], log7[3], log8[3]]
L5 = [belev1, belev2, belev3, belev4, belev5, belev6, belev7, belev8]

plt.plot(x, L1, 'o-', color='black', label='Surface')
plt.plot(x, L2, color='lightcoral', label='fine-grained')
plt.fill_between(x, L1, L2, hatch='.', color='lightcoral', alpha=0.4)
plt.plot(x, L3, color='green', label='coarse-grained')
plt.fill_between(x, L2, L3, hatch='o', color='green', alpha=0.25)
plt.plot(x, L4, color='blue', label='very coarse-grained')
plt.fill_between(x, L3, L4, hatch='O', color='blue', alpha=0.1)
plt.plot(x, L5, 'o-', color='brown', label='rock-bed')
plt.fill_between(x, L4, L5, hatch='/', color='brown', alpha=0.5)
for i in range(len(x)):
    plt.vlines(x[i], L1[i]+20, L4[i]-20, colors='purple',linestyle='--')
plt.title('East-West profile 1')
plt.xlabel('Distance [Mile]')
plt.ylabel('Elevation AMSL [ft]')
plt.text(4.5, 565, 'West --->', bbox=dict(facecolor='white', alpha=0.5), fontsize = 14)
plt.legend(loc='best')
plt.grid(which='both', linestyle='-')
plt.show()
''' for interpolated plot '''
#inter(x, L1, L2, L3, L4, L5, 'Interpolated East-West profile 1')

#%% East-West well logs 2
#1 Lon: -89.9412 / Lat: 38.6989
d1 = 0
elev1 = 530.57   
belev1 = 400 
log1 = elev1 - np.array([0, 66, 66, 66])
#2 Lon: -89.9850 / Lat: 38.6987
d2 = d1 + 2.36
elev2 = 495.70  
belev2 = 360
log2 = elev2 - np.array([0, 55, 55, 55])
#3 Lon: -90.0299 / Lat: 38.6919
d3 = d2 + 2.47
elev3 = 435.77 
belev3 = 280
log3 = elev3 - np.array([0, 37, 50, 90])
#4 Lon: -90.0477 / Lat: 38.7001
d4 = d3 + 1.11
elev4 = 417.86 
belev4 = 300
log4 = elev4 - np.array([0, 75, 93, 104])
#5 Lon: -90.1278 / Lat: 38.6958
d5 = d4 + 4.33
elev5 = 415.77  
belev5 = 310
log5 = elev5 - np.array([0, 55, 70, 106])
#6 Lon: -90.1430 / Lat: 38.6965
d6 = d5 +  0.82
elev6 = 415.98 
belev6 = 315
log6 = elev6 - np.array([0, 75, 80, 102])
#7 Lon: -90.1610 / Lat: 38.6990
d7 = d6 + 0.99 
elev7 =  421.91 
belev7 = 305
log7  = elev7 - np.array([0, 60, 87, 114]) 
#8 Lon: -90.1794 / Lat: 38.6956
d8 = d7 + 1.02 
elev8 = 414.39 
belev8 = 340
log8 = elev8 - np.array([0, 35, 69, 73])

''' plotting the data '''
x = np.array([d1, d2, d3, d4, d5, d6, d7, d8])
L1 = [log1[0], log2[0], log3[0], log4[0], log5[0], log6[0], log7[0], log8[0]]
L2 = [log1[1], log2[1], log3[1], log4[1], log5[1], log6[1], log7[1], log8[1]]
L3 = [log1[2], log2[2], log3[2], log4[2], log5[2], log6[2], log7[2], log8[2]]
L4 = [log1[3], log2[3], log3[3], log4[3], log5[3], log6[3], log7[3], log8[3]]
L5 = [belev1, belev2, belev3, belev4, belev5, belev6, belev7, belev8]

plt.plot(x, L1, 'o-', color='black', label='Surface')
plt.plot(x, L2, color='lightcoral', label='fine-grained')
plt.fill_between(x, L1, L2, hatch='.', color='lightcoral', alpha=0.4)
plt.plot(x, L3, color='green', label='coarse-grained')
plt.fill_between(x, L2, L3, hatch='o', color='green', alpha=0.25)
plt.plot(x, L4, color='blue', label='very coarse-grained')
plt.fill_between(x, L3, L4, hatch='O', color='blue', alpha=0.1)
plt.plot(x, L5, 'o-', color='brown', label='rock-bed')
plt.fill_between(x, L4, L5, hatch='/', color='brown', alpha=0.5)
for i in range(len(x)):
    plt.vlines(x[i], L1[i]+20, L4[i]-20, colors='purple',linestyle='--')
plt.title('East-West profile 2')
plt.xlabel('Distance [Mile]')
plt.ylabel('Elevation AMSL [ft]')
plt.text(4.5, 525, 'West --->', bbox=dict(facecolor='white', alpha=0.5), fontsize = 14)
plt.legend(loc='best')
plt.grid(which='both', linestyle='-')
plt.show()
''' for interpolated plot '''
#inter(x, L1, L2, L3, L4, L5, 'Interpolated East-West profile 2')
#%% East-West well logs 3
#1 Lon: -89.9535 / Lat: 38.6369
d1 = 0
elev1 = 590.55 
belev1 = 400 
log1 = elev1 - np.array([0, 57, 57, 57])
#2 Lon: -89.9740 / Lat: 38.6287
d2 = d1 + 1.24
elev2 = 581.79   
belev2 = 360
log2 = elev2 - np.array([0, 150, 150, 150])
#3 Lon: -90.0254 / Lat: 38.6416
d3 = d2 + 2.91
elev3 = 434.87 
belev3 = 320
log3 = elev3 - np.array([0, 52, 88, 98])
#4 Lon: -90.0474 / Lat: 38.6443
d4 = d3 + 1.2
elev4 = 416.74  
belev4 = 300
log4 = elev4 - np.array([0, 40, 70, 84])
#5 Lon: -90.0920 / Lat: 38.6458
d5 = d4 + 2.41
elev5 = 424.21 
belev5 = 280
log5 = elev5 - np.array([0, 22, 90, 115])
#Lat 38.638694 long -90.140724
d6 = d5 + 2.67 
elev6 =  417.83 
belev6 = 280
log6 = elev6 - np.array([0, 32, 91, 115])
#lat 38.642995 long -90.157691
d7 = d6 + 0.96 
elev7 = 410.06   
belev7 = 305
log7  = elev7 - np.array([0, 30, 75, 97]) 
#lat 38.645833 long -90.17
d8 = d7 + 0.69 
elev8 =  423.61 
belev8 = 315
log8 = elev8 - np.array([0, 48, 71, 79])


''' plotting the data '''
x = np.array([d1, d2, d3, d4, d5, d6, d7, d8])
L1 = [log1[0], log2[0], log3[0], log4[0], log5[0], log6[0], log7[0], log8[0]]
L2 = [log1[1], log2[1], log3[1], log4[1], log5[1], log6[1], log7[1], log8[1]]
L3 = [log1[2], log2[2], log3[2], log4[2], log5[2], log6[2], log7[2], log8[2]]
L4 = [log1[3], log2[3], log3[3], log4[3], log5[3], log6[3], log7[3], log8[3]]
L5 = [belev1, belev2, belev3, belev4, belev5, belev6, belev7, belev8]

plt.plot(x, L1, 'o-', color='black', label='Surface')
plt.plot(x, L2, color='lightcoral', label='fine-grained')
plt.fill_between(x, L1, L2, hatch='.', color='lightcoral', alpha=0.4)
plt.plot(x, L3, color='green', label='coarse-grained')
plt.fill_between(x, L2, L3, hatch='o', color='green', alpha=0.25)
plt.plot(x, L4, color='blue', label='very coarse-grained')
plt.fill_between(x, L3, L4, hatch='O', color='blue', alpha=0.1)
plt.plot(x, L5, 'o-', color='brown', label='rock-bed')
plt.fill_between(x, L4, L5, hatch='/', color='brown', alpha=0.5)
for i in range(len(x)):
    plt.vlines(x[i], L1[i]+20, L4[i]-20, colors='purple',linestyle='--')
plt.title('East-West profile 3')
plt.xlabel('Distance [Mile]')
plt.ylabel('Elevation AMSL [ft]')
plt.text(4.5, 565, 'West --->', bbox=dict(facecolor='white', alpha=0.5), fontsize = 14)
plt.legend(loc='best')
plt.grid(which='both', linestyle='-')
plt.show()
''' for interpolated plot '''
#inter(x, L1, L2, L3, L4, L5, 'Interpolated East-West profile 3')







