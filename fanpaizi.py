import pygame
import sys
import random
import time
pygame.init()
screen=pygame.display.set_mode((1450,736))
bk=pygame.image.load("images/hougong.jpg")
screen.blit(bk,(0,0))
myimg1=["hougong1.jpg","hongong2.jpg","hongong3.jpg","hongong4.jpg","hongong5.jpg","hongong6.jpg","hougong1.jpg","hongong2.jpg","hongong3.jpg","hongong4.jpg","hongong5.jpg","hongong6.jpg"]
imgs=[]
y=5
lens=len(myimg1)
print(lens)
cur_i=-1
cur_card=""
for i in range(100):
    m=random.randint(0,lens-1)
    n=random.randint(0,lens-1)
    myimg1[m],myimg1[n]=myimg1[n],myimg1[m]
for i in range(12):
    if i%6==0 and y!=0:
        y+=250
    img1=pygame.image.load("images/back.png")
    x=i%6*200+100
    screen.blit(img1,(x,y))
    imgs.append(img1)
duibi_arr=[]
while True:
    sum_none=0
    for im in imgs:
        if im==None:
            sum_none+=1
    print("XXXXX"+str(sum_none)+"XXXXXX")

    if len(duibi_arr) > 0:
        print(duibi_arr[0])
        print(duibi_arr[1])
        print(myimg1[duibi_arr[0]])
        print(myimg1[duibi_arr[1]])
        imgs[duibi_arr[0]] = None
        imgs[duibi_arr[1]] = None
        duibi_arr = []
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousex,mousey=event.pos
            if mousex>100 and mousex<180 and mousey>260 and mousey<460:
                imgs[0]=pygame.image.load("images/"+myimg1[0])
                if cur_i==-1:
                    cur_i=0
                    cur_card=myimg1[0]
                else:
                    if cur_i==0:
                        imgs[0]=pygame.image.load("images/back.png")
                        cur_i=-1
                        cur_card=""
                    else:
                        if cur_card==myimg1[0]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(0)
                            cur_i=-1
                            cur_card=None
                        else:
                            imgs[cur_i]=pygame.image.load("images/back.png")
                            cur_i=0
                            cur_card=myimg1[0]
            elif mousex>300 and mousex<380 and mousey>260 and mousey<460:
                imgs[1] = pygame.image.load("images/" + myimg1[1])
                if cur_i==-1:
                    cur_i=1
                    cur_card=myimg1[1]
                else:
                    if cur_i==1:
                        imgs[1]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[1]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(1)
                            cur_i=-1
                            cur_card = None
                        else:
                            imgs[cur_i]=pygame.image.load("images/back.png")
                            cur_i =1
                            cur_card = myimg1[1]
            elif mousex > 500 and mousex < 580 and mousey > 260 and mousey < 460:
                imgs[2] = pygame.image.load("images/" + myimg1[2])
                if cur_i==-1:
                    cur_i=2
                    cur_card=myimg1[2]
                else:
                    if cur_i==2:
                        imgs[2]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[2]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(2)
                            cur_i=-1
                            cur_card = None
                        else:
                            imgs[cur_i] = pygame.image.load("images/back.png")
                            cur_i =2
                            cur_card = myimg1[2]
            elif mousex > 700 and mousex < 780 and mousey > 260 and mousey < 460:
                imgs[3] = pygame.image.load("images/" + myimg1[3])
                if cur_i==-1:
                    cur_i=3
                    cur_card=myimg1[3]
                else:
                    if cur_i==3:
                        imgs[3]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[3]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(3)
                            cur=-1
                            cur_card = None
                        else:
                            imgs[cur_i] = pygame.image.load("images/back.png")
                            cur_i =3
                            cur_card = myimg1[3]
            elif mousex > 900 and mousex < 980 and mousey > 260 and mousey < 460:
                imgs[4] = pygame.image.load("images/" + myimg1[4])
                if cur_i==-1:
                    cur_i=4
                    cur_card=myimg1[4]
                else:
                    if cur_i==4:
                        imgs[4]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[4]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(4)
                            cur_i=-1
                            cur_card = None
                        else:
                            imgs[cur_i] = pygame.image.load("images/back.png")
                            cur_i =4
                            cur_card = myimg1[4]
            elif mousex > 1100 and mousex < 1180 and mousey > 260 and mousey < 460:
                imgs[5] = pygame.image.load("images/" + myimg1[5])
                if cur_i==-1:
                    cur_i=5
                    cur_card=myimg1[5]
                else:
                    if cur_i==5:
                        imgs[5]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[5]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(5)
                            cur_i=-1
                            cur_card = None
                        else:
                            imgs[cur_i] = pygame.image.load("images/back.png")
                            cur_i =5
                            cur_card = myimg1[5]
            elif mousex > 100 and mousex < 180 and mousey >510 and mousey < 710:
                imgs[6] = pygame.image.load("images/" + myimg1[6])
                if cur_i==-1:
                    cur_i=6
                    cur_card=myimg1[6]
                else:
                    if cur_i==6:
                        imgs[6]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[6]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(6)
                            cur_i=-1
                            cur_card = None
                        else:
                            imgs[cur_i] = pygame.image.load("images/back.png")
                            cur_i = 6
                            cur_card = myimg1[6]
            elif mousex > 300 and mousex < 380 and mousey >510 and mousey < 710:
                imgs[7] = pygame.image.load("images/" + myimg1[7])
                if cur_i==-1:
                    cur_i=7
                    cur_card=myimg1[7]
                else:
                    if cur_i==7:
                        imgs[7]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[7]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(7)
                            cur_i=-1
                            cur_card = None
                        else:
                            imgs[cur_i] = pygame.image.load("images/back.png")
                            cur_i =7
                            cur_card = myimg1[7]
            elif mousex > 500 and mousex < 580 and mousey >510 and mousey < 710:
                imgs[8] = pygame.image.load("images/" + myimg1[8])
                if cur_i==-1:
                    cur_i=8
                    cur_card=myimg1[8]
                else:
                    if cur_i==8:
                        imgs[8]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[8]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(8)
                            cur_i=-1
                            cur_card=None
                        else:
                            imgs[cur_i] = pygame.image.load("images/back.png")
                            cur_i =8
                            cur_card = myimg1[8]
            elif mousex > 700 and mousex < 780 and mousey >510 and mousey < 710:
                imgs[9] = pygame.image.load("images/" + myimg1[9])
                if cur_i==-1:
                    cur_i=9
                    cur_card=myimg1[9]
                else:
                    if cur_i==9:
                        imgs[9]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[9]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(9)
                            cur_i=-1
                            cur_card = None
                        else:
                            imgs[cur_i] = pygame.image.load("images/back.png")
                            cur_i = 9
                            cur_card = myimg1[9]
            elif mousex > 900 and mousex < 980 and mousey >510 and mousey < 710:
                imgs[10] = pygame.image.load("images/" + myimg1[10])
                if cur_i==-1:
                    cur_i=10
                    cur_card=myimg1[10]
                else:
                    if cur_i==10:
                        imgs[10]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[10]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(10)
                            cur_i=-1
                            cur_card = None
                        else:
                            imgs[cur_i] = pygame.image.load("images/back.png")
                            cur_i =10
                            cur_card = myimg1[10]
            elif mousex > 1100 and mousex < 1180 and mousey >510 and mousey < 710:
                imgs[11] = pygame.image.load("images/" + myimg1[11])
                if cur_i==-1:
                    cur_i=11
                    cur_card=myimg1[11]
                else:
                    if cur_i==11:
                        imgs[11]=pygame.image.load("images/back.png")
                        cur_i = -1
                        cur_card = None
                    else:
                        if cur_card==myimg1[11]:
                            imgs[cur_i] = pygame.image.load("images/" + cur_card)
                            duibi_arr.append(cur_i)
                            duibi_arr.append(11)
                            cur_i=-1
                            cur_card = None
                        else:
                            imgs[cur_i] = pygame.image.load("images/back.png")
                            cur_i =11
                            cur_card = myimg1[11]

    screen.fill((0,0,0))
    bk = pygame.image.load("images/hougong.jpg")
    screen.blit(bk, (0, 0))
    y=5
    for i in range(0,lens):
        if i % 6 == 0 and y != 0:
            y += 250
        x = i % 6 * 200 + 100
        if imgs[i]==None:
            continue
        screen.blit(imgs[i],(x,y))
    if sum_none >= 12:
        over = pygame.image.load("images/over.png")
        screen.blit(over, (500, 20))
    pygame.display.update()