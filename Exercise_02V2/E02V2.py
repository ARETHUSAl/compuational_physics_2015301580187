# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:41:33 2017

@author: 王乎
"""

import pygame
from pygame.locals import *
from sys import exit
import os
 
pygame.init()

str = input("Input Your Name: ");
 
text = str
font = pygame.font.Font(os.path.join("ttc", "STKAITI.ttf"), 64)
rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))
 
pygame.image.save(rtext, "t.jpg")

######################################################################################

background_image_filename = 'background.jpg'
name_image_filename = 't.jpg'
 
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("MyName")
 
background = pygame.image.load(background_image_filename).convert()
name = pygame.image.load(name_image_filename).convert_alpha()
 
clock = pygame.time.Clock()
 
x, y = 100., 100.
speed_x, speed_y = 200., 200.
 
while True:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                        #这个地方应该是版本更新了的
            exit()                               #这样才能平滑退出（滑稽）
 
    screen.blit(background, (0,0))
    screen.blit(name, (x, y))
 
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0
 
    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds    
 
    # 到达边界则把速度反向
    if x > 640 - name.get_width():
        speed_x = -speed_x
        x = 640 - name.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0.
 
    if y > 480 - name.get_height():
        speed_y = -speed_y
        y = 480 - name.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0
 
    pygame.display.update()