import math
a = int(input("Anna 1. pizzan halkaisija (cm) "))
b = int(input("Anna 1. pizzan hinta "))
k = int(input("Anna 2. pizzan halkaisija (cm) "))
r = int(input("Anna 2. pizzan hinta "))
def pizzalaskuri():
    N = a * 0.01
    n = math.pi * N ** 2
    Yks = n * b
    M = k * 0.01
    m = math.pi * M ** 2
    Kaks = m * r
    print("Ensimmäisen pizzan hinta (euroa neliömetriä kohden): ", Yks, "Ja toisen: ", Kaks)
    if Yks > Kaks:
        print("Eli pizza 2. on halvempi.")
    elif Yks < Kaks:
        print("Eli pizza 1. on halvempi.")
pizzalaskuri()
