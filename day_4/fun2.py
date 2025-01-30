# funkcje zwracajace wynik
# kończy się słówkiem return

def dodaj(a, b):
    return a + b

def odejmij(a, b=0, c=0):
    return a - b -c
def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100

print(dodaj(5, 9)) # 14
wynik = dodaj(89, 56)
print('Wynik', wynik)

print(odejmij(1))

print(oblicz_vat(1000))
print(oblicz_vat(vat=9, kwota=4500))

zm = oblicz_vat(1000)
print(type(zm))

if zm == 1230:
    print('Ok')