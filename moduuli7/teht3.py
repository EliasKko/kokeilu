lista = {}
lista["EFHK"] = "Helsinki-Vantaa"
lista["EFOU"] = "Oulu"
def kyssäri():
    a = input("haluatko hakea(paina 1), vai lisätä(2) vai lopettaa(3): ")
    if a == "3":
        print("loppu")
    elif a == "2":
        b = input("Anna lentokentän nimi: ")
        c = input("Anna lentokentän  ICAO-koodi: ")
        lista[c] = b
        kyssäri()
    elif a == "1":
        s = input("Anna lentokentän ICAO-koodi: ")
        if s in lista:
            print("Lentokenttä on: ", lista[s])
            kyssäri()
        if s not in lista:
            print("Ei löydy")
            kyssäri()
kyssäri()
