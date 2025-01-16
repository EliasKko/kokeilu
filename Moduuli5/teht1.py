import random
lista = []
def heitto(kerrat):
    for i in range(kerrat):
        a = random.randint(1, 6)
        lista.append(a)
    return
def summa():
    a = sum(lista)
    print("Summa on: ", a)
    return

noppa = input("kerro noppien lukumäärä:")
heitto(int(noppa))
summa()


