class Auto:
    def __init__(self, rekisterinumero="ABC-123", huippunopeus="142km/h", nopeus=0, kuljettu_matka=0, kiihdytys=0):
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

print("[Huom. Nopeuden muutos tehdään tässä manuaalisesti!]")
auto = Auto()
auto.kiihtyy()
print("nyt nopeus on: ", auto.nopeus, "kmh")
auto.kiihtyy()
print("nyt nopeus on: ", auto.nopeus, "kmh")
auto.kiihtyy()
print("nyt nopeus on: ", auto.nopeus, "kmh")

