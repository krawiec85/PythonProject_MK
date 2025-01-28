# kolekcje

lista = []
print(lista)
print(type(lista))

pusta_lista = list()
print(pusta_lista)
print(type(pusta_lista))

# append () - dodawanie elementów do listy
lista.append('Radek')
lista.append('Maciek')
lista.append('Zenek')
lista.append('Anna')
lista.append('Mateo')
lista.append('Radek')
print(lista)  # ['Radek', 'Maciek', 'Zenek', 'Anna', 'Mateo', 'Radek']
# 0 1 2 3 4 5
print(len(lista))
print(lista[3])

print(lista[-1])  # ostatni element z listy

# slicowanie
print(lista[0:3])  # indeksy 0,1,2
print(lista[2:])  # ['Zenek', 'Anna', 'Mateo', 'Radek']
print(lista[2:5])
print(lista[2:15])
print(lista[:])
print(lista[2:2])
print(lista[2:3])
print(lista[-2:0])
print(lista[0:-2])
lista_15 = list(range(15))
print(lista[::2])
print(lista[::-1])
# nadpisanie elementu w liście na wskazanym indeksie
lista[3] = 'Asia'
print(lista)
# dopisanie elementu do listy we wzkazanym miejscu
lista.insert(1,'Mateusz')
print(lista)
lista.insert(15, "Mateusz")
print(lista)
#sprawdzenie indeksu dla wskazanego elementu
print(lista.index('Asia'))
lista.append('Asia')
print(lista)
print(lista.index('Asia'))
lista.remove('Asia')
print(lista)
lista.pop(5)
print(lista)
print(lista.pop(-3))
a = 1
b = 3
a = b
print(f'{a=}, {b=}')
b = 9
print(f'{a=}, {b=}')

lista_2 = lista # odpowiednik a = b
print(lista_2)
print(lista)
lista.clear()
print(lista_2)
print(lista)
liczby = [54, 999, 34, 22, 12.34, 567]
print(liczby)
liczby.sort()
print(liczby)
liczby[3]=666
print(liczby)

tekst = 'Pyth on.'
lista1 = list(tekst)
print(lista1)

lista2=[tekst]
print(lista2)

krotka = tuple(liczby)
print(type(krotka))
print(krotka)