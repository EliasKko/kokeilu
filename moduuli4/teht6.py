import random
N = int(input("Anna arvausten määrä: "))
A = 0
B = 0

for i in range(N):
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    list1.append(x)
    list1.append(y)
    A = A + 1
    if x^2+y^2<10:
        B = B + 1
        list2.append(x)
        list2.append(y)
X = 4 * B / A
print(A, B)
print("Piin likiarvo= ", X)
