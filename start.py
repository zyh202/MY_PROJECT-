from asyncio.windows_utils import Popen
import pygame,os
from locale import *
from sys import exit
pygame.init()
canvas=pygame.display.set_mode([638,479])
pygame.display.set_caption('pong start')
canvas.fill([255,255,255])
def filltext(content,pos,size):
    fontColor = (0, 0, 0)
    fontObj = pygame.font.Font("simhei.ttf", size)  # 通过字体文件获得字体对象
    font = fontObj.render(content, True, fontColor)  # 配置要显示的文字
    canvas.blit(font, pos)  # 绘制字

start = pygame.image.load('start.jpg')
bg=pygame.image.load('bg.jpg')

while 1:
    canvas.blit(bg,[0,0])
    canvas.blit(start,[200,300])
    filltext('pong game',[150,50],50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                p=Popen('py test.py',shell=True)
                exit()

    pygame.display.update()
