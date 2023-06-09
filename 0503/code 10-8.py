class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items = []
    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")
    def get_number_of_items(self):
        return len(self.__items)

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())

my_inventory.__items
print("52383013 CHOI RAK HUN")