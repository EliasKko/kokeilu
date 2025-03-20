import pygame
import random
import time


pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load('music.wav')
pygame.mixer.music.set_volume(0.7)

sound = pygame.mixer.Sound('boom.wav')
sound1 = pygame.mixer.Sound('bomb.wav')
sound2 = pygame.mixer.Sound('mario.wav')
sound3 = pygame.mixer.Sound('start.wav')
sound4 = pygame.mixer.Sound('rage.wav')
sound5 = pygame.mixer.Sound('over.wav')
soun6 = pygame.mixer.Sound('win.wav')
soun7 = pygame.mixer.Sound('fiuu.wav')
lokki = pygame.mixer.Sound('seagull.wav')
fontti = pygame.font.SysFont('rage', 100)
fontti1 = pygame.font.SysFont('kaiti', 40)
teksti = fontti.render('Lentominipeli', False,(170,20,0))
teksti1 = fontti1.render('peliä pelataan nuolinäppäimillä, paina ENTER aloittaaksesi', False, (1,0,0))
pygame.display.set_caption("Fuck Ass Ni99a")
kello = pygame.time.Clock()
peli = pygame.display.set_mode((1000, 500))
leveys = 0
velo = 0.1
velo2 = -0.1
lentokone = pygame.image.load('pngegg.png')
Vasemmalle = pygame.image.load('pngeggL.png')
Oikealle = pygame.image.load('pngeggR.png')
räjähdys = pygame.image.load('boom.png')
räjähdys = pygame.transform.scale(räjähdys,(100,50))
lintu1 = pygame.image.load('bird1.png')
lintu1 = pygame.transform.scale(lintu1,(100,50))
lintu2 = pygame.image.load('bird2.png')
lintu2 = pygame.transform.scale(lintu2,(100,50))
tausta = pygame.image.load('tausta1.jpg')
tausta = pygame.transform.scale(tausta,(1000,500))
go = pygame.image.load('youdied.jpg')
go = pygame.transform.scale(go,(600,300))
gg = pygame.image.load('courseclear.jpg')
gg = pygame.transform.scale(gg,(600,300))
cld = pygame.image.load('cloud1.png')
wtc = pygame.image.load('New_WTC.png')

class pelaaja(object):
    def __init__(self):
        self.x = 40
        self.y = 40
        self.vel = 7
        self.säde = 20
        self.health = 150
        self.oikea = False
        self.vasen = False
        self.ylös = False
        self.alas = False
        self.paikallaan = True
        self.hitbox = (self.x + 200,self.y + 200,28,40)

    def piirrä(self,peli):
        if self.paikallaan:
            peli.blit(lentokone, (self.x,self.y))
            self.hitbox = (self.x + 190, self.y + 230, 70, 50)
        if not(self.paikallaan):
            if self.vasen:
                peli.blit(Vasemmalle, (self.x,self.y))
                self.hitbox = (self.x + 190, self.y + 330, 70, 50)
            elif self.oikea:
                peli.blit(Oikealle, (self.x,self.y))
                self.hitbox = (self.x + 190, self.y + 330, 70, 50)
            else:
                peli.blit(lentokone, (self.x,self.y))
                self.hitbox = (self.x + 190, self.y + 230, 70, 50)
        else:
            if self.vasen:
                peli.blit(Vasemmalle, (self.x, self.y))
                self.hitbox = (self.x + 190, self.y + 330, 70, 50)
            elif self.oikea:
                peli.blit(Oikealle, (self.x, self.y))
                self.hitbox = (self.x + 1900, self.y + 330, 70, 50)
        #self.hitbox = (self.x + 200, self.y + 300, 50, 40)
        #pygame.draw.rect(peli,(255,0,0),self.hitbox,1)

