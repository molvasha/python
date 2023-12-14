# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной


# 1. Создание файла. ++++
# ---------------------------
# 2. Добавление новой записи. ++++
# * забрать ввод пользователя
# * открытие файла на дозапись
# * записать в файл
# ------------------------------
# 3 Вывод на экран
# * открыть файл на чтение
# * считывание данных
# * вывод на экран
# ------------------------------
# 4 Поиск контакта
# * выбрать вариант поиска
# * забрать ввод пользователя
# * открытие файла на чтение
# * считать данные
# * осуществить поиск
# * вывести результат поиска
# ------------------------------
# 5 Создание интерфейса ++++


def name_input():
    return input('Введите имя: ')


def surname_input():
    return input('Введите фамилию: ')


def patronymic_input():
    return input('Введите отчество: ')


def phone_input():
    return input('Введите номер: ')


def address_input():
    return input('Введите адрес: ')


def create_contact():
    '''Add an entry'''
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()

    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'


def write_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        print('\nКонтакт записан!\n')


def print_contacts():
    '''List all entries'''
    # with open('phonebook.txt', 'r', encoding='utf-8') as file:
    #     print('-----------------------')
    #     print(file.read())
    #     print('-----------------------')
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_list, 1):
            print(f'{nn}. {contact}\n')


def search_contact(field=''):
    ''''''
    # search = input('Введите данные для поиска: ')

    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. по имени\n'
        '3. по отчеству\n'
        '4. по номеру\n'
        '5. по городу\n'
        )
    index_var = int(input('Ведите вариант поиска: '))-1
    search = input('Введите данные для поиска: ')
    
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.strip().split('\n\n')

        for contact_str in contacts_list:
            contacts_list = contact_str.replace('\n', ' ').split(' ')
            if search in contacts_list[index_var]:
                print(f'\n{contact_str}\n')

def copy_contact():
    print_contacts()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        contacts_list_new=[]
        for nn, contact in enumerate(contacts_list, 1):
            contact = f'{nn}.{contact}'
            contacts_list_new.append(contact)
        line_to_copy = int(input('Введите номер строки для копирования: '))
        with open('phonebook.txt', 'r', encoding='utf-8') as file:
            contact_str = contacts_list_new[0]
            for i in range(len(contacts_list_new)):
                if f'{line_to_copy}.' in contacts_list_new[i]:
                    with open('phonebook2.txt', 'a', encoding='utf-8') as file:
                        file.write(contacts_list_new[i])
                        print('Копирование завершено')
    

def interface():
    with open('phonebook.txt', 'a'):
        pass

    user_input = None
    while user_input != '5':
        print(
            'Возможные варианты действия:\n'
            '1. Добавить контакт\n'
            '2. Вывод списка контактов\n'
            '3. Поиск контакта\n'
            '4. Копирование контакта\n'
            '5. Выход из программы\n'
        )

        user_input = input('Введите вариант: ')

        while user_input not in ('1', '2', '3', '4'):
            print('Некорректный ввод.')
            user_input = input('Введите вариант: ')

        print()

        match user_input:
            case '1':
                write_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_contact()
if __name__ == '__main__':
    interface()