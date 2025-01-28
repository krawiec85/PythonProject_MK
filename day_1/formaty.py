user = 'Tomek' #str
wiek = 39 # int
wersja = 3.90001
print(type(wersja)) #float

liczba = 4637485949 #int

print('Witaj %s, masz teraz %d lat.' % (user, wiek))
#print('Witaj %s, masz teraz %d lat.' % (user, wiek))

print('witaj %(user)s, jesteś %(user)s' % {'user': user}) #witaj Tomek, jesteś Tomek
print('witaj %(user)a, jesteś %(user)a' % {'user': user}) #witaj 'Tomek', jesteś 'Tomek'

print(f'Witaj {user}, masz teraz {wiek} lat.')

print('Używamy wersji pythona %i' % 3)
print('Używamy wersji pythona %f' % 3)
print('Używamy wersji pythona %f' % 3.9)
print('Używamy wersji pythona %.2f' % 3.9)
print('Używamy wersji pythona %.0f' % 3.9)
x = 3.8796
print(x)
print('%.2f' % x) #3.88

y = round(x)
print(y) # 4

z = round(x, 2)
print(z) #3.88

print(f'Używamy wersji pythona {wersja}')
print(f'Używamy wersji pythona {wersja:.1f}')

print(f'{user:<10}')
print(f'{user:>20}')

print(liczba)
print(f"Nasza duża liczba {liczba: ,}") #Nasza duża liczba  4,637,485,949
print(f"Nasza duża liczba {liczba: ,}".replace(',', '.')) #Nasza duża liczba  4.637.485.949

liczba = 150000000000000
print(f"Nasza duża liczba {liczba: ,}")

liczba = 15_000_000_000_0000
print(liczba)