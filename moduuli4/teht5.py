ktunnus = ("python")
ssana = ("rules")
kerrat = 0
a = input("Anna käyttäjätunnus: ")
b = input("Salasana: ")
if a != ktunnus and b != ssana:
    kerrat = kerrat + 1
    print("väärin")
while a != ktunnus and b != ssana and kerrat<5:
    a = input("Anna käyttäjätunnus: ")
    b = input("Salasana: ")
    if a != ktunnus and b != ssana:
        kerrat = kerrat + 1
        print("väärin")
if a == ktunnus and b == ssana:
    print("Tervetuloa")
if kerrat == 5:
    print("Pääsy evätty")