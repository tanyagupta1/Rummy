#Name:Tanya Gupta
#Roll No.: 2019119



import pygame
import pygame.mixer
import random
import time
from pygame.locals import *
file="magic.mp3"
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(file)
screen = pygame.display.set_mode([725,580])
green=(0,255,0)
blue=(255,0,255)
white=(255,255,255)

pygame.display.set_caption("Rummy")


screen.fill(white)
clk=pygame.time.Clock()

winner=True
score=80



card_l = [] #This variable will hold all the images of the cards
img1_1 = pygame.image.load("cards/ace_clubs.png").convert()
card_l.append(img1_1)
img1_2 = pygame.image.load("cards/2_clubs.png").convert()
card_l.append(img1_2)
img1_3 = pygame.image.load("cards/3_clubs.png").convert()
card_l.append(img1_3)
img1_4 = pygame.image.load("cards/4_clubs.png").convert()
card_l.append(img1_4)
img1_5 = pygame.image.load("cards/5_clubs.png").convert()
card_l.append(img1_5)
img1_6 = pygame.image.load("cards/6_clubs.png").convert()
card_l.append(img1_6)
img1_7 = pygame.image.load("cards/7_clubs.png").convert()
card_l.append(img1_7)
img1_8 = pygame.image.load("cards/8_clubs.png").convert()
card_l.append(img1_8)
img1_9 = pygame.image.load("cards/9_clubs.png").convert()
card_l.append(img1_9)
img1_10 = pygame.image.load("cards/10_clubs.png").convert()
card_l.append(img1_10)
img1_11 = pygame.image.load("cards/jack_clubs.png").convert()
card_l.append(img1_11)
img1_12 = pygame.image.load("cards/queen_clubs.png").convert()
card_l.append(img1_12)
img1_13 = pygame.image.load("cards/king_clubs.png").convert()
card_l.append(img1_13)
img2_1 = pygame.image.load("cards/ace_spades.png").convert()
card_l.append(img2_1)
img2_2 = pygame.image.load("cards/2_spades.png").convert()
card_l.append(img2_2)
img2_3 = pygame.image.load("cards/3_spades.png").convert()
card_l.append(img2_3)
img2_4 = pygame.image.load("cards/4_spades.png").convert()
card_l.append(img2_4)
img2_5 = pygame.image.load("cards/5_spades.png").convert()
card_l.append(img2_5)
img2_6 = pygame.image.load("cards/6_spades.png").convert()
card_l.append(img2_6)
img2_7 = pygame.image.load("cards/7_spades.png").convert()
card_l.append(img2_7)
img2_8 = pygame.image.load("cards/8_spades.png").convert()
card_l.append(img2_8)
img2_9 = pygame.image.load("cards/9_spades.png").convert()
card_l.append(img2_9)
img2_10 = pygame.image.load("cards/10_spades.png").convert()
card_l.append(img2_10)
img2_11 = pygame.image.load("cards/jack_spades.png").convert()
card_l.append(img2_11)
img2_12 = pygame.image.load("cards/queen_spades.png").convert()
card_l.append(img2_12)
img2_13 = pygame.image.load("cards/king_spades.png").convert()
card_l.append(img2_13)
img3_1 = pygame.image.load("cards/ace_hearts.png").convert()
card_l.append(img3_1)
img3_2 = pygame.image.load("cards/2_hearts.png").convert()
card_l.append(img3_2)
img3_3 = pygame.image.load("cards/3_hearts.png").convert()
card_l.append(img3_3)
img3_4 = pygame.image.load("cards/4_hearts.png").convert()
card_l.append(img3_4)
img3_5 = pygame.image.load("cards/5_hearts.png").convert()
card_l.append(img3_5)
img3_6 = pygame.image.load("cards/6_hearts.png").convert()
card_l.append(img3_6)
img3_7 = pygame.image.load("cards/7_hearts.png").convert()
card_l.append(img3_7)
img3_8 = pygame.image.load("cards/8_hearts.png").convert()
card_l.append(img3_8)
img3_9 = pygame.image.load("cards/9_hearts.png").convert()
card_l.append(img3_9)
img3_10 = pygame.image.load("cards/10_hearts.png").convert()
card_l.append(img3_10)
img3_11 = pygame.image.load("cards/jack_hearts.png").convert()
card_l.append(img3_11)
img3_12 = pygame.image.load("cards/queen_hearts.png").convert()
card_l.append(img3_12)
img3_13 = pygame.image.load("cards/king_hearts.png").convert()
card_l.append(img3_13)
img4_1 = pygame.image.load("cards/ace_diamonds.png").convert()
card_l.append(img4_1)
img4_2 = pygame.image.load("cards/2_diamonds.png").convert()
card_l.append(img4_2)
img4_3 = pygame.image.load("cards/3_diamonds.png").convert()
card_l.append(img4_3)
img4_4 = pygame.image.load("cards/4_diamonds.png").convert()
card_l.append(img4_4)
img4_5 = pygame.image.load("cards/5_diamonds.png").convert()
card_l.append(img4_5)
img4_6 = pygame.image.load("cards/6_diamonds.png").convert()
card_l.append(img4_6)
img4_7 = pygame.image.load("cards/7_diamonds.png").convert()
card_l.append(img4_7)
img4_8 = pygame.image.load("cards/8_diamonds.png").convert()
card_l.append(img4_8)
img4_9 = pygame.image.load("cards/9_diamonds.png").convert()
card_l.append(img4_9)
img4_10 = pygame.image.load("cards/10_diamonds.png").convert()
card_l.append(img4_10)
img4_11 = pygame.image.load("cards/jack_diamonds.png").convert()
card_l.append(img4_11)
img4_12 = pygame.image.load("cards/queen_diamonds.png").convert()
card_l.append(img4_12)
img4_13 = pygame.image.load("cards/king_diamonds.png").convert()
card_l.append(img4_13)
img5_1=pygame.image.load("cards/joker.png").convert()
card_l.append(img5_1)
img5_2=pygame.image.load("cards/joker.png").convert()
card_l.append(img5_2)
img5_3=pygame.image.load("cards/joker.png").convert()
card_l.append(img5_3)
img5_4=pygame.image.load("cards/joker.png").convert()
card_l.append(img5_4)
joker=card_l[52:56]

