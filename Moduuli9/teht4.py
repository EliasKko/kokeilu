class Auto:
    def __init__(self, rekisterinumero, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

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

auto1 = Auto("ABC-123", 120)
SalamaMcqueen = Auto("NOP-331", 200)
FinMcmissle = Auto("BIG-455", 160)

auto1.kiihtyy(15)
SalamaMcqueen.kiihtyy(12)
FinMcmissle.kiihtyy(11)

auto1.kulje(1)
SalamaMcqueen.kulje(1)
FinMcmissle.kulje(1)

print("Kisan tilanne tunnin jälkeen matkamäärässä: ", auto1.kuljettu_matka, SalamaMcqueen.kuljettu_matka, FinMcmissle.kuljettu_matka)

auto1.kiihtyy(-3)
SalamaMcqueen.kiihtyy(-7)
FinMcmissle.kiihtyy(1)

auto1.kulje(4)
SalamaMcqueen.kulje(4)
FinMcmissle.kulje(4)

print("Kisan tilanne 5 tunnin jälkeen matkamäärässä: ", auto1.kuljettu_matka, SalamaMcqueen.kuljettu_matka, FinMcmissle.kuljettu_matka)

auto1.kiihtyy(10)
SalamaMcqueen.kiihtyy(15)
FinMcmissle.kiihtyy(-10)

auto1.kulje(4)
SalamaMcqueen.kulje(4)
FinMcmissle.kulje(4)

print("Kisan tilanne 9 tunnin jälkeen matkamäärässä: ", auto1.kuljettu_matka, SalamaMcqueen.kuljettu_matka, FinMcmissle.kuljettu_matka)

auto1.kiihtyy(-15)
SalamaMcqueen.kiihtyy(-15)
FinMcmissle.kiihtyy(15)

auto1.kulje(5)
SalamaMcqueen.kulje(5)
FinMcmissle.kulje(5)

print("Kisan tilanne 14 tunnin jälkeen matkamäärässä: ", auto1.kuljettu_matka, SalamaMcqueen.kuljettu_matka, FinMcmissle.kuljettu_matka)

print("Autot:")
print("1. SalamaMcqueen", SalamaMcqueen.rekisterinumero, "Huippunopeus kmh", SalamaMcqueen.huippunopeus)
print("2. FinMcmissle", FinMcmissle.rekisterinumero, "Huippunopeus kmh", FinMcmissle.huippunopeus)
print("3. auto1", auto1.rekisterinumero, "Huippunopeus kmh", auto1.huippunopeus)
