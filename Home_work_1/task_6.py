#  task_6


file = open("test_file.txt", "w")
file.write("сетевое программирование\n")
file.write("сокет\n")
file.write("декоратор\n")


print(file.encoding)
file.close()

with open("test_file.txt", encoding='utf-8') as file:
    for line in file:
        print(line, end='')