# task_2

import json


def write_order_to_json(item: str, quantity: str, price: str, buyer: str, date: str) -> None:

    with open('orders.json', 'r', encoding='utf-8') as f_w:
        data = json.load(f_w)

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        order_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        }
        order_list.append(order_info)
        json.dump(data, f_n, indent=4, ensure_ascii=False)

"""        
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
"""


if __name__ == "__main__":
    write_order_to_json('Ноутбук', '2', '45500', 'Fury', '01.01.2022')
    write_order_to_json('ПК', '5', '66500', 'Rasputin', '01.01.2022')
    write_order_to_json('Сервер', '2', '512000', 'Loki', '01.01.2022')
    write_order_to_json('АКБ', '1', '900', 'Werty', '01.01.2022')