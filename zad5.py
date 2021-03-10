import sys as system
system.stdout.write("wpisz 3 dowolne liczby calkowite: ")
a = system.stdin.readline()
b = system.stdin.readline()
c = system.stdin.readline()
wynik = pow(int(a), int(b)) + int(c)
print(wynik)
