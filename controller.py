from shopping_list import ShoppingList
from item import Item
from datetime import datetime
import view
import os


def main_menu():
    user_choice = ''
    while user_choice != 0:
        view.print_main_menu()
        user_choice = view.get_input()

        if user_choice == 1:
            shopping_list = open_shopping_list_from_file()
            if shopping_list:
                shopping_menu(shopping_list)

        elif user_choice == 2:
            create_shopping_list()

        view.print_exit_message()


def open_shopping_list_from_file():
    name = view.get_shop_name()
    file_path = name + '.csv'
    if os.path.exists(file_path):
        shopping_list = ShoppingList.create_from_csv(name)
        return shopping_list
    else:
        view.print_error_file()


def create_shopping_list():
    name = view.get_shop_name()
    day, month, year = view.get_date()
    if day and month and year:
        date = datetime(year, month, day)
        shopping_list = ShoppingList(name, date)
        shopping_menu(shopping_list)


def shopping_menu(shopping_list):
    user_choice = ''
    while user_choice != 0:
        view.print_shopping_menu()
        user_choice = view.get_input()

        if user_choice == 1:
            get_items_by_attr(shopping_list)

        elif user_choice == 2:
            print(shopping_list.get_total_price())

        elif user_choice == 3:
            add_new_item(shopping_list)


def get_items_by_attr(shopping_list):
    view.print_options_of_get_items()
    number = view.get_input()
    if number == 1:
        shopping_list.get_items()
    elif number == 2:
        shopping_list.get_items(True)


def add_new_item(shopping_list):
    print('This is test')
    name, quantity, unit, price_per_unit, categories = 'masło', 'szt', 1, 6, ['Food', 'Nabiał']
    item = Item(name, quantity, unit, price_per_unit, categories)
    shopping_list.add_item(item)
    shopping_list.save_data_to_file()


