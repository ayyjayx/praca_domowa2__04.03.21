lista = []
i = 0
while i < 10:
    a = input("Prosze wpisac dowolna liczbe calkowita: ")
    a = int(a)
    if a % 2 == 0:
        lista.append(a)
    i += 1
print(lista)
