class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    def __eq__(self, other):
        if isinstance(other, str):
            return  self.name == other
        return self.name == other.name and self.quantity == other.quantity
 

class ShoppingList:
    def __init__(self):
        self.shop_cart = []
        
    def add_items(self, name, quantity):
        new_item = Item( name, quantity)
        self.shop_cart.append(new_item)
    
    def remove_items(self, name, quantity):
        remd_item = Item( name, quantity)
        self.shop_cart.remove(name)

        
    def print_shop_cart(self):
        print("=~" * 15)
        print("SHOPPING LIST:")
        
        for item in self.shop_cart:
            print(item.name, item.quantity)
        
        print("=~" * 15)
        
    def run(self):
        while True:
            try:
                question = input("What would you like to do (Add/Remove/Show/Check Out)? ")

                if question == "Add":
                    name = input("Add item to list: ")
                    if not name.isalpha():
                        raise ValueError("Input invalid, please add name of item")
                    quantity = int(input("Add amount: "))
               
                    self.add_items(name, quantity)

                elif question == "Remove":
                    name = input("Remove item from list: ")
                    if not name.isalpha():
                        raise ValueError("Input invalid, please add name of item")             
                    quantity = int(input("how many? "))

                    self.remove_items(name, quantity)

                elif question == "Show":
                    self.print_shop_cart()
                                    
                elif question == "Check Out":
                    break

                    
            except Exception as error:
                print("There was an error, please try again.")
                print(error)
 
        self.print_shop_cart()

shop_cart = ShoppingList()
shop_cart.run()
