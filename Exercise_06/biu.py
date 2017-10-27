# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:28:36 2017

@author: 王乎
"""

import math
from matplotlib import pyplot



def change_amp(theta0):

    q = 0.5
    l = 9.8
    g = 9.8
    f = float(2/3)
    dt = 0.04
    #dt = math.pi / 100
    #theta0 = 0.2
    omega0 = 0
    angle = [theta0]
    avelo = [omega0]
    t = [0]
    F = 1.2
    #an = []
    #av = []
    for i in range(5000):
        
        avelo_new = avelo[-1] - ((g/l)*math.sin(angle[-1]) + q*avelo[-1] - F*math.sin(f*t[-1]))*dt
        avelo.append(avelo_new)
        
        angle_new = angle[-1] + avelo[-1]*dt
        '''
        while angle_new > math.pi:
            angle_new -= 2*math.pi
        while angle_new < -math.pi:
            angle_new += 2*math.pi
        '''
        angle.append(angle_new)
        '''
        if t[-1]%(3*math.pi) <= dt:
        if (t[-1]-(3*math.pi)/8)%(3*math.pi) <= dt:
            an.append(angle_new)
            av.append(avelo_new)
        '''
        t_new = t[-1] + dt
        t.append(t_new)

    return angle,avelo,t
    #return an,av


fig,ax = pyplot.subplots()
#one
'''
#for i in [0,0.5,1.2]:
for i in [1.2]:
    angle_0 = change_amp(i)[0]
    avelo_0 = change_amp(i)[1]
    t_0     = change_amp(i)[2]
    
    ax.set_xlabel(r'time(s)', fontsize=14)
    ax.set_ylabel(r'$\theta(radians)$', fontsize=14)
    ax.set_title(r'$\theta$ versus time')
    
    pyplot.plot(t_0,angle_0,label='FD=%s'%i)
'''
#two

angle1 =  change_amp(0)[0]  
angle2 =  change_amp(0.01)[0]
dangle = list(map(lambda x: abs(x[0]-x[1]), zip(angle1, angle2)))
t = change_amp(0)[2]
pyplot.plot(t,dangle,label = '$F_D = 1.2$')
pyplot.yscale('log')
ax.set_xlabel(r'time(s)', fontsize=14)
ax.set_ylabel(r'$\Delta \theta(radians)$', fontsize=14)
ax.set_title(r'$\Delta \theta(radians)$ versus time')

'''
#three
angle1 = change_amp()[0]
avelo1 = change_amp()[1]
#pyplot.plot(angle1,avelo1)
pyplot.scatter(angle1,avelo1,s=1)
ax.set_xlabel(r'$\theta(radians)$', fontsize=14)
ax.set_ylabel(r'$\omega(radians/s)$', fontsize=14)
ax.set_title(r'$\omega$ versus $\theta$   $F_D = 1.2$')
'''
pyplot.legend(loc='upper right')
pyplot.show()