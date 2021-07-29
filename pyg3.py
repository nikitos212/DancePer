import pygame as pg
import sys

c=0
cadr=1
dir=1
tr=False
class person(pg.sprite.Sprite):
    def __init__(self,img1):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load(img1).convert_alpha()
        self.rect=self.image.get_rect(topright=(400,100))
    def update(self,img1, img2, img3, img4, img5, img6, img7):
        global c
        global cadr
        global dir
        global tr
        c += 1
        m = [img1, img2, img3, img4, img5, img6, img7]
        i = cadr % len(m)
        if c % 5 == 0:
            if tr == True:
                self.image = pg.transform.flip(pg.image.load(m[i]), True, False)
                self.rect = self.image.get_rect(topright=(400, 100))
            else:
                self.image = pg.image.load(m[i]).convert_alpha()
            if cadr % 12 == 0:
                dir = 1
            elif cadr % 6 == 0 and cadr % 14 != 0:
                dir = -1
            if dir==1:
                cadr += 1
            else:
                cadr-=1
        if c%260==0 and c%520!=0:
            tr=True
        if c%260==0 and c%520==0:
            tr=False

pg.init()
sc=pg.display.set_mode((600,400))
per1=person("images/flex1.png")
t1=pg.time.Clock()
s2=pg.mixer.Sound("sounds/mi.mp3")
s2.play()
bg1=pg.image.load("images/bg.jpg")
bgrec1=bg1.get_rect(topleft=(0,0))
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    per1.image.set_colorkey((255, 255, 255))
    sc.fill((255, 5, 255))
    sc.blit(bg1, bgrec1)
    sc.blit(per1.image, per1.rect)
    per1.update("images/flex1.png","images/flex2.png","images/flex3.png","images/flex4.png","images/flex5.png","images/flex6.png","images/flex7.png")
    pg.display.update()
    t1.tick(50)
