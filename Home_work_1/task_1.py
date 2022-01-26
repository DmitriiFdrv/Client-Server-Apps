#   task_1


def type_code(items: list) -> None:

    for item in items:
        print(item)
        print(type(item))
    print('-' * 80)


string1 = 'разработка'
string2 = 'сокет'
string3 = 'декоратор'
arr_1 = [string1, string2, string3]

type_code(arr_1)

string1_utf8 = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
string2_utf8 = b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
string3_utf8 = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
arr_2 = [string1_utf8, string2_utf8, string3_utf8]

type_code(arr_2)