card_l2=card_l[:]
player_1=[]
comp=[]

for i in range(13):
    f=random.choice(card_l2)

    player_1.append(f)
    card_l2.remove(f)
for j in range(13):
    f1=random.choice(card_l2)

    comp.append(f1)
    card_l2.remove(f1)
    
def countsets(l):
    c=0
    for i in l:
        if type(i)==list:
            c+=1
            
    return c        

def findcons(l):
    """ finds the largest >=3 consecutive set and returns it or returns the initial list """
    k=[l[0]]
    f=[]
    l2=l[:]
    for i in range(len(l)-1):
        
        if l[i]+1==l[i+1]:
            #k.append(l[i])
            k.append(l[i+1])
        else:
            if len(k)<3:
                k=[l[i+1]]
            else:
                if len(k)!=0:
                    
                    f.append(k)
                    k=[l[i+1]]
    if len(k)>2:
        f.append(k)
    if len(f)!=0 :
        maxi=f[0]
        for i in range(1,len(f)):
            maxi+=f[i]
        for j in range(len(l2)):
            if l2[j] not in maxi:
                maxi.append(l2[j])
    else:
        
        
        maxi=l
    return maxi        
def make_run(l1,card_l,comp):
    clubs=card_l[0:13]
    spades=card_l[13:26]
    hearts=card_l[26:39]
    diamonds=card_l[39:52]
    joker=card_l[52:56]
    d={}
    if l1[0] in clubs:
        for i in l1:
            if i not in clubs:
                return comp
            
        for i in range(len(clubs)):
            if clubs[i] in l1:
                d[i]=clubs[i]
        l11=list(d.keys())        





        d=consec(l11)
    elif l1[0] in spades:
        for i in l1:
            if i not in spades:
                return comp
            
        for i in range(len(clubs)):
            if clubs[i] in l1:
                k[i]=clubs[i]
        l11=list(d.keys())        

            
        d=consec(l11)
    elif l1[0] in hearts:
        for i in l1:
            if i not in hearts:
                return comp
            
        for i in range(len(clubs)):
            if clubs[i] in l1:
                k[i]=clubs[i]
        l11=list(d.keys())        
            
        d=consec(l11)
        
    elif l1[0] in diamonds:

        for i in l1:
            if i not in diamonds:
                return comp
            
        for i in range(len(clubs)):
            if clubs[i] in l1:
                k[i]=clubs[i]
        l11=list(d.keys())        
            
        d=consec(l11)
    if d==True:
        l2=[]
        for i in l1:
            l2.append(i)
            comp.remove(i)
        comp.append(l2)
        return comp
    else:
        return comp
    
def consec(l1):

    for i1 in range(len(l1)-1):
        if l1[i1]+1!=l1[i1+1]:
            return False
    return True    

def makerun(l1,card_l):
    """first seperates into c,s,h,d and then uses const to make run and then combines the result to gove a sinlge list """
    #clubs=[img1_1,img1_2,img1_3,img1_4,img1_5,img1_6,img1_7,img1_8,img1_9,img1_10,img1_11,img1_12,img1_13]
    #spades=[img2_1,img2_2,img2_3,img2_4,img2_5,img2_6,img2_7,img2_8,img2_9,img2_10,img2_11,img2_12,img2_13]
    #hearts=[img3_1,img3_2,img3_3,img3_4,img3_5,img3_6,img3_7,img3_8,img3_9,img3_10,img3_11,img3_12,img3_13]
    #diamonds=[img4_1,img4_2,img4_3,img4_4,img4_5,img4_6,img4_7,img4_8,img4_9,img4_10,img4_11,img4_12,img4_13]
    clubs=card_l[0:13]
    spades=card_l[13:26]
    hearts=card_l[26:39]
    diamonds=card_l[39:52]
    clubs_d={}
    spades_d={}
    hearts_d={}
    diamonds_d={}
    
    for i in range(len(clubs)):
        if clubs[i] in l1:
            clubs_d[i]=clubs[i]
    for j in range(len(spades)):
        if spades[j] in l1:
            spades_d[j]=spades[j]
            
    for k in range(len(hearts)):
        if hearts[k] in l1:
            hearts_d[k]=hearts[k]
    for k1 in range(len(diamonds)):
        if diamonds[k1] in l1:
            diamonds_d[k1]=diamonds[k1]



    club1=list(clubs_d.keys())
    spade1=list(spades_d.keys())
    heart1=list(hearts_d.keys())
    diamond1=list(diamonds_d.keys())
    

    club_s=findcons(club1)
    spade_s=findcons(spade1)
    heart_s=findcons(heart1)
    diamond_s=findcons(diamond1)
    l11=[]
    

    for i in club_s:
        l11.append(clubs_d[i])
    for j in spade_s:
        l11.append(spades_d[j])
    for k in heart_s:
        l11.append(hearts_d[k])
    for m in diamond_s:
        l11.append(diamonds_d[m])
    #print(l11)
    return l11
            

    #print(clubs,spades,hearts,diamonds)

