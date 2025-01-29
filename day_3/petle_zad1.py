# możliwość wykonania kodu wielokrotnie
# for - pętla iteracyjna

for i in range(5):  # 01234
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(20):  # niema zmienna
    print("test podłoga")
    # print(_) # 19

for i in range(5):
    print(i * 2)
    print(i + 2)

import random

lista_kule = list(range(1, 50))
lista_wyn = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    lista_wyn.append(wyn)
print('Wynik losowania:', lista_wyn)

for i in range(10):
    if i % 2 == 0:
        print(i, 'parzysta')

lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)
print(lista3)

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]

for c in lista3:  # pobieraj z listy aż do ostatniego elementu
    if c > 4:
        print('Większe od 4')
    else:
        print('Mniejsze, równe 4')

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(-10, 0):  # bez 0
    print(i)

for i in range(10, 0, -2):  # od 10 do 1 bez zera co drugi, w dół
    print(i)

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print(c)  # tylko gdy warunek spełniony
#     print(c)  # przy każdym przejściu pętli
# print(c)  # po wykonaniu pętli

imiona = ["Radek", 'Tomek', 'Zenek', 'Ania']
print(imiona)
print(type(imiona))

for p in imiona:  # wyciągnie wszystkie imiona
    print(imiona.index(p), p)  # przypisanie indeksów do imion

for i in range(len(imiona)):  # range(4) -> 0123
    print(i, imiona[i])
# 0 Radek

# enamurete() - numeruje kolekcje i zwraca element i numer
for p in enumerate(imiona):
    print(p)

for i, p in enumerate(imiona, start=1):  # rozpakowanie tupli z przypisaniem indeksów
    print(i, p)

imiona = ["Radek", 'Tomek', 'Zenek', 'Ania']
wiek = [44, 55, 42, 27]
# Radek 44
for i in range(len(imiona)):
    print(f'{imiona[i]} {wiek[i]}')
    # print(p, wiek[imiona.index(p)])
    # IndexError: list index out of range - za dużo elementów jeśli dodamy jeszcze jedno imię

# zip() - łączy kolekcję
for i, w in zip(imiona, wiek):
    print(i, w)

# 0 Radek 44

imiona = ["Radek", 'Tomek', 'Zenek', 'Ania']
wiek = [44, 55, 42, 27]
for i in enumerate(zip(imiona, wiek)):
    print(i)
a, b = (0, ('Radek', 44))
print(a, b)
c, d = ('Radek', 44)
print(a, c, d)
(a, (c, d)) = (0, ('Radek', 44))
print(a, c, d)
for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 55
