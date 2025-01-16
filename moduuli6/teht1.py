import random
def heitto(x):
    for i in range(x):
        a = random.randint(1, 6)
        if a != 6:
            print(a)
        if a == 6:
            print(a)
            break
heitto(100)