
def lasku():
    arr = int(input("Anna gallonamäärä: "))
    if arr > 0:
        x = arr * 3.785
        print(int(x), "litraa")
        lasku()
    elif arr < 0:
        print("finito")
lasku()