# stworzyć funkcję obliczającą średnią
def liczby(*cyfry):
    print(cyfry)
    count = len(cyfry)
    suma = 0
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
    except Exception as e:
        print('Błąd:', e)
    else:
        print(f'Średnia {avg}')
    finally:
        print('Obliczenia zakończone')

liczby()
liczby(1,2,3,4,5,6)