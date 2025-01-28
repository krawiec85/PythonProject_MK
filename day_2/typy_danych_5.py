# słownik - para klucz wartość
# {"user: 'Radek' 'wiek':76"}
# odpowiednik json


# pusty słownik
dictionary = dict()
print(dictionary)
print(type(dictionary))

dictionary_1 = dict()
print(dictionary_1)
print(type(dictionary_1))

# dodanie elementu do słownika
dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = '48'
print(dictionary)

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', '48'])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', '48')])

# nadpisanie elementu
dictionary['imie'] = 'Tomek'
print(dictionary)

# print(dictionary['Imie']) #nie ma takiego klucza w słwoniku
print(dictionary.get('Imie', 'default')) #None, nia ma klucza

dictionary.update({'data': '12-12-2025'})
print(dictionary)

dict_small = {'x':2}
print(dict_small)

# input() - pozwala wprowadzić dane do komputera
tekst = input('Podaj imię')
print(tekst)

