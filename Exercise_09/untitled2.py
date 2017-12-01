# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:19:41 2017

@author: 王乎
"""

import math
import matplotlib.pyplot as plt

# set the mass of sun, jupiter and earth

gms=4*(math.pi)**2
gmj=1*gms
gme=gms*(1/330000)



xe=[1]
ye=[0]
xs=[0]
ys=[0]
xj=[5.2]
yj=[0]

vxe=[0]
vye=[2*math.pi]
vxj=[0]
vyj=[math.sqrt(gms/5.2)]
vxs=[0]
vys=[-math.sqrt(gms/5.2)]


dt=0.001
t=[0]

while t[-1]<=120:

    res=math.sqrt((xe[-1]-xs[-1])**2+(ye[-1]-ys[-1])**2)
    rej=math.sqrt((xe[-1]-xj[-1])**2+(ye[-1]-yj[-1])**2)
    rjs=math.sqrt((xj[-1]-xs[-1])**2+(yj[-1]-ys[-1])**2)
    
    vxe_new=vxe[-1]-gms*(xe[-1]-xs[-1])*dt/res**3-gmj*(xe[-1]-xj[-1])*dt/rej**3
    vye_new=vye[-1]-gms*(ye[-1]-ys[-1])*dt/res**3-gmj*(ye[-1]-yj[-1])*dt/rej**3

    vxj_new=vxj[-1]-gms*(xj[-1]-xs[-1])*dt/rjs**3-gme*(xj[-1]-xe[-1])*dt/rej**3
    vyj_new=vyj[-1]-gms*(yj[-1]-ys[-1])*dt/rjs**3-gme*(yj[-1]-ye[-1])*dt/rej**3

    vxs_new=vxs[-1]-gmj*(xs[-1]-xj[-1])*dt/rjs**3-gme*(xs[-1]-xe[-1])*dt/res**3
    vys_new=vys[-1]-gmj*(ys[-1]-yj[-1])*dt/rjs**3-gme*(ys[-1]-ye[-1])*dt/res**3

    vxe.append(vxe_new)
    vye.append(vye_new)
    vxj.append(vxj_new)
    vyj.append(vyj_new)
    vxs.append(vxs_new)
    vys.append(vys_new)

    xe.append(xe[-1]+vxe[-1]*dt)
    ye.append(ye[-1]+vye[-1]*dt)
    xj.append(xj[-1]+vxj[-1]*dt)
    yj.append(yj[-1]+vyj[-1]*dt)
    xs.append(xs[-1]+vxs[-1]*dt)
    ys.append(ys[-1]+vys[-1]*dt)

    t.append(t[-1]+dt)
    
fig, ax = plt.subplots()
ax.plot(xe,ye,label='earth',linewidth=1)
ax.plot(xj,yj,label='jupiter')
ax.plot(xs,ys,label='sun')
ax.legend(loc='upper right')
fig.set_size_inches(9, 9)

ax.set_xlabel('x(AU)')
ax.set_ylabel('y(AU)')
fig.savefig('worksix', dpi=300)

fig.show()
