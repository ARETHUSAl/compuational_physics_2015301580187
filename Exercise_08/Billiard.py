# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:26:10 2017

@author: 王乎
"""

import numpy
import matplotlib.pyplot as plt

dt = 0.01

class YX:
    def __init__(self, _alpha):
        self.alpha = _alpha
        
    def move(self):
        alpha = self.alpha
        vtho = numpy.sqrt(2)
        vthe=[numpy.pi/4]
        vx=[vtho*numpy.cos(vthe[-1])]
        vy=[vtho*numpy.sin(vthe[-1])]
        
        x=[1]
        y=[0]
        the=[0]
        t=[0]
        xp  = []
        vxp = []
        while t[-1]<10000:
            if -alpha*20<=x[-1]<=alpha*20:
                if y[-1]>20 or y[-1]<-20:
                    vy.append(-vy[-1])
                    vx.append(vx[-1])
                    vthe.append(numpy.arctan(float(vy[-1]/vx[-1])))
                else:
                    vx.append(vx[-1])
                    vy.append(vy[-1])
                    vthe.append(vthe[-1])
    
            if x[-1]>alpha*20:
                if y[-1]**2+(x[-1]-alpha*20)**2>=400:
                    thee=numpy.arctan(float(y[-1]/(x[-1]-alpha*20)))
                    vthe.append(numpy.pi-vthe[-1]+2*thee)
                    vx.append(vtho * numpy.cos(vthe[-1]))
                    vy.append(vtho * numpy.sin(vthe[-1]))
                else:
                    vx.append(vx[-1])
                    vy.append(vy[-1])
                    vthe.append(vthe[-1])
    
            if x[-1]<-alpha*20:
                if y[-1]**2+(x[-1]+alpha*20)**2>=400:
                    thee=numpy.arctan(float(y[-1]/(x[-1]+alpha*20)))
                    vthe.append(numpy.pi - vthe[-1]+2*thee)
                    vx.append(vtho*numpy.cos(vthe[-1]))
                    vy.append(vtho*numpy.sin(vthe[-1]))
                else:
                    vx.append(vx[-1])
                    vy.append(vy[-1])
                    vthe.append(vthe[-1])
    
            x.append(x[-1]+vx[-1]*dt)
            y.append(y[-1]+vy[-1]*dt)
            the.append(numpy.arctan(y[-1]/x[-1]))
            t.append(t[-1]+dt)
            
            '''
            if abs(y[-1])<=0.01:
                xp.append(x[-1])
                vxp.append(vx[-1])
            '''
        return x, y
        #return xp,vxp
    
    
#work one 

a = YX(20) 
axa,aya = a.move()

fig, ax = plt.subplots()
ax.set_title(r'Circular stadium - trajectory')
ax.set_xlabel(r'x')
ax.set_ylabel(r'y')
'''
plt.xlim((-20, 20))
plt.ylim((-20, 20))
'''

ax.plot(axa,aya,color = 'c', linewidth=0.5)
'''


i = 1
while i <= 200002:
    axas = axa[0:i]
    ayas = aya[0:i]
    ax.plot(axas,ayas,color = 'c', linewidth=0.5)
    
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('P%s.png'%i, dpi=100)
    i = i + 1999
'''
fig.savefig('Stadium a = %s.png'%a.alpha, dpi=300)
fig.show()

#work two
'''
a = YX(0.5) 
axpa,avxpa = a.move()
fig, ax = plt.subplots()
ax.set_title(r'Stadium Billiar a = %s'%a.alpha)
ax.set_xlabel(r'x')
ax.set_ylabel(r'$V_x$')

ax.scatter(axpa,avxpa ,color = 'c',s = 0.3)
fig.savefig('Stadium Billiar a = %s.png'%a.alpha, dpi=300)
fig.show()
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
