dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}
print(type(dictionary))

for i in dictionary:
    print(i)
# imie
# nazwisko
for i in dictionary.keys():
    print(i)
# imie
# nazwisko
for i in dictionary.values():
    print(i)
# Radek
# Kowalski
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')
for k, v in dictionary.items():
    print(k, '=>', v)
# imie => Radek
# nazwisko => Kowalski

pol_ang = {'kot':'cat', 'pies':'dog', 'dach':'roof'}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol) # {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'} - zamienione miejscami

# zrób pętlę po słowniku
for k, v in ang_pol.items():
    print(k, '=>', v)
    print(v)