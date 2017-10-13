# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:57:53 2017

@author: 王乎
"""

import sys
import math
import time
import numpy 
from matplotlib import pyplot
import pygame
from pygame.locals import *

pygame.init()


# fixed 
g        = 9.8
B2m      = 4e-5
iniSpeed = 700
sita     = math.pi/2
sign     = -2



class FlightState:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x  = _x
        self.y  = _y
        self.vx = _vx
        self.vy = _vy
        self.t  = _t


class CannonShell:
    def __init__(self, _fs = FlightState(0, 0, 0, 0, 0), _dt = 0.1):
        self.flightState = []
        self.flightState.append(_fs)
        self.dt = _dt
        print (self.flightState[-1].x, self.flightState[-1].y, self.flightState[-1].vx, self.flightState[-1].vy)
        
    def getNextState(self,currentState):
        #currentState = self.flightState[-1]
        nx  = currentState.x  + currentState.vx * self.dt
        ny  = currentState.y  + currentState.vy * self.dt
        nvx = currentState.vx + self.getCurrentAcc(currentState)[0] * self.dt
        nvy = currentState.vy + self.getCurrentAcc(currentState)[1] * self.dt
        return FlightState(nx, ny, nvx, nvy, currentState.t + self.dt)
        
    def shoot(self):
        while not(self.flightState[-1].y < 0):
            self.flightState.append(self.getNextState(self.flightState[-1]))
            
        r = - self.flightState[-2].y / self.flightState[-1].y
        self.flightState[-1].x = (self.flightState[-2].x + r * self.flightState[-1].x)/(r+1)
        self.flightState[-1].y = 0
    
    def getCurrentAcc(self,currentState):
        factor     = self.getFactor(currentState)
        ax         = factor * (-B2m * currentState.vx**2)
        ay         = factor * (-B2m * currentState.vy**2)-g
        currentAcc = [ax,ay]
        return currentAcc
        
    def getFactor(self,currentState):
        alpha  = 2.5
        a      = 6.5e-3
        factor = (1-a*currentState.y / 287.15)**alpha
        return factor
        
    def showTrajectory(self):
        x = []
        y = []
        for fs in self.flightState:
            x.append(fs.x)
            y.append(fs.y)
        return x,y
        

#work
cannonShell = CannonShell(FlightState(0, 0, 1000, 500, 0),_dt = 0.1)
cannonShell.shoot()
cx, cy = cannonShell.showTrajectory()


#######################################################################
#          pygame test
#######################################################################

background_image = pygame.image.load ("background.jpg")
cannon_image     = pygame.image.load ("cannon.png")
#cannon_image     = pygame.transform (cannon_image, (52, 52))

screen = pygame.display.set_mode((1324, 496), 0, 32)
pygame.display.set_caption("Cannon")

clock = pygame.time.Clock()

cannonShell = CannonShell(FlightState(0, 0, 1000, 500, 0),_dt = 0.1)


i = 0
while True:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()                      
            
    screen.blit(background_image, (0,0))
    
    ccx = cx[i]/50
    ccy = 400 - cy[i]/50
    screen.blit(cannon_image, (ccx, ccy))
    i = i+1
    pygame.time.wait(5)
        
         
    #screen.blit(background_image, (0,0))
    #screen.blit(cannon_image, (0, 0))
 
    time_passed = clock.tick(30)
    
    
    pygame.display.update()







