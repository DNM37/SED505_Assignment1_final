from abc import ABC, abstractmethod

# Tool Interface
class ToolIf(ABC):
    """
    Abstract interface for tool items.
    Requires implementing classes to provide `get_cost` and `display` methods.
    """
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def display(self):
        pass

# Hammer Class
class Hammer(ToolIf):
    """
    Represents a hammer as a tool item, with a name and cost.
    """
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    
    def get_cost(self):
        """
        Returns the cost of the hammer.
        """
        return self.cost
    
    def display(self):
        """
        Displays information about the hammer, including its name and cost.
        """
        print(f"{self.name} is a hammer and costs ${self.cost:.2f}.")

# Screwdriver Class
class Screwdriver(ToolIf):
    """
    Represents a screwdriver as a tool item, with a name and cost.
    """
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    
    def get_cost(self):
        """
        Returns the cost of the screwdriver.
        """
        return self.cost
    
    def display(self):
        """
        Displays information about the screwdriver, including its name and cost.
        """
        print(f"{self.name} is a screwdriver and costs ${self.cost:.2f}.")
