# stworzyć funkcję kantor
# ma mieć dwie wewnętrzne funkcje, jedna ma być usd a druga eur
# w zależności od parametru zwracamy funkcję usd lub eur

def kantor(waluta):
    def usd(kwota):
        return kwota * 1.18

    def eur(kwota):
        return kwota * 0.9

    if waluta == 'USD':
        return usd
    elif waluta == 'EUR':
        return eur
    else:
        return None

xWymiana = kantor('USD')
print(xWymiana(1000))

