import random
N = int(input("Anna arvausten määrä: "))
A = 0
B = 0

for i in range(N):
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    A = A + 1
    if x^2+y^2<10:
        B = B + 1
X = 4 * B / A
print("Piin likiarvo= ", X)
