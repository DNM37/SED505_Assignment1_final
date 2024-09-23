class RetailStore:
    """
    Represents a retail store that tracks customers, revenue from tools and groceries,
    and calculates statistics about total sales.
    """
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.total_grocery_revenue = 0.0
        self.total_tool_revenue = 0.0
    
    def add_customer(self, customer):
        """
        Adds a customer to the store's customer list.
        """
        self.customers.append(customer)
    
    def add_revenue(self, grocery_cost, tool_cost):
        # This method adds the revenue from groceries and tools to their respective totals.
        # The two arguments are the cost spent on groceries and tools by a single customer.
        self.total_grocery_revenue += grocery_cost
        self.total_tool_revenue += tool_cost
    
    def display_statistics(self):
        """
        Calculates and displays store statistics such as total revenue, tool revenue percentage,
        grocery revenue percentage, and average spending per customer.
        """
        # Displays store statistics, such as total revenue, average spending per customer,
        # and the percentage of revenue from groceries and tools.
        total_revenue = self.total_grocery_revenue + self.total_tool_revenue
        avg_spend = total_revenue / len(self.customers) if self.customers else 0
        
        print(f"\nRetail Store: {self.name} Statistics")
        print(f"Total Revenue: ${total_revenue:.2f}")
        print(f"Average Spend per Customer: ${avg_spend:.2f}")
        
        if total_revenue > 0:
            grocery_percentage = (self.total_grocery_revenue / total_revenue) * 100
            tool_percentage = (self.total_tool_revenue / total_revenue) * 100
            print(f"Percentage spent on Groceries: {grocery_percentage:.2f}%")
            print(f"Percentage spent on Tools: {tool_percentage:.2f}%")