def make_set(l1,card_l):
    global comp
    d=False
    
    clubs=card_l[0:13]
    spades=card_l[13:26]
    hearts=card_l[26:39]
    diamonds=card_l[39:52]
    joker=card_l[52:56]
    c_1=[clubs[0],spades[0],hearts[0],diamonds[0]]
    c_2=[clubs[1],spades[1],hearts[1],diamonds[1]]
    c_3=[clubs[2],spades[2],hearts[2],diamonds[2]]
    c_4=[clubs[3],spades[3],hearts[3],diamonds[3]]
    c_5=[clubs[4],spades[4],hearts[4],diamonds[4]]
    c_6=[clubs[5],spades[5],hearts[5],diamonds[5]]
    c_7=[clubs[6],spades[6],hearts[6],diamonds[6]]
    c_8=[clubs[7],spades[7],hearts[7],diamonds[7]]
    c_9=[clubs[8],spades[8],hearts[8],diamonds[8]]
    c_10=[clubs[9],spades[9],hearts[9],diamonds[9]]
    c_11=[clubs[10],spades[10],hearts[10],diamonds[10]]
    c_12=[clubs[11],spades[11],hearts[11],diamonds[11]]
    c_13=[clubs[12],spades[12],hearts[12],diamonds[12]]
    if (l1[0] in c_1) or (l1[1] in c_1):
        d=makeset(l1,c_1)
    elif (l1[0] in c_2) or (l1[1] in c_2):
        d=makeset(l1,c_2)
    elif (l1[0] in c_3) or (l1[1] in c_3):
        d=makeset(l1,c_3)
    elif (l1[0] in c_4) or (l1[1] in c_4):
        d=makeset(l1,c_4)
    elif (l1[0] in c_5) or (l1[1] in c_5) :
        d=makeset(l1,c_5)
    elif (l1[0] in c_6) or (l1[1] in c_6):
        d=makeset(l1,c_6)
    elif (l1[0] in c_7) or (l1[1] in c_7) :
        d=makeset(l1,c_7)
    elif (l1[0] in c_8) or (l1[1] in c_8):
        d=makeset(l1,c_8)
    elif (l1[0] in c_9) or (l1[1] in c_9):
        d=makeset(l1,c_9)
    elif (l1[0] in c_10) or (l1[1] in c_10):
        d=makeset(l1,c_10)
    elif (l1[0] in c_11) or (l1[1] in c_11) :
        d=makeset(l1,c_11)
    elif (l1[0] in c_12) or (l1[1] in c_12):
        d=makeset(l1,c_12)
    elif (l1[0] in c_13) or (l1[1] in c_13):
        d=makeset(l1,c_13)
    if d==True:
        l2=[]
        for i in l1:
            l2.append(i)
            comp.remove(i)
        comp.append(l2)
        return comp
    else:
        return comp
        
def makeset(l1,l2):
    global joker
    j=0
    for i in l1:
        if i in joker:
            j+=1
    if j>1:
        return
    for i in l1:
        if (i not in l2) and (i not in joker):
            return
    return True        




def make_____set(l1,a,b,c,d):

    if (a in l1) and (b in l1) and (c in l1) and (d in l1):
        l2=[a,b,c,d]
        l1.remove(a)
        l1.remove(b)
        l1.remove(c)
        l1.remove(d)
        l1.append(l2)
        return l1


    elif (a in l1) and (b in l1) and (c in l1):
        l2=[a,b,c]
        l1.remove(a)
        l1.remove(b)
        l1.remove(c)
        l1.append(l2)
        return l1
    elif (a in l1) and (b in l1) and (d in l1):
        l2=[a,b,d]
        l1.remove(a)
        l1.remove(b)
        l1.remove(d)
        l1.append(l2)
        return l1
    elif (a in l1) and (c in l1) and (d in l1):
        l2=[a,c,d]
        l1.remove(a)
        l1.remove(c)
        l1.remove(d)
        l1.append(l2)
        return l1
    elif (b in l1) and (c in l1) and (d in l1):
        l2=[b,c,d]
        l1.remove(b)
        l1.remove(c)
        l1.remove(d)
        l1.append(l2)
        return l1
def check_type(l):
    for i in l:
        if type(i)==list:
            return True
    return False


def print_cards(l,pl,x=0):
    
    

    
    if pl=='comp':
        c=0
        if len(l)==3:
            pygame.draw.rect(screen,(0,255,0),[x,0,20*len(l)+90,120])
        else:
            pygame.draw.rect(screen,(0,255,0),[x,0,20*len(l)+70,120])
            
    else:
        c=400
        #pygame.draw.rect(screen,(0,255,0),[0,400,500,120])
        
    for i in range(len(l)):
        screen.blit(l[i],(x,c))
        x+=20
    pygame.display.update()
def printcard(l1):
    l2=l1[:]
    k=0
    

    for i in l1:
        if type(i)==list:
            print_cards(i,'comp',k)
            if len(i)==3:
                k+=20*len(i)+90
            else:
                k+=20*len(i)+70
                

            
            l2.remove(i)
    if len(l2)!=len(l1):
        
        calc_score(l2)

    if len(l2)!=0:
        print_cards(l2,'comp',k)
def calc_score(l):
    global score
    clubs=card_l[0:13]
    spades=card_l[13:26]
    hearts=card_l[26:39]
    diamonds=card_l[39:52]
    club_d={}
    spade_d={}
    heart_d={}
    diamond_d={}
    
    for i in range(len(clubs)):
        if clubs[i] in l:
            club_d[i]=clubs[i]
    for j in range(len(spades)):
        if spades[j] in l:
            spade_d[j]=spades[j]
            
    for k in range(len(hearts)):
        if hearts[k] in l:
            heart_d[k]=hearts[k]
    for k1 in range(len(diamonds)):
        if diamonds[k1] in l:
            diamond_d[k1]=diamonds[k1]



    club1=list(club_d.keys())
    spade1=list(spade_d.keys())
    heart1=list(heart_d.keys())
    diamond1=list(diamond_d.keys())    

    s=0
    s+=scores(club1)
    s+=scores(spade1)
    s+=scores(heart1)
    s+=scores(diamond1)
    score=s

def scores(l):
    k=0
    if len(l)==0:
        return 0

    for i in range(len(l)):
        k+=l[i]+1
    return k    
                    

def textprint(text,x,y):
    fon=pygame.font.Font("freesansbold.ttf",25)
    

    textsurface=fon.render(text,True,(0,0,0))
    texrec=textsurface.get_rect()
    texrec.center=(x,y)
    screen.blit(textsurface,texrec)
    
    




def linj(l1,l2):
    for i in l1:
        if i in l2:
            print('True')
    else:
        print('False')
    
