# task_3

import yaml

my_dict = {
        'prods': ['pc', 'laptop', 'smartphone', 'headphones'],
        'quantity': 9,
        'price': {
            'pc': '2000€',
            'laptop': '94321€',
            'smartphone': '30000€',
            'headphones': '2300€'}
        }

with open('file.yaml', 'w', encoding='utf-8') as f_i:
    yaml.dump(my_dict, f_i, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open('file.yaml', 'r', encoding='utf-8') as f_o:
    my_dict_out = yaml.load(f_o, Loader=yaml.SafeLoader)

print(my_dict == my_dict_out)





"""
def write_dict_to_yaml(dict, file):
    with open('file.yaml', 'w', encoding='utf-8') as f_n:
        yaml.dump(dict, f_n, default_flow_style=False, allow_unicode = True)

    with open('file.yaml') as f_n:
        f_n_content = yaml.load(f_n)

    print(f_n_content == dict)


if __name__ == "__main__":
    my_dict = {
        '11111€': [1, 2, 3, 4],
        '2222€': 999,
        '333€': {
            'QWERTY': [1, 2, 3, 4],
            'qwerty': 4321,
        }
    }

    write_dict_to_yaml(my_dict, 'file.yaml')"""