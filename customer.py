from grocery_bag import GroceryBag
from toolbox import Toolbox
from retail_store import RetailStore
from groceries import GroceryIf
from tools import ToolIf

class Customer:
    """
    Represents a customer with a name, cash balance, shopping cart, toolbox, grocery bag,
    and associated retail store.
    The customer can fill the cart, add cash, make purchases, and view cart items.
    """
    def __init__(self, name, cash, store: RetailStore, groceries: list[GroceryIf], tools: list[ToolIf]):
        self.name = name
        self.cash = cash
        self.grocery_bag = GroceryBag(f"{name}'s Grocery Bag")
        self.toolbox = Toolbox(f"{name}'s Toolbox")
        self.store = store
        self.groceries = groceries  # List of groceries to purchase
        self.tools = tools          # List of tools to purchase
    
    def fill_cart(self):
        """
        Adds a tool or grocery item to the customer's shopping cart.
        """
        print(f"{self.name} is shopping for groceries.")
        for grocery in self.groceries:
            added = self.grocery_bag.add_grocery(grocery)
            if not added:
                print("Unable to add the grocery!")
        
        print(f"{self.name} is shopping for tools.")
        for tool in self.tools:
            added = self.toolbox.add_tool(tool)
            if not added:
                print("Unable to add the tool!")
    
    def checkout(self):
        """
        Attempts to purchase the items in the grocery bag and toolbox.
        If the customer has enough cash, the purchase is successful and the store's revenue is updated.
        """
        total_grocery_cost = self.grocery_bag.total_cost
        total_tool_cost = self.toolbox.total_cost * 1.14  # Adding GST for tools
        total_cost = total_grocery_cost + total_tool_cost
        
        if self.cash >= total_cost:
            self.cash -= total_cost
            self.store.add_revenue(total_grocery_cost, total_tool_cost)
            print(f"{self.name} successfully purchased items for a total of ${total_cost:.2f}.")
        else:
            print(f"{self.name} does not have enough cash to complete the purchase!")
        
        self.grocery_bag.display()
        self.toolbox.display()
    
    def add_cash(self, amount):
        """
        Adds the specified amount of cash to the customer's cash balance.
        """
        self.cash += amount
        print(f"{self.name} has added ${amount:.2f} to their balance. New balance: ${self.cash:.2f}.")
