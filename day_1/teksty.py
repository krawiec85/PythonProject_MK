tekst = 'Witaj Świecie'
print(tekst)
print(type(tekst))  # <class 'str'>

#teksty są niemutowalne
tekst.upper()
print(tekst) # Witaj Świecie
""" Return a copy of the string converted to uppercase. """
print(tekst.upper()) #WITAJ ŚWIECIE
tekst_upper = tekst.upper()

print(tekst.capitalize()) # Witaj świecie
print(tekst.lower()) # witaj świecie
print(tekst.swapcase()) #wITAJ śWIECIE

print(tekst)
#0123456.... - indeksy numerowane od 0

print(tekst[6]) #"Ś"

print(tekst.index('Ś'))
print(tekst.index('i'))
print(tekst.count('i'))
print(tekst.count('j',0,4)) #0 razy bo z prawej strony zbiór otwarty

print(tekst.removeprefix('Witaj')) # Świecie

# usuniećie białych znaków, spacji itp.
print(tekst.removesuffix('Świecie').strip()) # 'Witaj'

tekst_zamiana = "Witaj Dobry Świecie"
print(tekst_zamiana.replace("Dobry ", "")) #Witaj Świecie

encode_s = tekst.encode('utf-8')
print(encode_s) #b'Witaj \xc5\x9awiecie' - zapis szesnastkowy dla literki Ś
print(encode_s.decode('utf-8'))


imie='Radek'
#f string
tekst_format= f'Mam na imię {imie} i lubie Pythona.'
print(tekst_format)

tekst_format= f'\tMam na imię {imie}\n i lubie Pythona.\b'
print(tekst_format)
#Mam na imię Radek
# i lubie Pythona
# \t - tab
# \n - nowa linia
# \b - backspace

starszy = 'Witaj %s!' # %s w to miejsce postawi string
print(starszy % imie) #Witaj Radek!

print('Witaj {}!'.format(imie)) #Witaj Radek!

print('Witaj', imie) # Witaj Radek

print('''Teskt
    wielonijkowy''')
