def print_main_menu():
    options = ['Show items', 'Show total price']
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
