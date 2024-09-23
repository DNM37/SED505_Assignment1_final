from groceries import GroceryIf

class GroceryBag:
    """
    Represents a grocery bag that can hold up to 4 grocery items.
    Calculates the total cost of groceries in the bag.
    """
    def __init__(self, name):
        self.name = name
        self.total_cost = 0.0
        self.items = []
        self.num_items = 0
    
    def add_grocery(self, grocery: GroceryIf):
        """
        Adds a grocery item to the bag if it contains less than 4 items.
        Updates the total cost of the grocery bag.
        Returns True if the grocery was added, False otherwise.
        """
        if self.num_items < 4:
            self.items.append(grocery)
            self.num_items += 1
            self.total_cost += grocery.get_cost()
            return True
        return False
    
    def display(self):
        """
        Displays the groceries in the bag and the total cost of all groceries.
        """
        print(f"\n{self.name} is a grocery bag with the following items:")
        for item in self.items:
            item.display()
        print(f"The total cost of these items is ${self.total_cost:.2f}\n")
