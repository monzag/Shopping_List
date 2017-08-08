def print_main_menu():
    options = ['Get shopping list from file', 'Add new shopping list']
    get_list(options)
    print_exit_option()


def get_list(options):
    print('')
    number = 1
    for option in options:
        print('{}. {}'.format(number, option))
        number += 1
    print('')


def print_exit_option():
    print('0. Exit\n')


def get_input():
    number = input('\nWrite number: ')
    if number.isdigit():
        return int(number)

    return None


def print_exit_message():
    print('\nGood bye:) ')


def print_error_file():
    print('\nFile not exist')


def get_shop_name():
    return input('\nType name of shopping list: ')


def print_shopping_menu():
    options = ['Show items', 'Show total price', 'Add new item']
    get_list(options)
    print_exit_option()


def get_date():
    day = input('Day: ')
    month = input('Month:')
    year = input('Year: ')

    if day.isdigit() and month.isdigit() and year.isdigit():
        if 0 < int(day) < 32 and 0 < int(month) < 13 and len(year) == 4:
            return int(day), int(month), int(year)


def print_options_of_get_items():
    options = ['to buy', 'already bought']
    print('Show items by: ')
    get_list(options)
