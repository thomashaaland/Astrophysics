from scitools.all import *
from random import uniform, gauss
import numpy as np

#constants
n = 10**7 #number of particles
n_v = n/(0.1)**3
k = 1.38065*10**(-23) # Boltzmann constant
T = [6000, 50000, 15*10**6,10**9] # Temperature [K]
m = 1.67372*10**(-27) # electron mass [kg]
dt = 10**(-9)

def loop(T):
    sigma = sqrt(k*T/m)
    hits = []
    F = []

    x = np.random.rand(n,3)*0.1
    v = np.random.randn(n,3)*sigma
    
    for i in range(0,n):
    #Forward timestep:
        x_f = x[i]+v[i]*dt
        if x_f[0] > 0.1:
            hits.append(i)
            f = m*v[i][0]/float(dt)
            F.append(f)
    #Backward timestep:
        x_b = x[i]-v[i]*dt
        if x_b[0] > 0.1:
            hits.append(i)
            f = -m*v[i][0]/float(dt)
            F.append(f)

    return sum(F)

P1 = loop(T[0])/(0.1)**2
P2 = loop(T[1])/(0.1)**2
P3 = loop(T[2])/(0.1)**2
P4 = loop(T[3])/(0.1)**2

P_a = n_v*k*linspace(6000, 10**9, 1001)

loglog(linspace(6000, 10**9, 1001),P_a, 'b')
hold('on')
loglog(T, [P1,P2,P3,P4], 'ro')
xlabel('Temperature [K]')
ylabel('Pressure [N/A]')