class towers(object):
    def __init__(self):
        self.x = 250
        self.y = 450
        self.vel = 0.4
        self.vel2 = 0.01
        self.vel1 = 3
        self.ole = False
        self.koko = 550
        self.koko1 = 500
        self.start_ticks=pygame.time.get_ticks()
        self.alkukuva = pygame.image.load('New_WTC.png')
        self.kuva = pygame.transform.scale(self.alkukuva, (self.koko, self.koko1))
        self.räjähdys = pygame.image.load('boom.png')
        self.räjähdys = pygame.transform.scale(self.räjähdys, (190, 40))

    def kasvu(self):
        self.seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
        if self.seconds > 10:
            self.ole = True
        if self.ole and self.y >= 100:
            if self.seconds < 20:
                self.y -= self.vel
            self.seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
            if self.seconds > 20:
                peli.blit(self.räjähdys, (self.x+170, self.y+200))
                peli.blit(self.räjähdys, (self.x + 300, self.y + 200))
            if self.seconds > 23:
                self.y += self.vel1
                self.x += self.vel
                if self.x >= 253:
                    self.x -= 3

    def piirrä(self,peli):
        if self.ole:
            peli.blit(self.kuva, (self.x,self.y))




class cloud(object):
    def __init__(self,x,y,vel,size):
        self.x = x
        self.y = y
        self.vel = vel
        self.size = size
        self.ole = True
        self.pic = pygame.image.load('cloud1.png')


    def liikku(self):
        if self.ole and  self.x <= 1000:
            self.x += self.vel
            if self.x >= 1000:
                self.ole = False
    def piirrä(self):
        self.pic = pygame.transform.scale(self.pic, (self.size, self.size/2))
        if self.ole:
            peli.blit(self.pic, (self.x,self.y))



class lintu(object):
    def __init__(self,y):
        self.x = -1000
        self.y = y
        self.vel1 = 100
        self.vel = 5
        self.flapcount = 1
        self.spawncount = 0
        self.olemassa = True
        self.rect = pygame.Rect(self.x + 33, self.y + 2, 40, 40)
        #self.rect = (self.x + 33, self.y + 2, 40, 40)

    def lento(self):
        if self.olemassa and self.x <= 1000:
            self.x += self.vel
            self.flapcount += self.vel1
            self.rect = pygame.Rect(self.x + 33, self.y + 2, 40, 40)
            if self.x >= 1000:
                self.olemassa = False

    def piirrä(self,peli):
        if self.olemassa:
            if self.flapcount >= 2000:
                self.flapcount -= 2000
            elif self.flapcount <= 1000:
                peli.blit(lintu1, (self.x,self.y))
            elif self.flapcount >= 1000:
                peli.blit(lintu2, (self.x,self.y))

class kivi(object):
    def __init__(self,x,y):
        self.alkuperäinenkuva = pygame.image.load('kivi.png')
        self.x = x
        self.y = y
        self.x1 = 1
        self.maxkoko = 270
        self.vel = 5
        self.olemassa = True
        self.rect = pygame.Rect(self.x + 2, self.y + 2, self.x1, self.x1)
        self.kuva = pygame.transform.scale(self.alkuperäinenkuva, (self.x1, self.x1))


    def kasvu(self):
        if self.olemassa and self.x1 < self.maxkoko:
            self.x1 += self.vel
            self.kuva = pygame.transform.scale(self.alkuperäinenkuva, (self.x1,self.x1))
            #self.rect = pygame.draw.ellipse(peli, (255,0,0),(self.x+2, self.y+2, self.x1, self.x1),1)
            self.rect = pygame.Rect(self.x + 2, self.y + 2, self.x1, self.x1)
            if self.x1 >= self.maxkoko:
                self.olemassa = False

    def piirrä(self,peli):
        if self.olemassa:
            peli.blit(self.kuva, (self.x,self.y))


def uusipilvi():
    kaks = random.randint(10, 400)
    yks1 = random.randint(100, 600)
    neljä = random.randint(1, 9)
    return cloud(-190, kaks, neljä, yks1)


def uusikivi():
    yks = random.randint(100, 700)
    kaks = random.randint(-100, 430)
    soun7.play()
    return kivi(yks,kaks)

