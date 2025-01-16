import random
a = random.randint(1,10)
V = int(input("arvaa luku 1-10: "))
if V > a:
    print("liian suuri arvaus")
if V < a:
    print("liian pieni arvaus")
while a != V:
    V = int(input("arvaa luku 1-10: "))
    if V > a:
        print("Liian suuri arvaus")
    if V < a:
        print("Liian pieni arvaus")
if a == V:
    print("Oikein")