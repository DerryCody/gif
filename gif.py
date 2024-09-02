import pygame
import time
pygame.init()
HEIGHT=600
WIDTH=600
TITLE="HAPPY BIRTHDAY!"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

a=True
bg1=pygame.image.load("bauble.webp")
bg2=pygame.image.load("tree.webp")
bg3=pygame.image.load("feast.webp")

while a==True:
    screen.fill("white")
    screen.blit(bg1,(0,0))
    font=pygame.font.SysFont("comic sans",50)
    message1=font.render("YOU BETTER GET READY...",True,"red")
    screen.blit(message1,(20,200))
    pygame.display.update()
    time.sleep(2)
    screen.blit(bg2,(0,0))
    message2=font.render("AND DECORATE YOUR TREES...",True,"green")
    screen.blit(message2,(25,540))
    pygame.display.update()
    time.sleep(2)
    screen.blit(bg3,(0,0))
    message4=font.render("BECAUSE ITS CHRISTMAS!",True,"white")
    screen.blit(message4,(100,60))
    pygame.display.update()
    time.sleep(2)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            a=False
    pygame.display.update()

