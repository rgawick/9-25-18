class ShoppingList():
    def __init__(self, store, description):
        self.store = store
        self.description = description
        self.shopping_list = []

    def add_item(self, item):
        self.item = item
        self.shopping_list.append(item)

    def view_list(self):
        print(self.shopping_list)

class GroceryItem():
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "%s" % (self.title)

while True:
    print("1 - Create new list")
    print("2 - View list")
    print("3 - Add to list")
    prompt = input("Please enter an option from the menu above or enter 'q' to quit:").lower()

    if (prompt == "1"):
        store = input("Which grocery store will you be shopping at? (HEB / Kroger / Randalls / Sam's Club / Fiesta): ")
        list_description = input("Please enter a description for the shopping list: ")
        shopping_list = ShoppingList(store, list_description)

    elif (prompt == "2"):
        shopping_list.view_list()

    elif (prompt == "3"):
        name = input("Please enter the name of item you are purchasing: ")
        grocery_item = GroceryItem(name)
        shopping_list.add_item(grocery_item)

    elif (prompt == 'q'):
        break

    else:
        print("Please enter a valid option.")
