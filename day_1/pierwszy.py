import sys

print()  # wypisz/wydrukuj
# Process finished with exit code 0 - program zakończył działanie bez błędu
# Process finished with exit code 1 - program zakończył działanie z błędem

print("Nazywam się Radek")
# ctrl d - powielanie linii

print('Nazywam się Radek')

# type() - sprawdzenie typu danych
print(type("Mateusz"))  # <calss 'str'>, string, dane typu kontekstowego
print('39' + '39')  # 3939
print(39 + 39)  # 78 operacja na liczbach
print(type(39))  # <class 'int'>, liczba całkowita, integer
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)
# print('39' + 39) #TypeError: can only concatenate str (not "int") to str
# nie zaminie typów na inne w trakcie wykonywania operacji

# musimy jawnie wskazać odpowienie typy
print(int('39'))  # rzutowanie, zamiana na liczbę
print(int('39') + 39)  # 78
print('39' + str(39))  # 3939
print(5 * '4')  # 44444
print(5 * 4)  # 20

# zmienna - pudełko na dane, przechowuje jeden element
# snake_case
# nazwa zmiennej powinna sugerować co przechowuje

liczba = 39
print(liczba)  # wypisanie wartości zmiennej
print(type(liczba))  # <class 'int'>

liczba = 'Radek'
print(liczba)
print(type(liczba))

name = 'Mateusz'
print(name + ' Kowalski')
name = 90
# print(name + 'Kowalski') - nie zadziała, TypeError: unsupported operand type(s) for +: 'int' and 'str'
# podpowiedz dla programist
name: str = 'Mateusz'
print(name)
name = 90
print(name)  # 90

age = 56
print(age)
print(type(age)  # 56
