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
