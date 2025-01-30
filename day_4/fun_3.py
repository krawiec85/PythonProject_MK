a = 10
b = 10


def dodaj():
    a = 7  # lokalne zmienne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # użyje globalnych


def dodaj3():
    global a
    a = 9  # nadpisze globalne a
    b = 89
    print(a + b)


print(f'Wartość a z góry {a=} (globalna)')
dodaj()
print(f'Wartość a z góry {a=} (globalna)')
dodaj2()
print(f'Wartość a z góry {a=} (globalna)')
dodaj3() # 98, zmieniło wartość a globalnego
print(f'Wartość a z góry {a=} (globalna)')
dodaj2()
print(f'Wartość a z góry {a=} (globalna)')
