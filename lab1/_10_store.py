goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price

table_quantity = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']
table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] \
             + store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']

couch_quantity = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']
couch_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] \
             + store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']

chair_quantity = store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] \
                 + store[goods['Стул']][2]['quantity']
chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] \
             + store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price'] \
             + store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']


def answer():
    print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
    print(f'Стол - {table_quantity}, стоимость {table_cost} руб')
    print(f'Диван - {couch_quantity}, стоимость {couch_cost} руб')
    print(f'Стул - {chair_quantity}, стоимость {chair_cost} руб')


if __name__ == "__main__":
    answer()
