from tools import ToolIf

class Toolbox:
    """
    Represents a toolbox that can hold up to 4 tool items.
    Calculates the total cost of tools in the toolbox.
    """
    def __init__(self, name):
        self.name = name
        self.total_cost = 0.0
        self.items = []
        self.num_items = 0
    
    def add_tool(self, tool: ToolIf):
        """
        Adds a tool to the toolbox if it contains less than 4 items.
        Updates the total cost of the toolbox.
        Returns True if the tool was added, False otherwise.
        """
        if self.num_items < 4:
            self.items.append(tool)
            self.num_items += 1
            self.total_cost += tool.get_cost()
            return True
        return False
    
    def display(self):
        """
        Displays the tools in the toolbox and the total cost of all tools.
        """
        print(f"\n{self.name} is a toolbox with the following items:")
        for item in self.items:
            item.display()
        print(f"The total cost of these items is ${self.total_cost:.2f}\n")
