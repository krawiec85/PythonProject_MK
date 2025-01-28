# operacje na liczbach losowych
import random

print(random.randint(1, 100))  # int od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5)) # od 0 do 4
print(random.random()) # float od 0 do 0.99999

lista = [67, 45, 32, 68, 69, 90, 42]
print(random.choice(lista)) # wylosuje element

lista_kule = list(range(1,50))

wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))
print(random.sample(lista_kule, 6))
