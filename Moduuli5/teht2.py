luvut = []
luku = input("anna luku: ")
if luku != "":
    luku = int(luku)
    luvut.append(luku)
def jouu():
    luku = input("anna luku: ")
    if luku != "":
        luku = int(luku)
        luvut.append(luku)
    while  luku != "":
        luku = input("anna luku: ")
        if luku != "":
            luku = int(luku)
            luvut.append(luku)
jouu()
luvut.sort()
print(luvut)
