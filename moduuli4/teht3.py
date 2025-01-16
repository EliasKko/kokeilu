a = int(input("anna luku: "))
list = []
if a!="":
    list.append(a)
while  a!="":
    a = int(input("anna luku: "))
    if a!="":
        list.append(a)
isoinluku = max(list)
pieninluku = min(list)
print("iosin luku: ", isoinluku, "pienin luku: ", pieninluku)

