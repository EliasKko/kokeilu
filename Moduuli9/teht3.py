class Auto:
    def __init__(self, rekisterinumero="ABC-123", huippunopeus="142km/h", nopeus=60, kuljettu_matka=2000, kiihdytys=0):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka
        self.kiihdytys = kiihdytys

    def kiihtyy(self):
        a = int(input("anna kiihdytys: "))
        self.kiihdytys=a
        if self.kiihdytys != 0 and self.nopeus < 142:
            self.nopeus = self.nopeus + self.kiihdytys
            if self.nopeus < 0:
                self.nopeus = 0
            elif self.nopeus > 142:
                self.nopeus = 142

    def kulje(self):
        a = int(input("Anna matkan tuntimäärä: "))
        if a != 0:
            self.kuljettu_matka = self.kuljettu_matka + a * self.nopeus
            print("Matkaa on kulunut: ", self.kuljettu_matka, "km")

auto = Auto()
auto.kulje()