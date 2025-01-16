Moi = input("mies vai nainen?: ")
Joo = int(input("hemoglobiini (g/l): "))
if Moi == "mies" and Joo >= 134 and Joo < 195:
    print("hemoglobiiniarvot ovat hyvät.")
elif Moi == "mies" and Joo < 134:
    print("hemoglobiiniarvot ovat liian alhaiset.")
elif Moi == "mies" and Joo > 195:
    print("hemoglobiiniarvot ovat liian korkeat.")
elif Moi == "nainen" and Joo < 117:
    print("hemoglobiiniarvot ovat liian alhaiset.")
elif Moi == "nainen" and Joo >= 117 and Joo < 175:
    print("hemoglobiiniarvot ovat hyvät.")
elif Moi == "nainen" and Joo > 175:
    print("hemoglobiiniarvot ovat liian korkeat.")
else:
    print("väärin kirjoitettu tieto")