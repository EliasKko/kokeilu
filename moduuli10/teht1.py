class Hissi:
    def __init__(self):
        self.ylinkerros = 8
        self.alinkerros = 0
        self.kerros = 0

    def kerros_ylös(self):
        self.kerros += 1
        print("kerros on nyt: ", self.kerros)

    def kerros_alas(self):
        self.kerros -= 1
        print("kerros on nyt: ", self.kerros)

    def siirry_kerrokseen(self,siirtymäkerros):
        while self.kerros < siirtymäkerros and siirtymäkerros <= self.ylinkerros:
            self.kerros_ylös()
        while self.kerros > siirtymäkerros and siirtymäkerros >= self.alinkerros:
            self.kerros_alas()
        if siirtymäkerros > self.ylinkerros:
            print("ei pääse")
        elif siirtymäkerros < self.alinkerros:
            print("ei pääse")

kerros = int(input("anna kerros: "))
h = Hissi()
h.siirry_kerrokseen(kerros)
kerros1 = int(input("anna kerros: "))
h.siirry_kerrokseen(kerros1)