while winner:
    hearts=card_l[26:39]
    x=80
    for i in hearts:
        screen.blit(i,(x,30))
        pygame.display.update()
        x+=40           
    
    
    pygame.mixer.music.play()
    pygame.draw.rect(screen,(255,255,255),[0,0,725,580])
    textprint("Welcome To RUMMY!!!",725/2,200)
    textprint('Click Anywhere To Continue...',725/2,400)
    
    pygame.display.update()
    #time.sleep(5)
    print('yo')
    for even in pygame.event.get():
        if even.type==pygame.MOUSEBUTTONUP:
            winner=False
        
screen.fill(green)

i=0
while not winner:
    if score==0:
        pygame.draw.rect(screen,(0,0,255),[0,0,725,580])
        textprint("YOU WON!!!",300,200)
        pygame.mixer.music.play() 
        time.sleep(5)
        winner=True
        
        #pygame.quit()
        #quit()
        
    for event in pygame.event.get(): #to quit
        if event.type==pygame.QUIT:
            winner=True
            pygame.quit()

            quit()

        print(event)
    
    printcard(comp)
    print_cards(player_1,'p1')
    
    pygame.draw.rect(screen,(255,0,0),[400,200,75,100])
    pygame.draw.rect(screen,(255,0,255),[580,140,135,40])
    textprint("Make run!",647,160)
    pygame.draw.rect(screen,(255,0,123),[580,200,135,40])
    textprint("Make set!",647,220)
    pygame.draw.rect(screen,(0,255,0),[0,500,300,100])
    

    textprint("Computer's cards",160,550)
    pygame.draw.rect(screen,green,[0,130,200,40])

    textprint("Your cards",120,150)
    pygame.draw.rect(screen,(0,255,0),[605,0,200,40])
    
    


    textprint('Score:'+str(score),660,20)
    
    
    


    if check_type(comp)==False:

        for event in pygame.event.get():  #mouse click and arrange cards
            if event.type==pygame.MOUSEBUTTONUP:
                
                

                x,y=pygame.mouse.get_pos()
                sav=0
                
                if ((x >400 and x<475) and (y>200 and y<300)):#to open cards from deck
                    screen.blit(card_l2[0],(200,200))
                    
                
                    pygame.display.update()
                    
                    while not sav:
                        for ev3 in pygame.event.get():
                            if ev3.type==pygame.MOUSEBUTTONUP:
                                
                                print('hi')
                                x1,y1=pygame.mouse.get_pos()
                                if (x1<271 and x1>200) and (y1<296 and y1>200):
                                    print('ho')
                                    sav2=0
                                    while not sav2:
                                        
                                        for ev4 in pygame.event.get():
                                            if ev4.type==pygame.MOUSEBUTTONUP:
                                                print('hey')
                                                x2,y2=pygame.mouse.get_pos()
                                                for i1 in range(len(comp)):
                                                    if x2>i1*20 and x2<20*(i1+1) and y2<100:
                                                        
                                                        

                                                        comp.insert(i1+1,card_l2[0])
                                                        printcard(comp)
                                                        card_l2.remove(card_l2[0])
                                                        
                                                        sav3=0
                                                        while not sav3:
                                                            for ev5 in pygame.event.get():
                                                                if ev5.type==pygame.MOUSEBUTTONUP:
                                                                    x3,y3=pygame.mouse.get_pos()
                                                                    for i12 in range(len(comp)):
                                                                        
                                                                        if x3>i12*20 and x3<20*(i12+1) and y3<100:
                                                                            
                                                                            
                                                                            
                                                                            player_1.append(comp[i12])
                                                                            
                                                                            screen.blit(comp[i12],(200,200))
                                                                            pygame.display.update()
                                                                            comp.remove(comp[i12])
                                                                            printcard(comp)
                                                                            time.sleep(2)
                                                                            screen.blit(player_1[0],(200,200))
                                                                            pygame.display.update()
                                                                            newc=player_1[0]

                                                                            player_1.remove(player_1[0])
                                                                            print_cards(player_1,'p1')
                                                                            
                                                                            
                                                                            
                                                                           
                                                                            sav=1
                                                                            sav2=1
                                                                            sav3=1
                                                                            break
                                                                            
                                                                break    
                                                                    
                                                        break
                                                
                                            break
                            break                     


                elif (x<271 and y>200) and (y<296 and y>200):
                    print('ho')
                    sav2=0
                    while not sav2:
                                        
                        for ev4 in pygame.event.get():
                            if ev4.type==pygame.MOUSEBUTTONUP:
                                print('hey')
                                x2,y2=pygame.mouse.get_pos()
                                for i1 in range(len(comp)):
                                    if x2>i1*20 and x2<20*(i1+1) and y2<100:
                                                        
                                                        

                                        comp.insert(i1+1,newc)
                                        printcard(comp)
                                        #card_l2.remove(card_l2[0])
                                        pygame.draw.rect(screen,(0,255,0),[200,200,71,96])
                                        pygame.display.update()
                                                        
                                        sav3=0
                                        while not sav3:
                                            for ev5 in pygame.event.get():
                                                if ev5.type==pygame.MOUSEBUTTONUP:
                                                    x3,y3=pygame.mouse.get_pos()
                                                    for i12 in range(len(comp)):
                                                                        
                                                        if x3>i12*20 and x3<20*(i12+1) and y3<100:
                                                                            
                                                                            
                                                                            
                                                            player_1.append(comp[i12])
                                                                            
                                                            screen.blit(comp[i12],(200,200))
                                                            pygame.display.update()
                                                            comp.remove(comp[i12])
                                                            printcard(comp)
                                                            time.sleep(2)
                                                            screen.blit(player_1[0],(200,200))
                                                            pygame.display.update()
                                                            newc=player_1[0]

                                                            player_1.remove(player_1[0])
                                                            print_cards(player_1,'p1')
                                                                            
                                                                            
                                                                            
                                                                           
                                                            sav=1
                                                            sav2=1
                                                            sav3=1
                                                            break
                                                                            
                                                break    
                                                                    
                                        break
                                                
                            break
            #break                     
                    
                    
                    


















                for i in range(len(comp)):
                    if (x>i*20 and x<20*(i+1) and y<100):
                        screen.blit(comp[i],(i*20,20))
                        pygame.display.update()
                        
                        
                        while not sav:
                            
                            for ev2 in pygame.event.get():
                                if ev2.type==pygame.MOUSEBUTTONUP:
                                    x1,y1=pygame.mouse.get_pos()
                                    for i1 in range(len(comp)):
                                        if x1>i1*20 and x1<20*(i1+1) and y1<100:
                                            

                                            comp.insert(i1,comp.pop(i))
                                            print(comp)
                                            sav=1
                                            break
                                        
                        break
                        
            
                    elif (x>i*20 and x<20*(i+1) and y>400):
                        screen.blit(player_1[i],(i*20,420))
                        pygame.display.update()
                        
                        
                        while not sav:
                            
                            for ev2 in pygame.event.get():
                                if ev2.type==pygame.MOUSEBUTTONUP:
                                    x11,y11=pygame.mouse.get_pos()
                                    for i11 in range(len(comp)):
                                        if x11>i11*20 and x11<20*(i11+1) and y11>400:
                                            

                                            player_1.insert(i11,player_1.pop(i))
                                            
                                            sav=1
                                            break
                                        

                                    
                            
                        break

                    
                        
            if event.type==KEYDOWN and event.key==K_RSHIFT:
                run=0
                runl=[]
                while not run:
                    for eve in pygame.event.get():
                        if eve.type==MOUSEBUTTONUP:
                            x_1,y_1=pygame.mouse.get_pos()
                            
                                
                            for i in range(len(comp)):
                                    

                                if (x_1>i*20 and x_1<20*(i+1) and y_1<100) and (comp[i] not in runl):
                                    screen.blit(comp[i],(i*20,20))
                                    runl.append(comp[i])
                                    pygame.display.update()
                                    print('ye')
                                    break
                                    
                                elif  (x_1>580 and x_1<715) and (y_1>140 and y_1<180):
                                    

                                    comp=make_run(runl,card_l,comp)
                                    pygame.mixer.music.play()
                                    
                                    
                                    run=1
                                    break
                                    
                              
                                elif (x_1>580 and x_1<715) and (y_1>200 and y_1<240):
                                        
                                    linj(runl,comp)

                                    comp=make_set(runl,card_l)
                                    pygame.mixer.music.play()
                                    
                                    
                                    #print(str(check_type(comp))+'this')
                                        
                                    run=1
                                    break
                        break    
                    
        
    

 
    


    elif check_type(comp)==True and countsets(comp)==1:
        mainl=[]

        for i in comp:
            if type(i)!=list:
                mainl.append(i)
        c=len(comp)-len(mainl)        
        for event in pygame.event.get():  #mouse click and arrange cards
            if event.type==pygame.MOUSEBUTTONUP:
                x,y=pygame.mouse.get_pos()
                sav=0
                
                if ((x >400 and x<475) and (y>200 and y<300)):#to open cards from deck
                    screen.blit(card_l2[0],(200,200))
                    
                
                    pygame.display.update()
                    
                    while not sav:
                        for ev3 in pygame.event.get():
                            if ev3.type==pygame.MOUSEBUTTONUP:
                                
                                print('hi')
                                x1,y1=pygame.mouse.get_pos()
                                if (x1<271 and x1>200) and (y1<296 and y1>200):
                                    print('ho')
                                    sav2=0
                                    while not sav2:
                                        
                                        for ev4 in pygame.event.get():
                                            if ev4.type==pygame.MOUSEBUTTONUP:
                                                print('hey')
                                                x2,y2=pygame.mouse.get_pos()
                                                for i1 in range(len(mainl)):
                                                    if x2>150+i1*20 and x2<150+20*(i1+1) and y2<100:
                                                        c=len(comp)-len(mainl)
                                                        
                                                        
                                                        

                                                        comp.insert(c+i1,card_l2[0])
                                                        printcard(comp)
                                                        card_l2.remove(card_l2[0])
                                                        
                                                        sav3=0
                                                        while not sav3:
                                                            for ev5 in pygame.event.get():
                                                                if ev5.type==pygame.MOUSEBUTTONUP:
                                                                    x3,y3=pygame.mouse.get_pos()
                                                                    for i12 in range(len(mainl)):
                                                                        
                                                                        if x3>150+i12*20 and x3<150+20*(i12+1) and y3<100:
                                                                            
                                                                            
                                                                            
                                                                            player_1.append(comp[c+i12-1])
                                                                            
                                                                            screen.blit(comp[c+i12-1],(200,200))
                                                                            pygame.display.update()
                                                                            comp.remove(comp[c+i12-1])
                                                                            printcard(comp)
                                                                            time.sleep(2)
                                                                            screen.blit(player_1[0],(200,200))
                                                                            pygame.display.update()
                                                                            newc=player_1[0]

                                                                            player_1.remove(player_1[0])
                                                                            print_cards(player_1,'p1')
                                                                            
                                                                            
                                                                            
                                                                           
                                                                            sav=1
                                                                            sav2=1
                                                                            sav3=1
                                                                            break
                                                                            
                                                                break    
                                                                    
                                                        break
                                                
                                            break
                            break                     


                elif (x<271 and y>200) and (y<296 and y>200):
                    print('ho')
                    sav2=0
                    while not sav2:
                                        
                        for ev4 in pygame.event.get():
                            if ev4.type==pygame.MOUSEBUTTONUP:
                                print('hey')
                                x2,y2=pygame.mouse.get_pos()
                                for i1 in range(len(mainl)):
                                    if x2>150+i1*20 and x2<150+20*(i1+1) and y2<100:
                                                        
                                                        

                                        comp.insert(i1+c,newc)
                                        printcard(comp)
                                        #card_l2.remove(card_l2[0])
                                        pygame.draw.rect(screen,(0,255,0),[200,200,71,96])
                                        pygame.display.update()
                                                        
                                        sav3=0
                                        while not sav3:
                                            for ev5 in pygame.event.get():
                                                if ev5.type==pygame.MOUSEBUTTONUP:
                                                    x3,y3=pygame.mouse.get_pos()
                                                    for i12 in range(len(mainl)):
                                                                        
                                                        if x3>150+i12*20 and x3<150+20*(i12+1) and y3<100:
                                                                            
                                                                            
                                                                            
                                                            player_1.append(comp[c+i12-1])
                                                                            
                                                            screen.blit(comp[c+i12-1],(200,200))
                                                            pygame.display.update()
                                                            comp.remove(comp[c+i12-1])
                                                            printcard(comp)
                                                            time.sleep(2)
                                                            screen.blit(player_1[0],(200,200))
                                                            pygame.display.update()
                                                            newc=player_1[0]

                                                            player_1.remove(player_1[0])
                                                            print_cards(player_1,'p1')
                                                                            
                                                                            
                                                                            
                                                                           
                                                            sav=1
                                                            sav2=1
                                                            sav3=1
                                                            break
                                                                            
                                                break    
                                                                    
                                        break
                                                
                            break
            #break                     
                    
                    
                    


















                for i in range(len(comp)):
                    if (x>150+i*20 and x<150+20*(i+1) and y<100):
                        screen.blit(comp[c+i-1],(150+i*20,20))
                        pygame.display.update()
                        
                        
                        while not sav:
                            
                            for ev2 in pygame.event.get():
                                if ev2.type==pygame.MOUSEBUTTONUP:
                                    x1,y1=pygame.mouse.get_pos()
                                    for i1 in range(len(mainl)):
                                        if x1>150+i1*20 and x1<150+20*(i1+1) and y1<100:
                                            

                                            comp.insert(i1,comp.pop(i))
                                            print(comp)
                                            sav=1
                                            break
                                        
                        break
                        
            
                    elif (x>i*20 and x<20*(i+1) and y>400):
                        screen.blit(player_1[i],(i*20,420))
                        pygame.display.update()
                        
                        
                        while not sav:
                            
                            for ev2 in pygame.event.get():
                                if ev2.type==pygame.MOUSEBUTTONUP:
                                    x11,y11=pygame.mouse.get_pos()
                                    for i11 in range(len(comp)):
                                        if x11>i11*20 and x11<20*(i11+1) and y11>400:
                                            

                                            player_1.insert(i11,player_1.pop(i))
                                            
                                            sav=1
                                            break
                                        

                                    
                            
                        break

                    
                        
            if event.type==KEYDOWN and event.key==K_RSHIFT:
                run=0
                runl=[]
                while not run:
                    for eve in pygame.event.get():
                        if eve.type==MOUSEBUTTONUP:
                            x_1,y_1=pygame.mouse.get_pos()
                            
                                
                            for i in range(len(mainl)):
                                    

                                if (x_1>150+i*20 and x_1<150+20*(i+1) and y_1<100) and (comp[c+i-1] not in runl):
                                    screen.blit(comp[c+i-1],(150+i*20,20))
                                    runl.append(comp[c+i-1])
                                    pygame.display.update()
                                    print('ye')
                                    break
                                    
                                elif  (x_1>580 and x_1<715) and (y_1>140 and y_1<180):
                                    

                                    comp=make_run(runl,card_l,comp)
                                    pygame.mixer.music.play()
                                    
                                    run=1
                                    break
                                    
                              
                                elif (x_1>580 and x_1<715) and (y_1>200 and y_1<240):
                                        
                                    linj(runl,comp)

                                    comp=make_set(runl,card_l)
                                    pygame.mixer.music.play()
                                    time.sleep(2)
                                    
                                    print(str(check_type(comp))+'this')
                                        
                                    run=1
                                    break
                        break            
    elif check_type(comp)==True and countsets(comp)==2:
        mainl=[]

        for i in comp:
            if type(i)!=list:
                mainl.append(i)
        c=len(comp)-len(mainl)        
        for event in pygame.event.get():  #mouse click and arrange cards
            if event.type==pygame.MOUSEBUTTONUP:
                x,y=pygame.mouse.get_pos()
                sav=0
                
                if ((x >400 and x<475) and (y>200 and y<300)):#to open cards from deck
                    screen.blit(card_l2[0],(200,200))
                    
                
                    pygame.display.update()
                    
                    while not sav:
                        for ev3 in pygame.event.get():
                            if ev3.type==pygame.MOUSEBUTTONUP:
                                
                                
                                x1,y1=pygame.mouse.get_pos()
                                if (x1<271 and x1>200) and (y1<296 and y1>200):
                                    
                                    sav2=0
                                    while not sav2:
                                        
                                        for ev4 in pygame.event.get():
                                            if ev4.type==pygame.MOUSEBUTTONUP:
                                                
                                                x2,y2=pygame.mouse.get_pos()
                                                for i1 in range(len(mainl)):
                                                    if x2>300+i1*20 and x2<300+20*(i1+1) and y2<100:
                                                        c=len(comp)-len(mainl)
                                                        
                                                        
                                                        

                                                        comp.insert(c+i1-1,card_l2[0])
                                                        printcard(comp)
                                                        card_l2.remove(card_l2[0])
                                                        
                                                        sav3=0
                                                        while not sav3:
                                                            for ev5 in pygame.event.get():
                                                                if ev5.type==pygame.MOUSEBUTTONUP:
                                                                    x3,y3=pygame.mouse.get_pos()
                                                                    for i12 in range(len(mainl)):
                                                                        
                                                                        if x3>300+i12*20 and x3<300+20*(i12+1) and y3<100:
                                                                            
                                                                            
                                                                            
                                                                            player_1.append(comp[c+i12-2])
                                                                            
                                                                            screen.blit(comp[c+i12-2],(200,200))
                                                                            pygame.display.update()
                                                                            comp.remove(comp[c+i12-2])
                                                                            printcard(comp)
                                                                            time.sleep(2)
                                                                            screen.blit(player_1[0],(200,200))
                                                                            pygame.display.update()
                                                                            newc=player_1[0]

                                                                            player_1.remove(player_1[0])
                                                                            print_cards(player_1,'p1')
                                                                            
                                                                            
                                                                            
                                                                           
                                                                            sav=1
                                                                            sav2=1
                                                                            sav3=1
                                                                            break
                                                                            
                                                                break    
                                                                    
                                                        break
                                                
                                            break
                            break                     


                elif (x<271 and y>200) and (y<296 and y>200):
                    print('ho')
                    sav2=0
                    while not sav2:
                                        
                        for ev4 in pygame.event.get():
                            if ev4.type==pygame.MOUSEBUTTONUP:
                                print('hey')
                                x2,y2=pygame.mouse.get_pos()
                                for i1 in range(len(mainl)):
                                    if x2>300+i1*20 and x2<300+20*(i1+1) and y2<100:
                                                        
                                                        

                                        comp.insert(i1+c-1,newc)
                                        printcard(comp)
                                        #card_l2.remove(card_l2[0])
                                        pygame.draw.rect(screen,(0,255,0),[200,200,71,96])
                                        pygame.display.update()
                                                        
                                        sav3=0
                                        while not sav3:
                                            for ev5 in pygame.event.get():
                                                if ev5.type==pygame.MOUSEBUTTONUP:
                                                    x3,y3=pygame.mouse.get_pos()
                                                    for i12 in range(len(mainl)):
                                                                        
                                                        if x3>300+i12*20 and x3<300+20*(i12+1) and y3<100:
                                                                            
                                                                            
                                                                            
                                                            player_1.append(comp[c+i12-2])
                                                                            
                                                            screen.blit(comp[c+i12-2],(200,200))
                                                            pygame.display.update()
                                                            comp.remove(comp[c+i12-2])
                                                            printcard(comp)
                                                            time.sleep(2)
                                                            screen.blit(player_1[0],(200,200))
                                                            pygame.display.update()
                                                            newc=player_1[0]

                                                            player_1.remove(player_1[0])
                                                            print_cards(player_1,'p1')
                                                                            
                                                                            
                                                                            
                                                                           
                                                            sav=1
                                                            sav2=1
                                                            sav3=1
                                                            break
                                                                            
                                                break    
                                                                    
                                        break
                                                
                            break
            #break                     
                    
                    
                    


















                for i in range(len(mainl)):
                    if (x>300+i*20 and x<300+20*(i+1) and y<100):
                        screen.blit(comp[c+i-2],(300+i*20,20))
                        pygame.display.update()
                        
                        
                        while not sav:
                            
                            for ev2 in pygame.event.get():
                                if ev2.type==pygame.MOUSEBUTTONUP:
                                    x1,y1=pygame.mouse.get_pos()
                                    for i1 in range(len(mainl)):
                                        if x1>300+i1*20 and x1<300+20*(i1+1) and y1<100:
                                            

                                            comp.insert(i1,comp.pop(i))
                                            print(comp)
                                            sav=1
                                            break
                                        
                        break
                        
            
                    elif (x>i*20 and x<20*(i+1) and y>400):
                        screen.blit(player_1[i],(i*20,420))
                        pygame.display.update()
                        
                        
                        while not sav:
                            
                            for ev2 in pygame.event.get():
                                if ev2.type==pygame.MOUSEBUTTONUP:
                                    x11,y11=pygame.mouse.get_pos()
                                    for i11 in range(len(comp)):
                                        if x11>i11*20 and x11<20*(i11+1) and y11>400:
                                            

                                            player_1.insert(i11,player_1.pop(i))
                                            
                                            sav=1
                                            break
                                        

                                    
                            
                        break

                    
                        
            if event.type==KEYDOWN and event.key==K_RSHIFT:
                run=0
                runl=[]
                while not run:
                    for eve in pygame.event.get():
                        if eve.type==MOUSEBUTTONUP:
                            x_1,y_1=pygame.mouse.get_pos()
                            
                                
                            for i in range(len(mainl)):
                                    

                                if (x_1>300+i*20 and x_1<300+20*(i+1) and y_1<100) and (comp[c+i-1] not in runl):
                                    screen.blit(comp[c+i-2],(300+i*20,20))
                                    runl.append(comp[c+i-2])
                                    pygame.display.update()
                                    print('ye')
                                    break
                                    
                                elif  (x_1>580 and x_1<715) and (y_1>140 and y_1<180):
                                    

                                    comp=make_run(runl,card_l,comp)
                                    pygame.mixer.music.play()
                                    
                                    
                                    run=1
                                    break
                                    
                              
                                elif (x_1>580 and x_1<715) and (y_1>200 and y_1<240):
                                        
                                    linj(runl,comp)

                                    comp=make_set(runl,card_l)
                                    pygame.mixer.music.play()
                                    
                                    print(str(check_type(comp))+'this')
                                        
                                    run=1
                                    break
                        break            
    elif check_type(comp)==True and countsets(comp)==3:
        mainl=[]

        for i in comp:
            if type(i)!=list:
                mainl.append(i)
        c=len(comp)-len(mainl)        
        for event in pygame.event.get():  #mouse click and arrange cards
            if event.type==pygame.MOUSEBUTTONUP:
                x,y=pygame.mouse.get_pos()
                sav=0
                
                if ((x >400 and x<475) and (y>200 and y<300)):#to open cards from deck
                    screen.blit(card_l2[0],(200,200))
                    
                
                    pygame.display.update()
                    
                    while not sav:
                        for ev3 in pygame.event.get():
                            if ev3.type==pygame.MOUSEBUTTONUP:
                                
                                print('hi')
                                x1,y1=pygame.mouse.get_pos()
                                if (x1<271 and x1>200) and (y1<296 and y1>200):
                                    print('ho')
                                    sav2=0
                                    while not sav2:
                                        
                                        for ev4 in pygame.event.get():
                                            if ev4.type==pygame.MOUSEBUTTONUP:
                                                print('hey')
                                                x2,y2=pygame.mouse.get_pos()
                                                for i1 in range(len(mainl)):
                                                    if x2>450+i1*20 and x2<450+20*(i1+1) and y2<100:
                                                        c=len(comp)-len(mainl)
                                                        
                                                        
                                                        

                                                        comp.insert(c+i1-2,card_l2[0])
                                                        printcard(comp)
                                                        card_l2.remove(card_l2[0])
                                                        
                                                        sav3=0
                                                        while not sav3:
                                                            for ev5 in pygame.event.get():
                                                                if ev5.type==pygame.MOUSEBUTTONUP:
                                                                    x3,y3=pygame.mouse.get_pos()
                                                                    for i12 in range(len(mainl)):
                                                                        
                                                                        if x3>450+i12*20 and x3<450+20*(i12+1) and y3<100:
                                                                            
                                                                            
                                                                            
                                                                            player_1.append(comp[c+i12-3])
                                                                            
                                                                            screen.blit(comp[c+i12-3],(200,200))
                                                                            pygame.display.update()
                                                                            comp.remove(comp[c+i12-3])
                                                                            printcard(comp)
                                                                            time.sleep(2)
                                                                            screen.blit(player_1[0],(200,200))
                                                                            pygame.display.update()
                                                                            newc=player_1[0]

                                                                            player_1.remove(player_1[0])
                                                                            print_cards(player_1,'p1')
                                                                            
                                                                            
                                                                            
                                                                           
                                                                            sav=1
                                                                            sav2=1
                                                                            sav3=1
                                                                            break
                                                                            
                                                                break    
                                                                    
                                                        break
                                                
                                            break
                            break                     


                elif (x<271 and y>200) and (y<296 and y>200):
                    print('ho')
                    sav2=0
                    while not sav2:
                                        
                        for ev4 in pygame.event.get():
                            if ev4.type==pygame.MOUSEBUTTONUP:
                                print('hey')
                                x2,y2=pygame.mouse.get_pos()
                                for i1 in range(len(mainl)):
                                    if x2>450+i1*20 and x2<450+20*(i1+1) and y2<100:
                                                        
                                                        

                                        comp.insert(i1+c-2,newc)
                                        printcard(comp)
                                        #card_l2.remove(card_l2[0])
                                        pygame.draw.rect(screen,(0,255,0),[200,200,71,96])
                                        pygame.display.update()
                                                        
                                        sav3=0
                                        while not sav3:
                                            for ev5 in pygame.event.get():
                                                if ev5.type==pygame.MOUSEBUTTONUP:
                                                    x3,y3=pygame.mouse.get_pos()
                                                    for i12 in range(len(mainl)):
                                                                        
                                                        if x3>450+i12*20 and x3<450+20*(i12+1) and y3<100:
                                                                            
                                                                            
                                                                            
                                                            player_1.append(comp[c+i12-3])
                                                                            
                                                            screen.blit(comp[c+i12-3],(200,200))
                                                            pygame.display.update()
                                                            comp.remove(comp[c+i12-3])
                                                            printcard(comp)
                                                            time.sleep(2)
                                                            screen.blit(player_1[0],(200,200))
                                                            pygame.display.update()
                                                            newc=player_1[0]

                                                            player_1.remove(player_1[0])
                                                            print_cards(player_1,'p1')
                                                                            
                                                                            
                                                                            
                                                                           
                                                            sav=1
                                                            sav2=1
                                                            sav3=1
                                                            break
                                                                            
                                                break    
                                                                    
                                        break
                                                
                            break
            #break                     
                    
                    
                    


















                for i in range(len(mainl)):
                    if (x>450+i*20 and x<450+20*(i+1) and y<100):
                        screen.blit(comp[c+i-3],(450+i*20,20))
                        pygame.display.update()
                        
                        
                        while not sav:
                            
                            for ev2 in pygame.event.get():
                                if ev2.type==pygame.MOUSEBUTTONUP:
                                    x1,y1=pygame.mouse.get_pos()
                                    for i1 in range(len(mainl)):
                                        if x1>450+i1*20 and x1<450+20*(i1+1) and y1<100:
                                            

                                            comp.insert(i1,comp.pop(i))
                                            print(comp)
                                            sav=1
                                            break
                                        
                        break
                        
            
                    elif (x>i*20 and x<20*(i+1) and y>400):
                        screen.blit(player_1[i],(i*20,420))
                        pygame.display.update()
                        
                        
                        while not sav:
                            
                            for ev2 in pygame.event.get():
                                if ev2.type==pygame.MOUSEBUTTONUP:
                                    x11,y11=pygame.mouse.get_pos()
                                    for i11 in range(len(comp)):
                                        if x11>i11*20 and x11<20*(i11+1) and y11>400:
                                            

                                            player_1.insert(i11,player_1.pop(i))
                                            
                                            sav=1
                                            break
                                        

                                    
                            
                        break

                    
                        
            if event.type==KEYDOWN and event.key==K_RSHIFT:
                run=0
                runl=[]
                while not run:
                    for eve in pygame.event.get():
                        if eve.type==MOUSEBUTTONUP:
                            x_1,y_1=pygame.mouse.get_pos()
                            
                                
                            for i in range(len(mainl)):
                                    

                                if (x_1>450+i*20 and x_1<450+20*(i+1) and y_1<100) and (comp[c+i-1] not in runl):
                                    screen.blit(comp[c+i-3],(450+i*20,20))
                                    runl.append(comp[c+i-3])
                                    pygame.display.update()
                                    print('ye')
                                    break
                                    
                                elif  (x_1>580 and x_1<715) and (y_1>140 and y_1<180):
                                    

                                    comp=make_run(runl,card_l,comp)
                                    pygame.mixer.music.play()
                                    
                                    
                                    run=1
                                    break
                                    
                              
                                elif (x_1>580 and x_1<715) and (y_1>200 and y_1<240):
                                        
                                    linj(runl,comp)

                                    comp=make_set(runl,card_l)
                                    pygame.mixer.music.play()
                                    
                                    print(str(check_type(comp))+'this')
                                        
                                    run=1
                                    break
                        break                            
    pygame.display.update()
    clk.tick(60)
    

