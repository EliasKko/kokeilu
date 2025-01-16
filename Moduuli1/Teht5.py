import math
a = int(input("Anna leiviskät."))
b = int(input("Anna naulat."))
c = int(input("Anna luodit."))
L = c * 0.0133
N = b * 0.4256
I = a * 8.512
Kilo = L + N + I
whole_number, decimal_part = divmod(Kilo, 1)
whole_number = int(Kilo)
print("kilogrammoja = ", whole_number,"grammoja = ", decimal_part )
