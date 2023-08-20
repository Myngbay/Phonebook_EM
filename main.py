import io
from typing import NoReturn, Dict


def main() -> NoReturn:
    """Функция main() при запуске программы запрашивает у пользователя действие и зависимо от выбора вызывает
    следующую функцию """
    choice: int = int(input('1. Добавить\n'
                       '2. Редактировать\n'
                       '3. Поиск\n'
                       '4. Вывести в консоль\n'
                       'Введите цифру 1, 2, 3 или 4:'))

    if choice == 1:
        add()
    if choice == 2:
        edit()
    if choice == 3:
        search_data()
    if choice == 4:
        show_data()


def add() -> NoReturn:
    """Функция add() поочереди запрашивает данные как имя, фамилия и т.д. после этого все данные записываются в
    словарь и передаются в функцию write_data()"""
    name: str = input('Введите имя: ')
    second_name: str = input('Введите фамилию: ')
    surname: str = input('Введите отчество: ')
    organization_name: str = input('Введите название организации: ')
    work_phone: str = input('Введите рабочий номер: ')
    personal_phone: str = input('Введите личный номер: ')

    data_dict: Dict[str, str] = {'Имя': name,
                                 'Фамилия': second_name,
                                 'Отчество': surname,
                                 'Название организации': organization_name,
                                 'Рабочий номер': work_phone,
                                 'Личный номер': personal_phone}

    write_data(data_dict)


def edit() -> NoReturn:
    """Функция edit() читает файл с данными phonebook.txt, записывает их в словарь. Затем у пользователя
    запрашивается имя поля которое нужно изменить, после этого значение в словаре изменяются и словарь передается в
    функцию write_data()"""
    data_dict_2: Dict[str, str] = {}

    with io.open('phonebook.txt', encoding='utf-8') as book:
        for index in book.readlines():
            key, val = index.strip().split(':')
            data_dict_2[key] = val

    user_editing: str = input('Какое поле хотите изменить? ')
    changed_value: str = input('Введите новое значение: ')
    data_dict_2[user_editing] = changed_value

    write_data(data_dict_2)


def search_data() -> NoReturn:
    """Функция search_data() читает файл с данными phonebook.txt, записывает их в словарь. Затем у пользователя
    запрашивается имя поля которое нужно найти, после этого значение из словаря выводится в консоль"""
    data_dict_3: Dict[str, str] = {}
    with io.open('phonebook.txt', encoding='utf-8') as book:
        for index in book.readlines():
            key, val = index.strip().split(':')
            data_dict_3[key] = val

    user_request: str = input('Какое поле хотите найти? ')

    print(data_dict_3[user_request])


def show_data() -> NoReturn:
    """Функция show_data() читает файл с данными phonebook.txt, записывает их в словарь и выводит в консоль """
    data_dict_4: Dict[str, str] = {}
    with io.open('phonebook.txt', encoding='utf-8') as book:
        for index in book.readlines():
            key, val = index.strip().split(':')
            data_dict_4[key] = val
    for key, val in data_dict_4.items():
        print(f"{key} : {val}")


def write_data(file) -> NoReturn:
    """Функция write_data() записывает в файл phonebook.txt переданное значение file"""
    with open('phonebook.txt', 'w', encoding='utf-8') as book:
        for key, val in file.items():
            book.write('{}:{}\n'.format(key, val))
    print('Данные записаны.')


if __name__ == '__main__':
    main()