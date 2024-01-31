from return_data_file import data_file


def copy_row():
    data, nf = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    nf = int(input("Введите номер файла в который хотите скопировать: "))
    print(nf)
    while nf < 1 or nf > 2:
        nf = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(data[number_row - 1])

    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    count_rows = len(data)
    data = [f'{i + 1};{data[i].split(";")[1]};'
                f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3]};'
                f'{data[i].split(";")[4]}'
                for i in range(len(data))]
    with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
    print("Данные скопированы")