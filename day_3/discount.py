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

products = [
    {'sku': 1, 'exp_date': today, 'price': 100},
    {'sku': 2, 'exp_date': today, 'price': 50},
    {'sku': 3, 'exp_date': tommorow, 'price': 200},
    {'sku': 4, 'exp_date': today, 'price': 100.99},
    {'sku': 5, 'exp_date': tommorow, 'price': 500},
    {'sku': 6, 'exp_date': today, 'price': 250},
]

for product in products:
    # print(product)
    # print(type(product))
    print(product['exp_date'])
    if product['exp_date'] != today:
        continue # zakończy działanie pętli i przechodzi do kolejnego elementu
    product['price'] *= 0.8  # obniżenie ceny o 20%
    print(f'''Price for sku {product['sku']}
is now: {product['price']}''')
