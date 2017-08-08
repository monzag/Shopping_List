class Item:

    def __init__(self, name, quantity, unit, price_per_unit, categories, is_bought=False):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.price_per_unit = price_per_unit
        self.categories = categories
        self.is_bought = is_bought

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_total_price(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        if self.is_bought is True:
            return '[x] {}, unit: {}, categories: {}'.format(self.name, self.unit, self.categories) + self.show_price()

        else:
            return '[ ] {}, unit: {}, categories: {}'.format(self.name, self.unit, self.categories) + self.show_price()

    def show_price(self):
        return '\n{} zł/{}'.format(self.price_per_unit, self.quantity)
