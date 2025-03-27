class Auto:
    def __init__(self,rekkari,huippunopeus,nopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = 0

    def kulje(self):
        a = 3
        self.matka += self.nopeus * a
        print(self.rekkari)
        print("mittari näyttää: ",self.matka, "km")


class Sähkö_auto(Auto):
    def __init__(self,rekkari,huippunopeus,nopeus,akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekkari,huippunopeus,nopeus)

class Polttomoottori_auto(Auto):
    def __init__(self,rekkari,huippunopeus,nopeus,bensa_tankin_koko):
        self.bensa_tankin_koko = bensa_tankin_koko
        super().__init__(rekkari,huippunopeus,nopeus)



yks = Sähkö_auto("ABC-15",180,40,"52.5 kWh")
kaks = Polttomoottori_auto("ACD-123",165,50,"32.3 l")
yks.kulje()
kaks.kulje()