lista = []
lang = input('Podaj jaki znasz język programowania')

match lang.strip().casefold():
    case 'python':
        lista.append('Znam Pythona')
    case 'java':
        lista.append('Znam Jave')
    case _:
        print('Nie znam takiego')

print(lista)
