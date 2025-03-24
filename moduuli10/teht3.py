class Talo:
    def __init__(self,x,y,hissienmäärä):
        self.alinkerros = x
        self.ylinkerros = y
        self.hissit = []
        for i in range(hissienmäärä):
            self.hissit.append(Hissi(len(self.hissit)+1))

    def aja_hissiä(self, hissinumero, siirtymäkerros):
        self.hissit[hissinumero-1].siirry_kerrokseen(siirtymäkerros)

    def palo_hälytys(self):
        for hissienmäärä in range(len(self.hissit)):
            self.aja_hissiä(hissienmäärä,self.alinkerros)

class Hissi:
    def __init__(self,x):
        self.hissi_numero = x
        self.ylinkerros = 8
        self.alinkerros = 0
        self.kerros = 0

    def kerros_ylös(self):
        self.kerros += 1
        print("hissi", self.hissi_numero, "on kerroksessa: ", self.kerros)

    def kerros_alas(self):
        self.kerros -= 1
        print("hissi", self.hissi_numero, "on kerroksessa: ", self.kerros)

    def siirry_kerrokseen(self,siirtymäkerros):
        while self.kerros < siirtymäkerros and siirtymäkerros <= self.ylinkerros:
            self.kerros_ylös()
        while self.kerros > siirtymäkerros and siirtymäkerros >= self.alinkerros:
            self.kerros_alas()
        if siirtymäkerros > self.ylinkerros:
            print("ei pääse")
        elif siirtymäkerros < self.alinkerros:
            print("ei pääse")

huussi = Talo(0,8,3)
huussi.aja_hissiä(1,8)
huussi.aja_hissiä(2,6)
huussi.aja_hissiä(3,5)
huussi.palo_hälytys()