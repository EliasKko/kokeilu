lista = []
def summma():
    a = input("Anna summia, kun olet valmis paina enter: ")
    if a != "":
        a = int(a)
        lista.append(a)
        summma()
    if a == "":
        print("Lukujen summa: ", sum(lista))
summma()