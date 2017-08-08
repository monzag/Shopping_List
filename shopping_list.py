from item import Item


class ShoppingList:

    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.items = []

    def get_items(is_bought=False):
        for item in self.items:
            if item.is_bought == is_bought:
                print(item)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items)
