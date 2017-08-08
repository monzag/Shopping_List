from shopping_list import ShoppingList
from item import Item
import view


def main_menu():
    shopping_list = ShoppingList.create_from_csv('alma')

    user_choice = ''
    while user_choice != 0:
        view.print_main_menu()
        view.get_input()

        if user_choice == 1:
            # show items
            pass

        elif user_choice == 2:
            shopping_list.get_total_price()

    view.print_exit_message()
