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
#print(eleccoeff)
for i in range(0,len(eleccoeff[1])):
    for j in range(0,int(eleccoeff[1][i])):
        x.append(eleccoeff[0][i])

print(muoncoeff)
for i in range(0,len(muoncoeff[1])):
    print(i)
    for j in range(0,int(muoncoeff[1][i])):
        print(j)
        
        y.append(muoncoeff[0][i])
        print(muoncoeff[0][i])
#print(y)




np.random.seed(12345678)
test = np.random.normal(0, 1, 1000)


newx=[]

for i in range(0,len(x)):

    newx.append(x[i]/sum(x)) 

newy=[]

for i in range(0,len(y)):

    newy.append(y[i]/sum(y)) 


#print(test)

print('coeff: ',ks_2samp(newx, newy))
#Ks_2sampResult(statistic=0.022999999999999909, pvalue=0.95189016804849647)
#Ks_2sampResult(statistic=0.41800000000000004, pvalue=3.7081494119242173e-77)

elecmean=[[],[]]
muonmean=[[],[]]
e=[]
f=[]
with open("/Users/lukecalvin/2023/eli_np_muon_primaries_1.0GeV/elecmeansave.csv", "r") as txt_file7:
    for line in txt_file7:
        
        elecmean[0].append(float(line.split()[0]))
        elecmean[1].append(float(line.split()[1]))


#print(eleccoeff)

with open("/Users/lukecalvin/2023/eli_np_muon_primaries_1.0GeV/muonmeansave.csv", "r") as txt_file8:
    for line in txt_file8:
        
        muonmean[0].append(float(line.split()[0]))
        muonmean[1].append(float(line.split()[1]))


#print(muoncoeff)

for i in range(0,len(elecmean[1])):
    for j in range(0,int(elecmean[1][i])):
        
        e.append(elecmean[0][i])


for i in range(0,len(muonmean[1])):
    for j in range(0,int(muonmean[1][i])):
        
        f.append(muonmean[0][i])
#print(y)




np.random.seed(12345678)
test = np.random.normal(0, 1, 1000)


#print(x)
#print(test)


newe=[]

for i in range(0,len(e)):

    newe.append(e[i]/sum(e)) 

newf=[]

for i in range(0,len(f)):

    newf.append(f[i]/sum(f)) 


#print(test)

print('mean: ',ks_2samp(newe, newf))

#Ks_2sampResult(statistic=0.022999999999999909, pvalue=0.95189016804849647)
#Ks_2sampResult(statistic=0.41800000000000004, pvalue=3.7081494119242173e-77)

elecmode=[[],[]]
muonmode=[[],[]]
c=[]
d=[]
with open("/Users/lukecalvin/2023/eli_np_muon_primaries_1.0GeV/elecmodesave.csv", "r") as txt_file5:
    for line in txt_file5:
        
        elecmode[0].append(float(line.split()[0]))
        elecmode[1].append(float(line.split()[1]))


#print(eleccoeff)

with open("/Users/lukecalvin/2023/eli_np_muon_primaries_1.0GeV/muonmodesave.csv", "r") as txt_file6:
    for line in txt_file6:
        
        muonmode[0].append(float(line.split()[0]))
        muonmode[1].append(float(line.split()[1]))


#print(muoncoeff)

for i in range(0,len(elecmode[1])):
    for j in range(0,int(elecmode[1][i])):
        
        c.append(elecmode[0][i])


for i in range(0,len(muonmode[1])):
    for j in range(0,int(muonmode[1][i])):
        
        d.append(muonmode[0][i])
#print(y)




np.random.seed(12345678)
test = np.random.normal(0, 1, 1000)


#print(x)
#print(test)

newc=[]

for i in range(0,len(c)):

    newc.append(c[i]/sum(c)) 

newd=[]

for i in range(0,len(d)):

    newd.append(d[i]/sum(d)) 


#print(test)

print('mode: ',ks_2samp(newc, newd))


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


newa=[]

for i in range(0,len(a)):

    newa.append(a[i]/sum(a)) 

newb=[]

for i in range(0,len(b)):

    newb.append(b[i]/sum(b)) 


#print(test)

print('track: ',ks_2samp(newa, newb))


