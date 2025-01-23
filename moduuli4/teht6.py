import random
N = int(input("Anna arvausten määrä: "))
A = 0
B = 0

while N > 0:
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    A = A + 1
    N = N - 1
    if x^2+y^2<10:
        B = B + 1
    if N == 0:
        break
X = 4 * B / A
print("Piin likiarvo= ", X)
