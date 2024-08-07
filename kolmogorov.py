import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib import ticker
import statistics as st

eleccoeff=[[],[]]
muoncoeff=[[],[]]
with open("/Users/lukecalvin/2023/eli_np_muon_primaries_1.0GeV/elec coeffsave.txt", "r") as txt_file1:
    for line in txt_file1:
        line.split()
        eleccoeff[0].append(line[0])
        eleccoeff[1].append(line[1])

print(eleccoeff)