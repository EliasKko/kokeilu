import random
a = int(input("anna maksimisilmäluku: "))
luvut = []
def heitto(x):
    for i in range(x):
        h = random.randint(1, a)
        luvut.append(h)
        if h != a:
            print(h)
        if h == a:
            print(h)
            print("Tässä on silmälukujen summa: ", sum(luvut))
            break
heitto(1000)