def uusilintu():
    yks = random.randint(100,400)
    return lintu(yks)

def taustapiirto():
    peli.blit(tausta, (leveys, leveys))
    pilvi1.liikku()
    pilvi1.piirrä()
    pilvi2.liikku()
    pilvi2.piirrä()
    tornit.kasvu()
    tornit.piirrä(peli)
    murikka.piirrä(peli)
    murikka.kasvu()
    birdie.lento()
    birdie.piirrä(peli)
    lentäjä.piirrä(peli)
    pygame.display.update()

törmäysetäisyys = 200
yks = random.randint(100,400)
kaks = random.randint(100,400)
yks1 = random.randint(100,300)
kaks1 = random.randint(300,500)
kolme = random.randint(-100,40)
kolme1 = random.randint(-100,40)
neljä = random.randint(1,7)
neljä1 = random.randint(1,4)
lentäjä = pelaaja()
pilvi1 = uusipilvi()
pilvi2 = uusipilvi()
tornit = towers()

start_ticks=pygame.time.get_ticks()
musiik = False
run = False
startscreen = True
while startscreen:
    musiik = True
    peli.blit(tausta,(0, 0))
    peli.blit(teksti, (100, 60))
    peli.blit(teksti1, (70, 190))
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000

    if seconds <2:
        sound3.play()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        startscreen = False
        run = True
if musiik == True:
    pygame.mixer.music.play(0)

murikka = uusikivi()
birdie = uusilintu()

while run:
    kello.tick(60)
    leveys += velo
    if leveys >= 2:
        leveys -= 2
        pygame.display.update()



    pygame.display.update()
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    taustapiirto()
    if seconds > 20 and seconds < 22:
        sound1.play()
    if seconds > 33:
        peli.blit(gg, (200, 100))
        soun6.play(0)
        pygame.display.update()
        time.sleep(4)
        run = False
    if not pilvi1.ole:
        pilvi1 = uusipilvi()
    if not pilvi2.ole:
        pilvi2 = uusipilvi()
    if not murikka.olemassa:
        murikka = uusikivi()
    if not birdie.olemassa:
        birdie = uusilintu()
    if lentäjä.health <= 1:
        peli.blit(go, (200, 100))
        pygame.display.update()
        sound4.play()
        sound5.play()
        time.sleep(3)
        run = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if birdie.rect.colliderect(lentäjä.hitbox):
        print("hit")
        sound.play()
        lentäjä.health -= 5
        print(lentäjä.health)
        for i in range(70):
            peli.blit(räjähdys, (lentäjä.x + 150, lentäjä.y + 270))
            peli.blit(räjähdys, (lentäjä.x + 199, lentäjä.y + 250))
            pygame.display.update()
    if murikka.x1 >= törmäysetäisyys and murikka.rect.colliderect(lentäjä.hitbox):
        print("hit")
        sound.play()
        lentäjä.health -= 30
        print(lentäjä.health)
        murikka.olemassa = False
        for i in range(300):
            peli.blit(räjähdys, (lentäjä.x + 150, lentäjä.y + 270))
            peli.blit(räjähdys, (lentäjä.x + 199, lentäjä.y + 250))
            pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        lentäjä.x -= lentäjä.vel
        lentäjä.paikallaan = False
        lentäjä.oikea = False
        lentäjä.vasen = True
    elif keys[pygame.K_RIGHT]:
        lentäjä.x += lentäjä.vel
        lentäjä.paikallaan = False
        lentäjä.vasen = False
        lentäjä.oikea = True
    else:
        lentäjä.oikea = False
        lentäjä.vasen = False

    if keys[pygame.K_UP]:
        lentäjä.y -= lentäjä.vel
        lentäjä.ylös = True
        lentäjä.alas = False
    elif keys[pygame.K_DOWN]:
        lentäjä.y += lentäjä.vel
        lentäjä.alas = True
        lentäjä.ylös = False
    else:
        lentäjä.ylös = False
        lentäjä.alas = False





pygame.quit()