lista = set()
def kysy():
    a = input("Anna nimi: ")
    if a != "":
        if a in lista:
            print("Aiemmin syötetty nimi")
            kysy()
        if a not in lista:
            print("Uusi nimi")
            lista.add(a)
            kysy()
kysy()
print("Tässä listan nimet: ")
for a in lista:
    print(a)