#  task_4


arr = ['разработка', 'администрирование', 'protocol', 'standard']

for i in arr:
    print(f'Переменная => {i}\n'
          f'В байтовом виде => {i.encode("utf8")}\n'
          f'decode  => {i.encode("utf8").decode()}\n',
          '-' * 40)