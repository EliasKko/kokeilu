haii = int(input("Anna luku:"))
x = haii - 1
while x > 1:
    if haii % x == 0:
        print("ei ole alkuluku")
        break
    elif haii % x != 0 and x > 0:
        x = x - 1
        print("calculating...")
if x <=1:
    print("alkuluku")

