import pygame
import random
import time

from soupsieve.util import lower

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('enemy.wav')
sound = pygame.mixer.Sound('boom.wav')
sound5 = pygame.mixer.Sound('over.wav')
sound2 = pygame.mixer.Sound('wait.wav')
soun6 = pygame.mixer.Sound('win.wav')
soun7 = pygame.mixer.Sound('fiuu.wav')
sound9 = pygame.mixer.Sound('blaster.wav')
pygame.display.set_caption("Fuck Ass Ni99a")
fontti1 = pygame.font.SysFont('kaiti', 40)
entre = fontti1.render('press ENTER to continue', False, (255,255,255))
SPEIS = fontti1.render('press SPACE to continue', False, (255,0,255))
teksti1 = fontti1.render('Im going to kill you!', False, (255,0,0))
teksti2 = fontti1.render('you wont survive the next attack', False, (255,0,0))
teksti3 = fontti1.render('try to dodge this', False, (255,0,0))
teksti4 = fontti1.render('that wasnt all', False, (255,0,0))
teksti5 = fontti1.render('next one is my SPECIAL MOVE', False, (255,0,0))
teksti6 = fontti1.render('alright I give up...', False, (255,0,0))
teksti7 = fontti1.render('SIKE', False, (255,0,0))
teksti8 = fontti1.render('okay okay you won', False, (255,0,0))
teksti9 = fontti1.render('check this out', False, (255,0,0))
kello = pygame.time.Clock()
bossfight = pygame.display.set_mode((1000, 500))
tausta = pygame.image.load('back.png')
tausta = pygame.transform.scale(tausta,(1000,500))
heart = pygame.image.load('heart.png')
heart = pygame.transform.scale(heart,(100,100))
go = pygame.image.load('youdied.jpg')
go = pygame.transform.scale(go,(600,300))
gg = pygame.image.load('courseclear.jpg')
gg = pygame.transform.scale(gg,(600,300))
#knife1 = pygame.image.load('knife.png')
#knife1 = pygame.transform.scale(knife1,(300,150))
#knife1 = pygame.transform.rotate(knife1,125)
boss = pygame.image.load('enemy.png')
boss = pygame.transform.scale(boss,(200,150))
blaster = [pygame.image.load('blaster1.png'),pygame.image.load('blaster2.png'),pygame.image.load('blaster3.png')]

class rock(object):
    def __init__(self,x,vel):
        self.x = x
        self.y = 20
        self.olemassa = True
        self.vel = vel
        self.rect = pygame.Rect(self.x, self.y - 10, 30, 20)
        self.kuva = pygame.image.load('kivi.png')
        self.kuva = pygame.transform.scale(self.kuva, (30, 15))
        #self.start_ticks = pygame.time.get_ticks()
        #self.seconds = (pygame.time.get_ticks() - start_ticks) / 1000

    def rain(self):
        if self.olemassa and self.y <= 500:
            self.vel += 0.2
            self.y += self.vel
            self.rect = pygame.Rect(self.x, self.y-10, 30, 20)
            #pygame.draw.rect(bossfight, (255, 0, 0), (self.rect1), 2)
            if self.y >= 400:
                self.olemassa = False




    def piirrä(self):
        if self.olemassa:
            self.rect = pygame.Rect(self.x, self.y - 10, 30, 20)
            bossfight.blit(self.kuva, (self.x, self.y))

def uusrock():
    yks = random.randint(400, 550)
    return rock(yks,2)
def uusrock2():
    yks = random.randint(400, 550)
    return rock(yks,10)

