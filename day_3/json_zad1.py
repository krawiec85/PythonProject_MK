# używany jest do komunikacji w internecie

import json

person_dict = {'name': 'Radek,', 'age':40, 'czy_pali':None}

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)

with open('nasze_dane_b.json', "w") as f:
    json.dump(person_dict, f, indent=4)

with open('nasze_dane.json', "r") as fh:
    data = json.load(fh)

print(data)
print(type(data))
print(data['name']) # Radek

json_text = json.dumps(data)
print(json_text)
print(type(json_text))

dict_json = json.loads(json_text)
print(dict_json)
print(type(dict_json))