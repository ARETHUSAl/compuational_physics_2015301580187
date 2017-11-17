# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 09:47:22 2017

@author: 王乎
"""
import math
import pygame
import time
import random

pygame.init()


# fixed 
g        = 9.8
uangle   = math.pi/4
deg10    = math.pi/180
ix       = 0
iy       = 420
######################################################################################################
#####################################################      精灵组设置
######################################################################################################
ButtleGroup = pygame.sprite.Group()

Boss1Group  = pygame.sprite.Group()     
Boss2Group  = pygame.sprite.Group()



######################################################################################################
#####################################################      图片设置
######################################################################################################
background_image = pygame.image.load ("bg.jpg")
'''      玩家角色   '''
player1     = pygame.image.load ("QmanD.png")
player2     = pygame.image.load ("QqiD.png")
player3     = pygame.image.load ("QxiaD.png")
'''       武器     '''
buttle1     = pygame.image.load ("huo.png")
buttle2     = pygame.image.load ("huolan.png")
buttle3     = pygame.image.load ("huolv.png")
'''       BOSS     '''
boss1       = pygame.image.load ("boss1.png")
boss2       = pygame.image.load ("yue.png")

player = [player1,player2,player3]

#######################################################################################################    
#######################################################         文字处理
#######################################################################################################      
def show_text(surface_handle, pos, text, color, font_bold = False, font_size = 13, font_italic = False):   
    ''''' 
    Function:文字处理函数 
    Input：surface_handle：surface句柄 
           pos：文字显示位置 
           color:文字颜色 
           font_bold:是否加粗 
           font_size:字体大小 
           font_italic:是否斜体 
    Output: NONE 
    author: socrates 
    blog:http://blog.csdn.net/dyx1024 
    date:2012-04-15 
    '''         
    #获取系统字体，并设置文字大小  
    cur_font = pygame.font.SysFont("宋体", font_size)  
      
    #设置是否加粗属性  
    cur_font.set_bold(font_bold)  
      
    #设置是否斜体属性  
    cur_font.set_italic(font_italic)  
      
    #设置文字内容  
    text_fmt = cur_font.render(text, 1, color)  
      
    #绘制文字  
    surface_handle.blit(text_fmt, pos)

##########################################################################################################
####################################################                  Boss类
##########################################################################################################
class Enemy(pygame.sprite.Sprite):  
    def __init__(self,position): 
        pygame.sprite.Sprite.__init__(self) 
        self.health = 10
        self.image = boss1 
        self.rect = self.image.get_rect()
        self.speed = 15   
        self.rect.left,self.rect.top = position 
        self.mask = pygame.mask.from_surface(self.image)    
          
    def move(self):  
        self.rect.left -= self.speed  

class Boss1(Enemy):
    def __init__(self,position):
        Enemy.__init__(self,position)
        self.health = 1
        self.speed  = 8
        self.image  = boss1
        self.rect.left,self.rect.top = position
        
class Boss2(Enemy):
    def __init__(self,position):
        Enemy.__init__(self,position)
        self.health = 5
        self.speed  = 2
        self.image  = boss2
        self.rect.left,self.rect.top = position
    
    
##########################################################################################################
####################################################                  武器类
##########################################################################################################
class Buttle(pygame.sprite.Sprite):
    def __init__(self,_position):
        pygame.sprite.Sprite.__init__(self)
    
        self.image  = buttle1  
        self.rect   = self.image.get_rect()           
        self.speed  = 18 
        self.hert   = 3
        self.active = False 
        self.rect.left,self.rect.top = _position
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):  
        self.rect.left += self.speed            
        if self.rect.left < 1136:  
            self.active = False  
              
    def reset(self,position):  
        self.rect.left,self.rect.top = position  
        self.active = True  

class Buttle1(Buttle):
    def __init__(self,_1position):
        self.position = _1position
        Buttle.__init__(self,self.position)
        self.image = buttle1
        self.speed = 20
        self.hert  = 3
        self.rect.left,self.rect.top = _1position
        
class Buttle2(Buttle):
    def __init__(self,_2position):
        self.position = _2position
        Buttle.__init__(self,self.position)
        self.image = buttle2
        self.speed = 30
        self.hert  = 2
        self.rect.left,self.rect.top = _2position
        
class Buttle3(Buttle):
    def __init__(self,_3position):
        self.position = _3position
        Buttle.__init__(self,self.position)
        self.image = buttle3
        self.speed = 40
        self.hert  = 1
        self.rect.left,self.rect.top = _3position
        
#######################################################################
#          pygame main
#######################################################################

screen = pygame.display.set_mode((1136, 640), 0, 32)
pygame.display.set_caption("Cannon")

clock = pygame.time.Clock()

playernum = 0
bossnum   = 0
healthy   = 10
isstart = False
Boss1_frequency = 0
Boss2_frequency = 0
jishi = 9
BF1 = 50
BF2 = 200
shijian = 0
while True:
    shijian += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background_image, (0,0))
    
    pressed_keys  = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()
    if pressed_keys[27]:
        pygame.quit()
        exit()
        
    if pressed_keys[113]:   # key q
        uangle = uangle + deg10
        if uangle > math.pi/2:
            uangle = math.pi/2
    if pressed_keys[101]:
        uangle = uangle - deg10
        if uangle < 0:
            uangle = 0
    if pressed_keys[97]:#A
        ix = ix - 10
        if ix < 0:
            ix = 0
    if pressed_keys[100]:#D
        ix = ix + 10
        if ix > 1100:
            ix = 1100
    if pressed_keys[119]:#W
        iy = iy - 10
        if iy > 640:
            iy = 640
    if pressed_keys[115]:#S
        iy = iy + 10
        if iy < 20:
            iy = 20
    if pressed_keys[9]:#TAB
        playernum = playernum + 1
        playernum = playernum % 3
        time.sleep(0.2)
        
    player_position = [ix + 100, iy + 100]
    
    jishi += 1
    if jishi > 9:
        isok = True
        if jishi > 18:
            jishi = 9
        
    if pressed_keys[32] & isok: #space 发射
        isok = False
        jishi = 0
        if playernum == 0:
            bu = Buttle1(player_position)
            ButtleGroup.add(bu) 
           #time.sleep(0.1)
        if playernum == 1:
            bu = Buttle2(player_position)
            ButtleGroup.add(bu)
            #time.sleep(0.1)
        if playernum == 2:
            bu = Buttle3(player_position)
            ButtleGroup.add(bu)
            #time.sleep(0.1)
            
    for bu in ButtleGroup:
        bu.move()
        screen.blit(bu.image,(bu.rect.left,bu.rect.top))
       
        if bu.rect.left > 1200:
            ButtleGroup.remove(bu)
            
    #aaa = len(ButtleGroup) 
    if Boss1_frequency % BF1 == 0:
        boss1_pos = [1200, random.randint(0, 560)]
        enemy1    = Boss1(boss1_pos)
        Boss1Group.add(enemy1)
    Boss1_frequency += 1
    if Boss1_frequency >= 2*BF1:
        enemy_frequency = 0
        
    if Boss2_frequency % BF2 == 0:
        boss2_pos = [1200, random.randint(0, 500)]
        enemy2    = Boss2(boss2_pos)
        Boss2Group.add(enemy2)
    Boss2_frequency += 1
    if Boss2_frequency >= 2*BF2:
        enemy_frequency = 0
        
    for enemy1 in Boss1Group:
        enemy1.move()
        screen.blit(enemy1.image,(enemy1.rect.left,enemy1.rect.top))
        
        if enemy1.rect.left < 0:
            Boss1Group.remove(enemy1)
            healthy -= 1
        
        for bu in ButtleGroup:
            result = pygame.sprite.collide_rect(bu,enemy1)
            if result:
                enemy1.health -= bu.hert
                ButtleGroup.remove(bu)
        
        if enemy1.health < 1:
            Boss1Group.remove(enemy1)
    
    for enemy2 in Boss2Group:
        enemy2.move()
        screen.blit(enemy2.image,(enemy2.rect.left,enemy2.rect.top))
        
        if enemy2.rect.left < 0:
            Boss2Group.remove(enemy2)
            healthy -= 5
            
        for bu in ButtleGroup:
            result = pygame.sprite.collide_rect(bu,enemy2)
            if result:
                enemy2.health -= bu.hert
                ButtleGroup.remove(bu)
        
        if enemy2.health < 1:
            Boss2Group.remove(enemy2)    
    
    if healthy < 1:
        show_text(screen, (200,200), "GAME OVER",(255,48,48), True, 150)
        
    if shijian > 0    and shijian < 500:
        show_text(screen, (800, 20), r'Level zero', (240,248,255), True, 40)
    if shijian > 500 and shijian < 2000:
        BF1 = 30
        BF2 = 120
        show_text(screen, (800, 20), r'Level one', (0,248,255), True, 40)
    if shijian > 2000 and shijian < 4000:
        BF1 = 15
        BF1 = 60
        show_text(screen, (800, 20), r'Level two', (240,128,144), True, 40)
    if shijian > 4000:
        BF1 = 10
        BF2 = 30
        show_text(screen, (800, 20), r'Level three', (255,0,0), True, 40)
        
    screen.blit(player[playernum], (ix, iy))
    udegre = uangle * 180 /math.pi
    udegre = int(udegre)
    #title_info  = r"Degree = %s°"%udegre
    health_info = r"Health = %s"%healthy
    show_text(screen, (20,  20), health_info,(240,248,255), True, 40)
    #show_text(screen, (800, 20), title_info, (240,248,255), True, 40)
    pygame.display.update()
    
    
   


  