class knife(object):
    def __init__(self,x,vel,vel1):
        self.x = x
        self.y = 40
        self.x1 = 600
        self.y1 = 190
        self.vel = vel
        self.vel1 = vel1
        self.vel2 = 7
        self.vel3 = 3.5
        self.vel4 = -3.5
        self.kuva = pygame.image.load('knife.png')
        self.kuva = pygame.transform.scale(self.kuva, (300, 150))
        self.kuva = pygame.transform.rotate(self.kuva, 130)
        self.rect = pygame.Rect(self.x, self.y, 300, 150)
        self.oikealle = True
        self.vasemmalle = False
        self.olemassa = True
        self.alas = True
        self.ylös = False
        self.sivuun = False
        self.sivuun1 = False


    def cut(self):
        if self.oikealle and self.x < 600:
            self.vel += 0.1
            self.x += self.vel
            if self.x <= 200:
                soun7.play()
            if self.x >= 600:
                self.y += 200
                self.kuva = pygame.transform.flip(self.kuva, True, True)
                self.oikealle = False
                self.vasemmalle = True
        if self.vasemmalle and self.x > 10:
            if self.x > 500:
                soun7.play()
            self.vel1 -= 0.1
            self.x += self.vel1
            if self.x <= 10:
                self.olemassa= False

    def cut2(self):
        #self.oikealle = False
        #self.x = 300
        if self.alas:
            soun7.play()
            self.vel += 7
            self.y += self.vel
            if self.y >= 200:
                self.ylös = True
                self.alas = False
        if self.ylös and self.y > -60:
            soun7.play()
            self.vel1 -= 1
            self.y += self.vel1
            if self.y < -60:
                self.ylös = False
                self.sivuun = True
        if self.sivuun and self.x <= 400:
            self.x += self.vel2
            if self.x >= 400:
                self.sivuun = False
                self.alas = True


    def cut3(self):
        if self.oikealle:
            self.x += self.vel3
            self.x1 += self.vel4
            if self.x >= 600:
                self.oikealle = False
                self.vasemmalle = True
        if self.vasemmalle and self.x > 10:
            #self.kuva = pygame.transform.rotate(self.kuva, 2)
            self.x += self.vel4
            self.x1 += self.vel3
            if self.x <= 10:
                self.olemassa= False





    def piirrä(self):
        if self.olemassa:
            self.rect = pygame.Rect(self.x + 140, self.y + 80, 35, 190)
            #pygame.draw.rect(bossfight,(255,0,0),(self.rect),2)
            bossfight.blit(self.kuva, (self.x, self.y))
            if self.x > 690:
                self.kuva = pygame.transform.flip(self.kuva, True, True)



    def piirrä2(self):
        if self.olemassa:
            soun7.play()
            self.kuva = pygame.transform.rotate(self.kuva, 90)
            self.rect = pygame.Rect(self.x + 140, self.y + 100, 35, 50)
            self.rec1t = pygame.Rect(self.x1 + 140, self.y1 + 100, 35, 50)
            #pygame.draw.rect(bossfight, (255, 0, 0), (self.rect), 2)
            #pygame.draw.rect(bossfight, (255, 0, 0), (self.rec1t), 2)
            bossfight.blit(self.kuva, (self.x, self.y))
            bossfight.blit(self.kuva, (self.x1, self.y1))
            if self.x >= 590:
                self.kuva = pygame.transform.flip(self.kuva, True, True)
                self.y += 30
                self.y1 -= 30




class platform(object):
    def __init__(self):
        self.x = 400
        self.y = 200
        self.rect = pygame.Rect(self.x, self.y, 200, 200)

    def piirrä(self):
        self.rect = pygame.Rect(self.x, self.y, 200, 200)
        pygame.draw.rect(bossfight,(255,255,255),(self.rect),1)

class soul(object):
    def __init__(self):
        self.x = 500
        self.y = 200
        self.health = 7000000
        self.vel = 4
        self.oikea = False
        self.vasen = False
        self.ylös = False
        self.alas = False
        self.paikallaan = True
        self.hitbox = (self.x,self.y,28,40)

    def piirrä(self):
        bossfight.blit(heart, (self.x, self.y))
        self.hitbox = pygame.Rect(self.x+45, self.y+45, 19, 19)
        #pygame.draw.rect(bossfight,(255,0,0),(self.hitbox),2)

class timer(object):
    def __init__(self,vel):
        self.going = True
        self.x1 = 10
        self.y1 = 10
        self.vel = vel
        self.rect1 = pygame.Rect(self.x1, self.y1, 30, 20)

    def tik(self):
        if self.going and self.y1 <= 500:
            self.y1 += self.vel
            self.rect1 = pygame.Rect(self.x1, self.y1, 30, 20)
            #pygame.draw.rect(bossfight, (255, 0, 0), (self.rect1), 2)
            if self.y1 >= 500:
                self.going = False

class gasterblaster(object):
    def __init__(self,x,vel1):
        self.x = x
        self.y = 100
        self.counter = 0
        self.vel = 0.08
        self.vel1 = vel1
        self.vel2 = 20
        self.ole = True
        self.var = 1
        self.rect = pygame.Rect(self.x + 17, self.y + 20, 10, self.var)

    def piirrä(self):
        if self.ole and self.counter < 10:
            self.var += self.vel2
            self.counter += self.vel
            if self.counter >= 0 and self.counter < 1:
                bossfight.blit(blaster[0],(self.x,self.y))
            if self.counter >= 1 and self.counter < 2:
                bossfight.blit(blaster[1],(self.x,self.y))
            if self.counter >= 2 and self.counter < 10:
                self.rect = pygame.Rect(self.x+17, self.y+20, 10, self.var)
                pygame.draw.rect(bossfight, (255, 255, 255), (self.rect))
                bossfight.blit(blaster[2],(self.x,self.y))
                self.x += self.vel1
            if self.counter >= 7:
                self.var = 1
                self.ole = False

