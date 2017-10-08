# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:44:43 2017

@author: 王乎
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

class ode:
    def __init__(self,dx,a,b,Y):
        self.dx = dx    # step length
        self.a = a      # lower limit
        self.Y = [0]
        if (type(Y) == int):
            self.Y[0] =Y
        else:
            self.Y = Y      # initial y
        self.N = int(float(b - self.a)/(self.dx)) + 1
        self.data = [[],[]] # store all the datas
           
    def set_fx(self,f,variable_name):                ###setting the function on the right side 
        self.f = [0]
        if (type(f) == str):
            self.f[0] = f
        else:
            self.f = f
        self.number = len(variable_name) - 1
        self.dep_name = []
        for i in range(len(variable_name)):
            self.dep_name.append(variable_name[i])
        self.dep_name_record = self.dep_name[:]
        return 0
    
    def Exe(self,string):
        pass
        
    def euler(self):                   ###simple Euler method
        self.y = []
        self.x = []
        self.x.append(self.a)           #
        for l in range(self.number):    ###
            self.y.append([])           ####    setting the initial value
            self.y[l].append(self.Y[l]) ###
        for i in range(1,self.N):
            for k in range(self.number):
                self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1])
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1])
            for m in range(self.number + 1):
                exec (self.dep_name[m])
            for j in range(self.number):
                self.y[j].append(self.y[j][i - 1] + eval(self.f[j]) * self.dx)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data
    
    def store(self,data__file):           #### save the calculculate datas            
        data_file = open(data__file,'w')
        for i in range(self.N):
            data_file.write(str(self.data[0][i]))
            data_file.write(' ')
            if (len(self.data[1] == 1)):
               data_file.write(str(self.data[1][i]))
            else:
                for j in range(len(self.data[1])):
                    data_file.write(str(self.data[1][j][i]))
                    data_file.write(' ')
            data_file.write('\n')
        data_file.close  
        
############################################################################################################
N= 1000
a1= input("a = :")
a1= float(a1)
b1= input("b = :")
b1= float(b1)
A = ode(0.01,0,0.5,N)
A.set_fx('%s*y-%s*y*y'%(a1,b1),['x','y']) # 调整a,b参数
euler_record = A.euler()[:]
b = 0
y = [100]
euler_2nd = [100]
###############################################################################################
'''plt.figure(figsize = (10,6))
plt.ylabel('Population',fontsize = 11)
plt.xlabel('Time', fontsize = 11)
plt.plot(euler_record[1][0],linewidth = 2,label = 'simple euler method')'''
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

xs = range(15000)
ys = range(60)
plt.ylabel('Population',fontsize = 12)
plt.xlabel('Time/year', fontsize = 12)
ax.set_title("N = %s , a = %s , b = %s"%(N,a1,b1))
ax.plot(euler_record[1][0],linewidth = 2,label = 'simple euler method')
savefig("N = %s , a = %s , b = %s.png"%(N,a1,b1),dpi=300)
plt.show()