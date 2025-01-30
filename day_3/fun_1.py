# funkcja - wykonuje fragment kodu w dowolnym momencie
# funkcja musi być zadeklarowana przed wywołaniem

a = 8
b = 6


# deklaracja funkcji
def dodaj():  # funkcja bez argumentów
    print(a + b)

dodaj()  # wywołanie funkcji

def dodaj2(a, b):  # funkcja z argumentami (obowiązkowe do przekazania)
    print(a + b)

dodaj2(67, 89) # wywołanie funkcji
# TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
input_a = input('Podaj pierwszy argument: ')
input_b = input('Podaj drugi argument: ')
dodaj2(int(input_a), int(input_b))  # przekazanie wartości zmiennych

def odejmij(a, b, c=0):  # funkcja z opcjonalnym argumentem (domyślnie 0)
    print(a - b - c)

odejmij(c=9, b=8, a=10)
odejmij(1, 2, c=9) # -10
# argumenty pozycyjne muszą być podane przed argumentami kolejnościami !!!!

print (dodaj())
# 14
# None