# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:43:55 2017

@author: 王乎
"""

import math
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


dt=0.0001
sigma=10
lb=8/3

class Z:
    def __init__(self, _r):
        self.r = _r
        
    def z(self):
        x=[1]
        y=[0]
        z=[0]
        dxdt=[0]
        dydt=[0]
        dzdt=[0]
        t=[0]
        
        x0 = []
        z0 = []
        
        y1 = []
        z1 = []
        
        for i in range(1999999):
            dxdt.append( sigma * ( y[-1] - x[-1] ))
            dydt.append( -x[-1] * z[-1] + self.r * x[-1] - y[-1])
            dzdt.append( x[-1] * y[-1] - lb * z[-1])
            
            x.append( x[-1] + dxdt[-1] * dt)
            y.append( y[-1] + dydt[-1] * dt)
            z.append( z[-1] + dzdt[-1] * dt)
            t.append( t[-1] + dt)
            '''
            if t[-1]>30:
                if abs(y[-1])<0.01:
                    x0.append(x[-1])
                    z0.append(z[-1])
                if abs(x[-1])<0.01:
                    y1.append(y[-1])
                    z1.append(z[-1])
        return x0,z0,y1,z1
'''
        return x,y,z
        #return t,z
 

#Work One
'''
a = Z(5)
ta,za = a.z()
b = Z(10)
tb,zb = b.z()
c = Z(25)
tc,zc = c.z()

fig, ax = plt.subplots()
ax.plot(ta,za,label = r'r = 5',color = 'cyan')
ax.plot(tb,zb,'k--',label = r'r = 10',color = 'tomato')
ax.plot(tc,zc,label = r'r = 25',color = 'green')
ax.set_xlabel(r'time')
ax.set_ylabel(r'Z')
ax.set_title(r'Lorenz model   Z versus time')
legend = ax.legend(loc='upper right')

fig.show()
'''

#Work two

a = Z(25)
xa,ya,za = a.z()
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xa,ya,za,color = 'c',linewidth=0.5)

ax.set_xlabel(r'X')
ax.set_ylabel(r'Y')
ax.set_zlabel(r'Z')
ax.set_title(r'Phase space plot: z versus x')
legend = ax.legend(loc='upper right')
fig.set_size_inches(18.5, 10.5)
fig.savefig('wewee.png', dpi=300)
fig.show()   


#Work Three
'''
a = Z(25)
xa,ya,za = a.z()
fig = plt.figure()
#ax = fig.gca(projection='3d')
ax = Axes3D(fig)
plt.xlim((-20, 20))
plt.ylim((-20, 20))
ax.set_zlim3d(0,40)
i = 1
while i<= 500000:
    xa1 = xa[0:i]
    ya1 = ya[0:i]
    za1 = za[0:i]
    ax.plot(xa1,ya1,za1,color = 'c',linewidth=0.5)

    fig.set_size_inches(18.5, 10.5)
    fig.savefig('w%s.png'%i, dpi=100)
    
    i = i+4999
'''
#work four
'''
c = Z(25)
xc0,zc0,yc1, zc1 = c.z()

fig = plt.figure()

ax1 = fig.add_subplot(141)
ax1.scatter(xc0,zc0,color = 'green',s = 0.1)
ax1.set_xlabel(r'Y')
ax1.set_ylabel(r'Z')
ax1.set_xlim = (-20,20)
ax1.set_title(r'Phase space plot: z versus x when y = 0')
legend = ax1.legend(loc='upper right')

ax2 = fig.add_subplot(144)
ax2.scatter(yc1,zc1,color = 'red', s = 0.1)
ax2.set_xlabel(r'X')
ax2.set_ylabel(r'Z')
ax2.set_xlim = (-20,20)
ax2.set_title(r'Phase space plot: z versus when x = 0')
legend = ax2.legend(loc='upper right')

plt.savefig('babaa.png',dpi = 300)
fig.show()
'''
#work five
'''
a = Z(160)
ta,za = a.z()
b = Z(166)
tb,zb = b.z()
c = Z(200)
tc,zc = c.z()

fig = plt.figure()
fig.set_size_inches(20, 12)

ax1 = fig.add_subplot(511)
ax1.plot(ta,za,label = r'r = 160',color = 'cyan',lw = 0.5)
ax1.set_xlabel(r'time')
ax1.set_ylabel(r'Z')
legend = plt.legend(loc='upper right')

ax2 = fig.add_subplot(513)
ax2.plot(tb,zb,label = r'r = 166',color = 'tomato',lw = 0.5)
ax2.set_xlabel(r'time')
ax2.set_ylabel(r'Z')
legend = plt.legend(loc='upper right')

ax3 = fig.add_subplot(515)
ax3.plot(tc,zc,label = r'r = 200',color = 'green',lw = 0.5)
ax3.set_xlabel(r'time')
ax3.set_ylabel(r'Z')
legend = plt.legend(loc='upper right')


plt.savefig('yue.png',dpi = 300)
fig.show()
'''










