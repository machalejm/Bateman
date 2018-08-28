import numpy as np
from math import exp
from math import log
import matplotlib.pyplot as plt
import Utility as ut


lam = (0.4468,0.6,0.7,0.00000754,0.00000016,330350.4,0.035,0.0001643,0.00000000222,433036.8,11955686.4)
N=len(lam)+1
lam =np.log(2)/lam
# lam = (1.2,0.2,0.3,0.4,0.5,0.51,0.7,0.8,0.9,1,1.1)
assert(len(lam)==N-1)
pop0s = np.zeros(N)
pop0s[0] = 1

#print("Activity".ljust(14),"Half-Life".ljust(25),"Initial Population".ljust(20), sep="")
#for i in range(0, len(lam)):
#    print(str(lam[i]).ljust(14),str(log(2)/lam[i]).ljust(25),str(pop0s[i]).ljust(20),sep="",end="\n")
#print()

def pop(n, t):
    if n!=N-1:
        resi = 0 
        for i in range(n+1):
            resj = 0
            for j in range(i,n+1):
                resk = 1
                for k in range(i,n+1):
                    if(k!=j): resk *= 1/(1-lam[j]/lam[k])
                resj += lam[j]*exp(-lam[j]*t) * resk
            resi += pop0s[i]*resj
        return resi / lam[n]
    else:
        resi = 0 
        for i in range(n+1):
            resj = 0
            for j in range(i,n):
                resk = 1
                for k in range(i,n):
                    if(k!=j): resk *= 1/(1-lam[j]/lam[k])
                resj += (1-exp(-lam[j]*t)) * resk
            resi += pop0s[i]*resj
        return pop0s[n] + resi

#print("Population of nuclide 1 after 1 half life is: ", pop(0,log(2)/lam[0]))

fig = plt.figure()
ax = fig.add_subplot(111)

STEP=100
times = np.linspace(0,10,STEP)
pops = np.zeros((N,STEP))
for i in range(N):
    for j in range(STEP):
        pops[i,j] = pop(i,times[j])
    ax.plot(times, pops[i,:], label = "Nuclide " + str(i+1))
ax.legend()
plt.show()