def uusblaster():
    yks = random.randint(400,550)
    if yks >= 500:
        kaks = -2
    elif yks <= 450:
        kaks = 2
    else:
        kaks = random.uniform(-0.3,0.3)
    sound9.play()
    return gasterblaster(yks,kaks)



def background():
    bossfight.blit(tausta, (0, 0))
    bossfight.blit(boss, (400, 30))
    plattis.piirrä()
    bossfight.blit(entre, (350, 410))
    pygame.display.update()

def background2():
    bossfight.blit(tausta, (0, 0))
    bossfight.blit(boss, (400, 30))
    plattis.piirrä()
    bossfight.blit(SPEIS, (350, 410))
    pygame.display.update()

def attack1():
    bossfight.blit(tausta, (0, 0))
    bossfight.blit(boss, (400, 30))
    plattis.piirrä()
    sielu.piirrä()
    veitsi.cut()
    veitsi.piirrä()
    pygame.display.update()


def attack2():
    bossfight.blit(tausta, (0, 0))
    bossfight.blit(boss, (400, 30))
    plattis.piirrä()
    sielu.piirrä()
    tiktok.tik()
    kivi.rain()
    kivi.piirrä()
    pygame.display.update()

def attack3():
    bossfight.blit(tausta, (0, 0))
    bossfight.blit(boss, (400, 30))
    plattis.piirrä()
    sielu.piirrä()
    tiktok1.tik()
    veitsi1.cut2()
    veitsi1.piirrä()
    pygame.display.update()

def attack4():
    bossfight.blit(tausta, (0, 0))
    bossfight.blit(boss, (400, 30))
    plattis.piirrä()
    sielu.piirrä()
    tiktok2.tik()
    kivi1.rain()
    kivi1.piirrä()
    pygame.display.update()

def attack5():
    bossfight.blit(tausta, (0, 0))
    bossfight.blit(boss, (400, 30))
    plattis.piirrä()
    sielu.piirrä()
    veitsi2.cut3()
    veitsi2.piirrä2()
    pygame.display.update()

def attack6():
    bossfight.blit(tausta, (0, 0))
    bossfight.blit(boss, (400, 30))
    plattis.piirrä()
    sielu.piirrä()
    veitsi3.cut()
    veitsi3.piirrä()
    pygame.display.update()

def attack7():
    bossfight.blit(tausta, (0, 0))
    bossfight.blit(boss, (400, 30))
    plattis.piirrä()
    sielu.piirrä()
    tiktok3.tik()
    gasteri.piirrä()
    pygame.display.update()

leveys = 400
leveys1 = 170
velo = 0.2
start_ticks=pygame.time.get_ticks()
veitsi = knife(10,0.01,(-0.01))
veitsi1 = knife(300,0.01,(-0.01))
veitsi2 = knife(10,0.01,(-0.01))
veitsi3 = knife(10,15,(-15))
sielu = soul()
plattis = platform()
yks = random.randint(450, 500)
kivi = uusrock()
kivi1 = uusrock2()
tiktok =  timer(1)
tiktok1 =  timer(4)
tiktok2 =  timer(0.8)
tiktok3 =  timer(0.6)

run = False

state = True
one = False
state1 = False
two = False
state2 = False
three = False
state3 = False
four = False
state4 = False
five = False
state5 = False
state6 = False
six = False
state7 = False
seven = False
state8 = False
musa = False
start_ticks=pygame.time.get_ticks()
while state:
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    if seconds < 3:
        sound2.play()
    pygame.display.update()
    kello.tick(100)
    leveys += velo
    leveys1 += velo
    if leveys >= 403:
        leveys -= 3
        leveys1 -= 3
        pygame.display.update()
    background()
    bossfight.blit(teksti1, (leveys, leveys1))
    pygame.display.update()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    if keys[pygame.K_RETURN]:
        state = False
        run = True
        yks = True
        musa = True
if musa:
    pygame.mixer.music.play(0)
