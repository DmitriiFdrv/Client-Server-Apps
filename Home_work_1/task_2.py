#  task_2


arr = ['class', 'function', 'method']

for i in arr:
    elem = eval(f"b'{i}'")
    print(f'-' * 20)
    print('type', type(elem))
    print(elem)
    print('len in bytes', len(elem))