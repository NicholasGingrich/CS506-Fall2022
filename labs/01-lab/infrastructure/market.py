class Market: 
    def __init__(self, name):
        self.name = name
        self.items_in_stock = {}
    
    def set_name(self, name):
        self.name = name

    def add_item_for_sale(self, item_name, quantity, price):
        self.items_in_stock["name"] = (quantity, price)

    

