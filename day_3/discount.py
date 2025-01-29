from datetime import datetime, date, timedelta

today = date.today()
print('Dzisiejsza data:', today)
print(type(today))

time = datetime.now()
print('Aktualny czas:', time)

print(time.year)
print(time.month)
print(time.day)

tommorow = today + timedelta(days=1)
print('Jutro będzie', tommorow)

formated_data = datetime.now().strftime('%d/%m/%Y')
print(type(formated_data))
print('Data formatowana:', formated_data)

formated_data = datetime.now().strftime('%H:%M')
print(type(formated_data))
print('Godzina:', formated_data)