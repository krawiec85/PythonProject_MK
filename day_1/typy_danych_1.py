import sys
wiek = 47 #int
rok = 2025 # int
temp = 36.6 #float

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)

print(rok // wiek) #część całkowita z dzielenia 43
print(rok % wiek) # reszta z dzielenia
print(5 % 2) # r1

print(wiek ** rok)

#len() sprawdzenie długości
print(len(str(wiek ** rok))) #ilość znaków
#print(len(str(wiek ** rok ** 2))) #ValueError: Exceeds the limit (4300 digits) for
# integer string conversion; use sys.set_int_max_str_digits() to increase the limit


print(54 - 5 * 43 + 4 / 2 +4 / 2)
print(54 - 5 * 43 + (4/2 +4)/2)

print(0.2 + 0.8)
print(0.2 + 0.7)
print(0.1 + 0.2)
print(sys.float_info)
#sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# typ logiczny
# True False
czy_znasz_pythona = True
print(czy_znasz_pythona)
print(type(czy_znasz_pythona))

print(int(czy_znasz_pythona))
print(int(False))

print(bool(1))

print(bool(100))
print(bool(-100))
print(bool('Radek'))
print(bool(0.01))
print(bool(None))

# and - i
print(True and True)
print(True and False)
# or - lub
print(True or True)
print(True or False)
# not - negacja
print(not True)

a = 8
b = 6

print(f'Porównanie {a} > {b} = {a > b}')
print(f'Porównanie {a} < {b} = {a < b}')
print(f'Porównanie {a} != {b} = {a != b}')