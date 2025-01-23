a = input("anna luku: ")
list = []
if a!="":
    a = int(a)
    list.append(a)
while  a!="":
    a = input("anna luku: ")
    if a!="":
        a = int(a)
        list.append(a)

isoinluku = max(list)
pieninluku = min(list)
print("iosin luku: ", isoinluku, "pienin luku: ", pieninluku)

