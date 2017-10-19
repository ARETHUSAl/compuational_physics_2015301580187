# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:03:40 2017

@author: 王乎
"""
import sys
import math
import time
import numpy 
from matplotlib import pyplot
from numpy import arange
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

# fixed 
g        = 9.8
#B2m     = 4e-5
S0m      = 4.1e-4
iniSpeed = 50
sita     = math.pi/2
sign     = -2
vwind    = 2
ws        = arange(0,100,20)
##############################################


class FlightState:
    def __init__(self, _x = 0, _y = 0, _z = 0, _vx = 0, _vy = 0, _vz = 0, _t = 0):
        self.x  = _x
        self.y  = _y
        self.z  = _z
        self.vx = _vx
        self.vy = _vy
        self.vz = _vz
        self.t  = _t


class CannonShell:
    def __init__(self, _fs = FlightState(0, 0, 0, 0, 0, 0, 0), _dt = 0.1):
        self.flightState = []
        self.flightState.append(_fs)
        self.dt = _dt
        print ("good!")
        
    def getNextState(self,currentState):
        #currentState = self.flightState[-1]
        nx  = currentState.x  + currentState.vx * self.dt
        ny  = currentState.y  + currentState.vy * self.dt
        nz  = currentState.z  + currentState.vz * self.dt
        nvx = currentState.vx + self.getCurrentAcc(currentState)[0] * self.dt
        nvy = currentState.vy + self.getCurrentAcc(currentState)[1] * self.dt
        nvz = currentState.vz + self.getCurrentAcc(currentState)[2] * self.dt
        return FlightState(nx, ny, nz, nvx, nvy, nvz, currentState.t + self.dt)
        
    def shoot(self):
        while not(self.flightState[-1].y < 0):
            self.flightState.append(self.getNextState(self.flightState[-1]))
            
        r = - self.flightState[-2].y / self.flightState[-1].y
        self.flightState[-1].x = (self.flightState[-2].x + r * self.flightState[-1].x)/(r+1)
        self.flightState[-1].y = 0
    
    def getCurrentAcc(self,currentState):
        factor     = self.getFactor(currentState)
        B2m        = self.getB2m(currentState)
        v          = math.sqrt(currentState.vx ** 2 + currentState.vy ** 2)
        ax         = factor * (-B2m * abs(v - vwind) * (currentState.vx - vwind))
        ay         = factor * (-B2m * abs(v - vwind) * currentState.vy) - g
        az         = - S0m * currentState.vx * w
        #ax         = (-B2m * abs(v - vwind) * (currentState.vx - vwind))
        #ay         = (-B2m * abs(v - vwind) * currentState.vy) - g
        currentAcc = [ax,ay,az]
        return currentAcc
        
    def getFactor(self,currentState):
        alpha  = 2.5
        a      = 6.5e-3
        factor = (1-a*currentState.y / 287.15)**alpha
        return factor
     
    def getB2m(self,currentState):
        v     = math.sqrt(currentState.vx ** 2 + currentState.vy ** 2)
        const = 0.0039
        vd    = 35
        det   = 5
        mid   = math.exp((v-vd) / det)
        B2m   = const + 0.0058 / (1 + mid)
        return B2m
    
    def showTrajectory(self):
        x = []
        y = []
        z = []
        for fs in self.flightState:
            x.append(fs.x)
            y.append(fs.y)
            z.append(fs.z)
        pyplot.plot(x, z, y, label = 'Angular Velocity is $%s m/s$'%w)
        pyplot.legend(bbox_to_anchor=(0.4,0.9))
    
        
        


###################################################################################
fig = pyplot.figure()#(figsize=(16,8,4))
xmin, xmax = 0., 150
ymin, ymax = 0., 50
zmin, zmax = 0., 20
dx = (xmax - xmin) * 0.1
dy = (ymax - ymin) * 0.2
dz = (zmax - zmin) * 0.5
#ax = pyplot.axes(xlim = (xmin, xmax + dx), ylim = (ymin, ymax + dy), zlim = (zmin, zmax + dz))
ax = fig.gca(projection='3d')
ax.set(xlabel=r'$x(m)$', ylabel=r'$z(m)$', zlabel=r'$y(m)$')
inputStartAngle = 30

for i in range(len(ws)):
    w = ws[i]
    startAngle = inputStartAngle
    Angle      = (startAngle/90)*sita
##################################################################################
    iniVy = iniSpeed*math.sin(Angle)
    iniVx = iniSpeed*math.cos(Angle)
    cannonShell = CannonShell(FlightState(0, 0, 0, iniVx, iniVy, 0, 0), _dt = 0.1)
    cannonShell.shoot()
    cannonShell.showTrajectory()

    pyplot.savefig("Cannon Trajectory")

pyplot.show()


