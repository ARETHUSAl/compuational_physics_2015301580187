# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:31:13 2017

@author: 王乎
"""


#使用pygame模块把字符转换为JPG文件，然后用PIL将JPG文件转换为字符画的形式，保存为txt文档

import os
import pygame
from PIL import Image
 
pygame.init()
 
text = u"WANGHU王乎"
font = pygame.font.Font(os.path.join("ttc", "msyh.ttc"), 64)
rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))#渲染到图片
 
pygame.image.save(rtext, "t.jpg")

###################################################################3


codeLib = '''@. '''#生成字符画所需的字符集
count = len(codeLib)

def transform1(image_file):
    image_file = image_file.convert("L")#转换为黑白图片，参数"L"表示黑白模式
    codePic = ''
    for h in range(0,image_file.size[1]):  #size属性表示图片的分辨率，'0'为横向大小，'1'为纵向
        for w in range(0,image_file.size[0]):
            gray = image_file.getpixel((w,h)) #返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组
            codePic = codePic + codeLib[int(((count-1)*gray)/256)]#建立灰度与字符集的映射
        codePic = codePic+'\r\n'
    return codePic

def transform2(image_file):
    codePic = ''
    for h in range(0,image_file.size[1]):
        for w in range(0,image_file.size[0]):
            g,r,b = image_file.getpixel((w,h))
            gray = int(r* 0.299+g* 0.587+b* 0.114)
            codePic = codePic + codeLib[int(((count-1)*gray)/256)]
        codePic = codePic+'\r\n'
    return codePic


fp = open(u't.jpg','rb')
image_file = Image.open(fp)
image_file=image_file.resize((int(image_file.size[0]*0.75), int(image_file.size[1]*0.5)))#调整图片大小
print (u'Info:',image_file.size[0],' ',image_file.size[1],' ',count)

out = open('out.txt','w') #输出TXT文件
out.write(transform1(image_file))
out.close()