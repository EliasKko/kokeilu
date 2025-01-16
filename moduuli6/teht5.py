lista = []
def summma():
    a = input("Anna summia, kun olet valmis paina enter: ")
    if a != "":
        a = int(a)
        if a % 2 == 0:
            lista.append(a)
            summma()
        elif a % 2 != 0:
            summma()
    if a == "":
        print("Parilliset: ", lista)
summma()