on = int(input("anna vuosiluku: "))
if on % 4 == 0:
    print("vuosi on karkausvuosi")
elif on % 100 == 0 and on % 400 == 0:
    prinht("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")