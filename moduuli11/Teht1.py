class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self,nimi,kirjoittaja,sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjan sivumäärä: {self.sivumäärä} kirjoittaja: {self.kirjoittaja}")


class Lehti(Julkaisu):
    def __init__(self,nimi,päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.päätoimittaja}")

ankka = Lehti("Aku Ankka", "Aki Hyyppä")
ankka.tulosta_tiedot()
hytti = Kirja("Hytti n:o 6","Rosa Liksom","200 sivua")
hytti.tulosta_tiedot()