from item import Item
from datetime import datetime


class ShoppingList:

    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.items = []

    def get_items(self, is_bought=False):
        for item in self.items:
            if item.is_bought == is_bought:
                print(item)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items)

    @classmethod
    def create_from_csv(cls, file_name):
        splitted_data = cls.get_data_from_file(file_name)

        for row in splitted_data:
            if len(row) < 4:
                shopping_list = cls.create_shopping_list(file_name, row)

            else:
                item = cls.create_item(row)
                shopping_list.items.append(item)

        return shopping_list

    @classmethod
    def create_shopping_list(cls, file_name, row):
        name = file_name
        day, month, year = row[0], row[1], row[2]
        date = datetime(year, month, day)
        shopping_list = ShoppingList(name, date)

        return shopping_list

    @classmethod
    def create_item(cls, row):
        name, quantity, unit, price_per_unit, categories_list = row[0], row[1], row[2], row[3], row[4]

        categories = categories_list.split('|')

        last_item = -1
        if row[last_item] == 'done':
            is_bought = True

        else:
            is_bought = False

        item = Item(name, quantity, unit, price_per_unit, categoties, is_bought)

        return item