gasteri = uusblaster()
while run:
    kello.tick(60)
    leveys += velo
    leveys1 += velo
    if leveys >= 403:
        leveys -= 3
        leveys1 -= 3
        pygame.display.update()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not state and yks:
        attack1()
        if not veitsi.olemassa:
            yks = False
            state1 = True

    if state1 and not yks:
        background()
        bossfight.blit(teksti2, (leveys, leveys1))
        pygame.display.update()
    if keys[pygame.K_RETURN] and state1:
        state1 = False
        two = True
    if not state1 and two:
        attack2()
        if not tiktok.going:
            two = False
            state2 = True

    if state2 and not two:
        background()
        bossfight.blit(teksti3, (leveys, leveys1))
        pygame.display.update()
    if keys[pygame.K_RETURN] and state2:
        state2 = False
        three = True
    if not state2 and three:
        attack3()
        if not tiktok1.going:
            three = False
            state3 = True

    if state3 and not three:
        background()
        bossfight.blit(teksti4, (leveys, leveys1))
        pygame.display.update()
    if keys[pygame.K_RETURN] and state3:
        state3 = False
        four = True
    if not state3 and four:
        attack4()
        if not tiktok2.going:
            four = False
            state4 = True

    if state4 and not four:
        background()
        bossfight.blit(teksti5, (leveys, leveys1))
        pygame.display.update()
    if keys[pygame.K_RETURN] and state4:
        state4 = False
        five = True
    if not state4 and five:
        attack5()
        if not veitsi2.olemassa:
            five = False
            state5 = True

    if state5 and not five:
        background()
        bossfight.blit(teksti6, (leveys, leveys1))
        pygame.display.update()
    if keys[pygame.K_RETURN] and state5:
        state5 = False
        state6 = True
    if state6 and not state5:
        background2()
        bossfight.blit(teksti7, (leveys, leveys1))
        pygame.display.update()
    if keys[pygame.K_SPACE] and state6:
        state6 = False
        six = True
    if six and not state6:
        attack6()
        if not veitsi3.olemassa:
            six = False
            state7 = True
    if state7 and not six:
        background()
        bossfight.blit(teksti9, (leveys, leveys1))
        pygame.display.update()
    if keys[pygame.K_RETURN] and state7:
        state7 = False
        seven = True
    if seven and not state7:
        attack7()
        if not tiktok3.going:
            seven = False
            state8 = True
    if state8 and not seven:
        background()
        bossfight.blit(teksti8, (leveys, leveys1))
        pygame.display.update()
    if keys[pygame.K_RETURN] and state8:
        bossfight.blit(gg, (200, 100))
        soun6.play(0)
        pygame.display.update()
        time.sleep(4)
        run = False


    if not kivi.olemassa and tiktok.going:
        kivi = uusrock()

    if not kivi1.olemassa and tiktok2.going:
        kivi1= uusrock2()

    if not gasteri.ole and tiktok3.going:
        gasteri = uusblaster()


    if veitsi.rect.colliderect(sielu.hitbox):
        sielu.health -= 100
        print("hit")
        print(sielu.health)
        sound.play()

    if gasteri.rect.colliderect(sielu.hitbox):
        sielu.health -= 50
        print("hit")
        print(sielu.health)
        sound.play()

    if veitsi1.rect.colliderect(sielu.hitbox):
        sielu.health -= 100
        print("hit")
        print(sielu.health)

        sound.play()

    if veitsi2.rect.colliderect(sielu.hitbox):
        sielu.health -= 2
        print("hit")
        print(sielu.health)
        sound.play()

    if veitsi3.rect.colliderect(sielu.hitbox):
        sielu.health -= 200
        print("hit")
        print(sielu.health)
        sound.play()

    if kivi.rect.colliderect(sielu.hitbox):
        print("hit")
        sielu.health -= 40
        print(sielu.health)
        sound.play()
        kivi.olemassa = False

    if kivi1.rect.colliderect(sielu.hitbox):
        print("hit")
        sielu.health -= 70
        print(sielu.health)
        sound.play()
        kivi.olemassa = False

    if sielu.health <= 1:
        bossfight.blit(go, (200, 100))
        pygame.display.update()
        sound5.play()
        time.sleep(3)
        run = False

    if keys[pygame.K_LEFT]:
        sielu.x -= sielu.vel
        sielu.paikallaan = False
        sielu.oikea = False
        sielu.vasen = True
    if plattis.rect.colliderect(sielu.hitbox) and sielu.x >= plattis.x + 130:
        sielu.vasen = False
    elif keys[pygame.K_RIGHT]:
        sielu.x += sielu.vel
        sielu.paikallaan = False
        sielu.vasen = False
        sielu.oikea = True
    if plattis.rect.colliderect(sielu.hitbox) and sielu.x <= plattis.x - 41:
        sielu.x += sielu.vel
    else:
        sielu.oikea = False
        sielu.vasen = False

    if keys[pygame.K_UP]:
        sielu.y -= sielu.vel
        sielu.ylös = True
        sielu.alas = False
    if plattis.rect.colliderect(sielu.hitbox) and sielu.y >= plattis.y + 130:
        sielu.ylös = False
    elif keys[pygame.K_DOWN]:
        sielu.y += sielu.vel
        sielu.alas = True
        sielu.ylös = False
    if plattis.rect.colliderect(sielu.hitbox) and sielu.y <= plattis.y - 41:
        sielu.y += sielu.vel

    else:
        sielu.ylös = False
        sielu.alas = False





