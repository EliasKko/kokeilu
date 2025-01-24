class Auto:
    def __init__(self, rekisterinumero, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka
a = input("anna autolle rekkari: ")
b = input("anna autolle huippunopeus: ")
auto = Auto(a, b)
print("Auton rekkari on: ", auto.rekisterinumero)
print("Huippunopeus: ", auto.huippunopeus)
print("Tämänhetkinen nopeus: ", auto.tämänhetkinen_nopeus)
print("Ja kuljettu matka: ", auto.kuljettu_matka)
