import pygame
import random
pygame.init()
screen=pygame.display.set_mode((1450,736))
bk=pygame.image.load("images/hougong.jpg")
screen.blit(bk,(0,0))
y=5
index=0
cards=["images/hongong1.jpg","images/hongong2.jpg","images/hongong3.jpg","images/hongong4.jpg","images/hongong5.jpg","images/hongong1.jpg","images/hongong2.jpg","images/hongong3.jpg","images/hongong4.jpg","images/hongong5.jpg"]
print("原来的:")
print(cards)
for j in range(1000):
    m=random.randint(0,len(cards)-1)
    n=random.randint(0,len(cards)-1)
    cards[m],cards[n]=cards[n],cards[m]
print("洗牌之后的:")
print(cards)
curx=-1
cury=-1
for i in range(10):
    if i%5==0 and y!=0:
        y+=250
    img1=pygame.image.load("images/back.png")
    x=i%5*200+100
    screen.blit(img1,(x,y))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mosx,mosy=event.pos
            if mosy>=5 and mosy<500:
                index=int((mosx-100)/200)
            elif mosy>=500:
                index=int((mosx-100)/200)+5
            if curx==-1:
                curx=index
                cury=mosy
                img2 = pygame.image.load(cards[index])
            else:
                if curx==index:
                    img2=pygame.image.load("images/back.png")
                    curx=-1
                    cury=-1
                else:
                    print(cards[curx])
                    print(cards[index])
                    print("----------------")
                    oldx=curx
                    oldy=cury
                    if cards[curx]!=cards[index]:
                        img2=pygame.image.load(cards[index])
                        img3 = pygame.image.load("images/back.png")
                        curx = index
                        cury = mosy
                    elif cards[curx]==cards[index]:
                        img2=pygame.image.load("images/same.png")
                        img3 = pygame.image.load("images/same.png")
                        curx = -1
                        cury = -1
                    if oldx< 5:
                        x1 = oldx*200 + 100
                    else:
                        x1 = (oldx - 5) * 200 + 100
                    if oldy >= 500:
                        y1 = 500
                    else:
                        y1 = 255
                    print("****************")
                    print(oldx)
                    print(x1)
                    print(y1)
                    print(img3)
                    print("*****************")
                    screen.blit(img3, (x1, y1))
            if index<5:
                x=index*200+100
            else:
                x=(index-5)*200+100
            if mosy>=500:
                y=500
            else:
                y=255
            screen.blit(img2, (x, y))
    pygame.display.update()
