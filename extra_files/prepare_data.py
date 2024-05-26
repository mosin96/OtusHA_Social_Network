import csv
import random
import string


def generate_password(length=12):
    """
    Функция для генерации случайного пароля.

    :param length: Длина генерируемого пароля (по умолчанию 12 символов).
    :return: Сгенерированный пароль.
    """
    # Создаем список символов, которые могут использоваться для создания пароля.
    characters = string.ascii_letters + string.digits

    # Генерируем случайный пароль из символов указанной длины.
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# people.v2.csv - скачать из https://raw.githubusercontent.com/OtusTeam/highload/master/homework/people.v2.csv
with open('people.v2.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

    with open('people.v3.csv', mode='w', encoding='utf-8', newline='') as csv_new_file:
        writer = csv.writer(csv_new_file)

        for i, row in enumerate(reader):
            print(f"Строка - n {i}")
            new_row = []
            new_row.extend(row[0].split(' '))  # Разделяем первую колонку на два элемента
            new_row.extend(row[1:])  # Добавляем остальные данные из строки
            new_row.append(generate_password())
            writer.writerow(new_row)

print("Копирование завершено.")

