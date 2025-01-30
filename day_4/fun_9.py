# funkcja lambda
# skrócony zapis funkcji

def odejmij(a, b):
    return a - b


print(odejmij(10, 5))  # 5

odejmij2 = lambda a, b: a - b
print(odejmij2(65, 32))

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(500))

wiek = lambda x: 'Dziecko' if x < 10 else ('Nastolatek' if x < 18 else 'Dorosły')
print(wiek(9))
print(wiek(17))
print(wiek(25))
print(wiek(35))

lista = [1, 2, 3, 4, 24, 50, 100, 500]
l = []
for i in lista:
    l.append(i * 2)
print(l)


def zmien(x):
    return x * 2


# mapowanie
l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)

# filtrowanie danych
l3 = []
for i in lista:
    if i <3:
        l3.append(i)
print(l3)

#filter() - zwraca elementy spełniające dany warunek
print(f'Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}')
print(f'Zastosowanie filter(): {list(filter(lambda x: x < 50, lista))}')
print(f'Zastosowanie filter(): {list(filter(lambda x: 3 < x < 150, lista))}')