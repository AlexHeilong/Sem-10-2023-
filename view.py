import text_fields

def main_menu() -> int:
    print(text_fields.main_menu)
    length_menu = len(text_fields.main_menu.split('\n')) - 1 # пунктов 5, первая строка "Главное меню" - ее и вырезаем
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            return int(choice)
        else:
            print(f'Введите цифру от 1 до {length_menu}')

def show_contacts(book: list[dict], error_message: str):
    if not book:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f'{i}.{contact.get("name"): <20} ' # <20 - выравнивание по левому краю (20 символов)  
                  f'{contact.get("phone"): <20} '
                  f'{contact.get("comment"): <20}')
        return True


def add_contact() -> dict:
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}

def input_index(message: str):
    return int(input(message))

def change_contact(book: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    contact = add_contact()
    return {contact.get('name') if contact.get('name') else book[index-1].get('name'),
            contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}
     # index-1 потому что пользователь вводит цифру, а индексы начинаются с 0

def show_message(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))

def input_search(message: str):
    return message
