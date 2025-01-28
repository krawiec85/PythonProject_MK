# zbiór (set) - przechowuje unikalne wartości (brak duplikatów)
# nie zachowuje kolejności przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)
print(type(zbior))

zb2 = set()
print(zb2)
print(type(zb2))

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
print(zbior)

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)

# pop() - usunięcie pierwszego elementu
print(zbior.pop())
print(zbior)
print(zbior.pop())
zmienna = zbior.pop()
print('Usunęliśmy element:', zmienna)

zbior_copy = zbior.copy()
print(zbior_copy)
print(zbior)
print(id(zbior))
print(id(zbior_copy))

# operacje na zbiorach
zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))
print(zbior_2)

# suma zbiorów
print(zbior.union(zbior_2))

# część wspólna
print(zbior & zbior_2)

# różnice (kolejność ma znaczenie)
print(zbior - zbior_2)
print(zbior.difference(zbior_2))
print(zbior_2.difference(zbior))

# łączy zbiory, zmienna bazowy!!!
zbior.update(zbior_2)
print(zbior)

krotka = tuple(zbior)
print(krotka)

lista = list(zbior)
print(lista)

#czy element istnieje w kolekcji
print(777 in zbior)
