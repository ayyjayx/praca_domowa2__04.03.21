import math
a = input("Wpisz dowolna liczbe do zpierwiastkowania: ")
a = float(a)
if a<0:
    print("Liczba jest ujemna")
else:
    print(math.sqrt(a))