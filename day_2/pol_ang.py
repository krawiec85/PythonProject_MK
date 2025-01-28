pol_ang = {'kot':'cat', 'pies':'dog'}
print('Znam takie słówka', pol_ang.keys())
odp = input('Podaj słówko do przetłumaczenia')

#print(pol_ang[odp.lower().strip()])

print(pol_ang[odp.casefold().strip()])