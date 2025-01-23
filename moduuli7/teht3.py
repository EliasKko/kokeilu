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
        lista.add(a)
        kyssäri()
kyssäri()
print(lista)