#  task_3


elem_1 = 'attribute'
elem_2 = 'класс'
elem_3 = 'функция'
elem_4 = 'type'
arr = [elem_1, elem_2, elem_3, elem_4]

for i in arr:
    try:
        i.encode(encoding='ascii')
    except UnicodeEncodeError:
        print(f'ОШИБКА записи: {i}')
        print(i.encode('utf8'))