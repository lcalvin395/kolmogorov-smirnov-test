import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ks_2samp


import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib import ticker
import statistics as st

eleccoeff=[[],[]]
muoncoeff=[[],[]]
x=[]
y=[]
with open("/Users/lukecalvin/2023/eli_np_muon_primaries_1.0GeV/eleccoeffsave.csv", "r") as txt_file1:
    for line in txt_file1:
        
        eleccoeff[0].append(float(line.split()[0]))
        eleccoeff[1].append(float(line.split()[1]))


#print(eleccoeff)

with open("/Users/lukecalvin/2023/eli_np_muon_primaries_1.0GeV/muoncoeffsave.csv", "r") as txt_file2:
    for line in txt_file2:
        
        muoncoeff[0].append(float(line.split()[0]))
        muoncoeff[1].append(float(line.split()[1]))


#print(muoncoeff)

for i in range(0,len(eleccoeff[1])):
    for j in range(0,int(eleccoeff[1][i])):
        
        x.append(eleccoeff[0][i])


for i in range(0,len(muoncoeff[1])):
    for j in range(0,int(muoncoeff[1][i])):
        
        y.append(muoncoeff[0][i])
#print(y)




np.random.seed(12345678)
test = np.random.normal(0, 1, 1000)


#print(x)
#print(test)

print('coeff: ',ks_2samp(x, y))
#Ks_2sampResult(statistic=0.022999999999999909, pvalue=0.95189016804849647)
#Ks_2sampResult(statistic=0.41800000000000004, pvalue=3.7081494119242173e-77)


electrack=[[],[]]
muontrack=[[],[]]
a=[]
b=[]
with open("/Users/lukecalvin/2023/eli_np_muon_primaries_1.0GeV/electracksave.csv", "r") as txt_file3:
    for line in txt_file3:
        
        electrack[0].append(float(line.split()[0]))
        electrack[1].append(float(line.split()[1]))


#print(electrack)

with open("/Users/lukecalvin/2023/eli_np_muon_primaries_1.0GeV/muontracksave.csv", "r") as txt_file4:
    for line in txt_file4:
        
        muontrack[0].append(float(line.split()[0]))
        muontrack[1].append(float(line.split()[1]))


#print(muontrack)

for i in range(0,len(electrack[1])):
    for j in range(0,int(electrack[1][i])):
        
        a.append(electrack[0][i])


for i in range(0,len(muontrack[1])):
    for j in range(0,int(muontrack[1][i])):
        
        b.append(muontrack[0][i])
#print(y)




np.random.seed(12345678)
test = np.random.normal(0, 1, 1000)


#print(x)
#print(test)

print('track: ',ks_2samp(x, y))