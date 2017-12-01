# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:55:20 2017

@author: 王乎
"""
import matplotlib.pyplot as plt
import numpy as np

class three_body:
    def __init__(self,dt,_xe,_vey,_xj,_vjy):
        #earth
        self.xe  = [_xe]
        self.ye  = [0]
        self.vex = [0]
        self.vey = [_vey]
        #juypter
        self.xj  = [_xj]
        self.yj  = [0]
        self.vjx = [0]
        self.vjy = [_vjy]
        
        #self.t   = t
        self.dt  = dt
        
    def sub(self):
        Ms = 2.0e30
        Me = 6.0e24
        Mj = 1.9e27
        for i in range(20000):
            re  = np.sqrt(self.xe[-1]**2 + self.ye[-1]**2)
            rj  = np.sqrt(self.xj[-1]**2 + self.yj[-1]**2)
            rej = np.sqrt((self.xe[-1] - self.xj[-1])**2 + (self.ye[-1] - self.yj[-1])**2)
            
            ae1 = 4*np.pi**2*self.xe[-1]/re**3
            ae2 = 4*np.pi**2*(Mj/Ms)*(self.xe[-1] - self.xj[-1])/rej**3
            ae3 = 4*np.pi**2*self.ye[-1]/re**3
            ae4 = 4*np.pi**2*(Mj/Ms)*(self.ye[-1] - self.yj[-1])/rej**3
            
            aj1 = 4*np.pi**2*self.xj[-1]/rj**3
            aj2 = 4*np.pi**2*(Me/Ms)*(self.xe[-1] - self.xj[-1])/rej**3
            aj3 = 4*np.pi**2*self.yj[-1]/rj**3
            aj4 = 4*np.pi**2*(Me/Ms)*(self.ye[-1] - self.yj[-1])/rej**3
            
            
            self.vex.append(self.vex[-1] - ae1*self.dt - ae2*self.dt)
            self.vey.append(self.vey[-1] - ae3*self.dt - ae4*self.dt)
            self.vjx.append(self.vjx[-1] - aj1*self.dt - aj2*self.dt)
            self.vjy.append(self.vjy[-1] - aj3*self.dt - aj4*self.dt)
            
            self.xe.append(self.xe[-1] + self.vex[-1]*self.dt)
            self.ye.append(self.ye[-1] + self.vey[-1]*self.dt)
            self.xj.append(self.xj[-1] + self.vjx[-1]*self.dt)
            self.yj.append(self.yj[-1] + self.vjy[-1]*self.dt)
            
            
        
    def plot(self):
        plt.plot(self.xe,self.ye,label = 'Earth')
        #plt.plot(self.xj,self.yj,label = 'Jupiter')
            
            
tr = three_body(0.001,1,2*np.pi,5.2,np.sqrt(4*(np.pi)**2/5.2))  
tr.sub()
tr.plot()
#xx,yy = tr.sub()
#plt.plot(xx,yy)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        