# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykonana jeden lub drugi blok programu
# warunek musi zwracać typ bool

# odp = True
odp = False
if odp:
    # blok programu, który wykonuje się gdy warunek True
    print('Brawo')
    print('Brawo')
    print('Brawo')
    print('Brawo')

print('Kolejna część programu')

odp = 'Radek'
print(bool(odp))
if odp:
    print('Dane zostały zmienione')

if odp == 'Radek':
    print('Nadal Radek')

odp = 0
if odp:
    print('Działa')
else:
    print('Zero -> False')

# Te same sposoby

a = 'Radek'
if len(a) > 3:
    print(f'Długość wynosi {len(a)}, więcej niż 3')

a = 'Radek'
n = len(a)
if n > 3:
    print(f'Długość wynosi {n}, więcej niż 3')

# oprator morsa :=, walrus operator
if (n := len(a)) > 3:
    print(f"Długość wynosi {n}, więcej niż 3")

podatek = 0
zarobki = int(input('Podaj zarobki'))
if zarobki < 10_000:
    podatek = 0
elif zarobki >= 10_000 and zarobki < 30_000:
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.4
else:
    podatek = 0.9

print(f'Podatek wynosi {podatek * zarobki}')

# podatek 0.2 dla przedziału 10_000 do 39_999

# podatek = 0
# zarobki = int(input('Podaj zarobki'))
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki > 10_000:
#     podatek = 0.2
# elif zarobki <= 39_999:
#     podatek = 0.2
# elif zarobki > 39_999:
#     podatek = 0.4
# else:
#     podatek = 0.9

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f'Rabat wynosi {rabat}')

rabat = 25 if suma_zam > 100 else 0  # to jest to samo co powyżej
print(f'Rabat wynosi {rabat}')

# zasymulujemy system zbierania logów
# zmienna będzie zawierać informację jaki system przysłał log
# gdy log z systemu "console" wyświetlimy napis "Stało się coś strasznego"

alert_system = input('System: ')
lista_b = []  # pusta lista błędów
if alert_system == 'console':
    print('Stało sie coś')
elif alert_system == 'email':
    print("system email")
    error = input('Podaj typ błędu')
    if error == 'error':
        lista_b.append('Krytyczny')
    elif error == 'medium':
        lista_b.append('Ostrzezenie')
    print(lista_b)
else:
    print('Inny')
