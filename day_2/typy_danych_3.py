# krotka - tuple - kolekcja niemutowalna, tylko do odczytu
# pozwala efektywniej zarządzać pamięcią
# krotka jednoelementowa - zastępstwo stałych, zmienna niezmienna

tupla_imiona = 'Radek', 'Tomek', 'Mateusz', 'Ania', 'Marek'
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
