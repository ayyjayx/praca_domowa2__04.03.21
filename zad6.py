a, b, c = input("Wpisz 3 dowolne liczby calkowite: ").split()
print(a, b, c)
if a == b == c:
    print('Liczby sa sobie rowne')
elif a > b:
    if c > a:
        print(c, 'jest najwieksze')
    else:
        print(a, 'jest najwieksze')
elif c > b:
    print(c, 'jest najwieksze')
else:
    print(b, 'jest najwieksze')
