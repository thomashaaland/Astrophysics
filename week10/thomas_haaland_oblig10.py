from scitools.all import *
from random import gauss

# constants
n = 100000
k = 1.38065*10**(-23) # Boltzmann constant
T = 6000. # Temperature [K]
m = 1.67372*10**(-27) #kg

sigma = sqrt(k*T/m)

v = list(zeros(n))
K = list(zeros(n))

for i in range(0,n):
    v_x = gauss(0,sigma); v_y = gauss(0,sigma); v_z = gauss(0,sigma)
    v[i] = array([v_x,v_y,v_z])
    K[i] = 0.5*m*dot(v[i],v[i])

K = sum(K)/n
print 'Numerical solution is', K

#Analytical result:

K_a = 3/2.*k*T
print 'Analytical solution is', K_a
