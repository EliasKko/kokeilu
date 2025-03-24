import random

class Kilpailu:
    def __init__(self,osallistujat):
        self.kilpailun_nimi = "Suuri romuralli"
        self.pituus = 8000
        self.osallistujat = []

    def tuntikuluu(self):
        for i in range(len(self.osallistujat)):
            self.osallistujat[len(self.osallistujat)].kulje(10)


    def tulostatilanne(self):

    def kisaohi(self):

class Auto:
    def __init__(self,nimi,huippunopeus):
        self.nimi = nimi
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihtyy(self, kiihty):
        for i in range(kiihty):
            if kiihty != 0 and self.nopeus < self.huippunopeus:
                self.nopeus = self.nopeus + kiihty
                if self.nopeus < 0:
                    self.nopeus = 0
                elif self.nopeus > self.huippunopeus:
                    self.nopeus == self.huippunopeus
        return

    def kulje(self, matka):
        for i in range(matka):
            if matka != 0 and self.kuljettu_matka <= 10000:
                self.kuljettu_matka = self.kuljettu_matka + matka * self.nopeus
        if self.kuljettu_matka >= 10000:
            print(self.rekisterinumero, "maalissa")
        return
osallistujat = 10
Race = Kilpailu(osallistujat)
for i in range(osallistujat):
    Race.osallistujat.append(Auto((len(Race.osallistujat)), random.randint(100,200)))
