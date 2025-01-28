# krotka - tuple - kolekcja niemutowalna, tylko do odczytu
# pozwala efektywniej zarządzać pamięcią
# krotka jednoelementowa - zastępstwo stałych, zmienna niezmienna

tupla_imiona = 'Radek', 'Tomek', 'Mateusz', 'Ania', 'Marek', 'Lukas'
print(tupla_imiona)
print(type(tupla_imiona))

tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)
print(type(tupla_liczby))

tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)
print(type(tupla_liczby))

# tupla jednoelementowa
tupla = 43,
print(tupla)
print(type(tupla))

# tuple jednoelementową tworzymy z nawiasami

tupla = (43,)
print(tupla)
print(type(tupla))

# tupla jest niemutowalna

del tupla_liczby

print(tupla_imiona.index('Radek'))  # index 0
print(tupla_imiona.count('Radek'))  # wystepuje raz

tup = 1, 2
print(type(tup))

a, b = 1, 2
print(a, b)

a, b = tup
print(a, b)  # rozpakowanie tupli

tup_2 = 1, 2, 3
# a, b = tup_2 #ValueError: too many values to unpack (expected 2)
a, *b = tup_2
print(a, b)  # 1 [2, 3]

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Radek', 'Tomek', 'Mateusz', 'Ania'] Marek Lukas

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Tomek', 'Mateusz', 'Ania', 'Marek'] Lukas

print(sorted(tupla_imiona))  # ['Ania', 'Lukas', 'Marek', 'Mateusz', 'Radek', 'Tomek']
