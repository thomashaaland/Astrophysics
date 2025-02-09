from scitools.std import *
from scipy import *

#Calculation loop stuff
t_max = 10**5
dt = 1
n= t_max/dt
t = linspace(0,t_max,n+1)
G = 6.67*10**(-11) # Gravitational constant
k = 0.00016 #friction coefficient

#Mars
r_m = [[0., 0.]] #Starting position mars
m_m = 6.4*10**23 #Mars mass
v_m = [[0., 0.]] #initial velocity
a_m = [] #initial acceleration

#Lander
r_r = [[(-298-3400)*1000., 0]] #Starting position lander
m_r = 100. #Mars lander mass
v_r = [[0., -4000.]] #initial velocity
a_r = [] #initial acceleration

#Forces

def F(r_m, r_r,i): #Gravitational forces pointing from rover to mars
    F   =  G*(m_m*m_r)/sqrt((r_m[i][0]-r_r[i][0])**2+(r_m[i][1]-r_r[i][1])**2)**3
    F_x =  F*(r_m[i][0]-r_r[i][0])
    F_y =  F*(r_m[i][1]-r_r[i][1])
    return [F_x, F_y]

def f(v_r, v_m, i): #Friction, calculates friction based on relative speed between rover and mars
    f_x = -k*(v_r[i][0]-v_m[i][0])
    f_y = -k*(v_r[i][1]-v_m[i][1])
    return [f_x, f_y]

#Integration loop
def Integration(v,r):
    i = 0
    while sqrt((r_m[i][0]-r_r[i][0])**2+(r_m[i][1]-r_r[i][1])**2) >= 3400000.:
        a_m.append([(-F(r_m, r_r, i)[0]-f(v_r,v_m,i)[0])/m_m, (-F(r_m, r_r, i)[1]-f(v_r,v_m,i)[1])/m_m])
        v_m.append([v_m[i][0]+a_m[i][0]*dt, v_m[i][1]+a_m[i][1]*dt])
        r_m.append([r_m[i][0]+v_m[i+1][0]*dt, r_m[i][1]+v_m[i+1][1]*dt])

        a_r.append([(F(r_m, r_r, i)[0]+f(v_r,v_m,i)[0])/m_r, (F(r_m, r_r, i)[1]+f(v_r,v_m,i)[1])/m_r])
        v_r.append([v_r[i][0]+a_r[i][0]*dt, v_r[i][1]+a_r[i][1]*dt])
        r_r.append([r_r[i][0]+v_r[i+1][0]*dt, r_r[i][1]+v_r[i+1][1]*dt])
        i = i+1
    return i
    
a=Integration(v_m,r_m)

r_r_x = []
r_r_y = []
r_m_x = []
r_m_y = []
for i in range(0,a):
    r_r_x.append(r_r[i][0])
    r_r_y.append(r_r[i][1])
    r_m_x.append(r_m[i][0])
    r_m_y.append(r_m[i][1])
r_R = [r_r_x, r_r_y]
r_M = [r_m_x, r_m_y]


plot(r_R[0],r_R[1])
hold("on")
plot(r_M[0],r_M[1],'o')
theta=linspace(0,2*pi,101)
plot(3400000*cos(theta),3400000*sin(theta))
title('Mars Express Landing')
xlabel('meters [m]')
ylabel('meters [m]')
plot([r_R[0][i]],[r_R[1][i]],'xk')
