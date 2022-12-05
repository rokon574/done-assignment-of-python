mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': 300, 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': 200, 'made': 'USA'},
        {'name': 'Iphone 5', 'price': 180.5, 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': 89.60, 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': 110 , 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': 350, 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
for mobiles in mobile_data :
    status = mobile_data.get('status')
    name = mobile_data.get('data')[0].get('name')
    price = mobile_data.get('data')[0].get('price')
    made = mobile_data.get('data')[0].get('made')
exchange_rate = mobile_data.get('exchnage_rate')
sentence = f'{name} is made in {made}.The price is {price} USD which is almost equal to {int(exchange_rate * price)} BDT'

print(sentence)
