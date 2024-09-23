from abc import ABC, abstractmethod

# Grocery Interface
class GroceryIf(ABC):
    """
    Abstract interface for grocery items.
    Requires implementing classes to provide `get_cost` and `display` methods.
    """
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def display(self):
        pass

# Apple Class
class Apple(GroceryIf):
    """
    Represents an apple as a grocery item, with a name, cost, and calorie count.
    """
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
    
    def get_cost(self):
        """
        Returns the cost of the apple.
        """
        return self.cost
    
    def display(self):
        """
        Displays information about the apple, including its name, calorie count, and cost.
        """
        print(f"{self.name} is an apple. It has {self.calories} calories and costs ${self.cost:.2f}.")

# Orange Class
class Orange(GroceryIf):
    """
    Represents an orange as a grocery item, with a name, cost, and calorie count.
    """
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
    
    def get_cost(self):
        """
        Returns the cost of the orange.
        """
        return self.cost
    
    def display(self):
        """
        Displays information about the orange, including its name, calorie count, and cost.
        """
        print(f"{self.name} is an orange. It has {self.calories} calories and costs ${self.cost:.2f}.")
