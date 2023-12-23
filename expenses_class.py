"""
Installing necessary libraries
"""
from uuid import uuid4
from datetime import datetime, timezone



"""
This class object represents an individuals' financial expense
"""
class Expense:
    """
    Defining the class attributes/states
    """
    def __init__(self, title, amount):
        self.id = str(uuid4())  # A unique identifier for each expense.
        self.title = title  # A string representing the title of the expense.
        self.amount = float(amount) # A float representing the amount of the expense.
        self.created_at = datetime.now(timezone.utc)  # A timestamp indicating when the expense was created.
        self.updated_at = self.created_at  # A timestamp indicating the time when an expense was last updated.

    """
    This method enables the updagting of the title and/or amount of each expense
    """
    def update(self, expense_title=None, expense_amount=None):
        if expense_title:
            self.title = expense_title
            print(f"The title has been updated to {expense_title}")
        if expense_amount:
            self.amount = expense_amount
            print(f"The amount has been updated to {expense_amount}")
        self.updated_at = datetime.now(timezone.utc)

    """
    This method converts each expense to a dictionary
    """
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def __repr__(self) -> str:
        return f"{self.title}_{self.amount}"




"""
This class object manages a collection of Expense objects. It enables the manipulation of Expense objects.
"""
class ExpenseDB:
    def __init__(self):
        self.database = []


    """ 
    This method inserts a new expense to the database
    """
    def add_expense(self, expense):
        self.database.append(expense)
        print(f"{expense} Expenses have been successfully added to the database with ID: {expense.id}")


    """ 
    This method removes an expense from database based on expense id
    """
    def remove_expense(self, expense_id):
        self.database = [expense for expense in self.database if expense.id != expense_id]
        print(f"The expense with id:  {expense_id} has been deleted from the database")


    """
    This method retrieves an expense from the database based on expense id
    """
    def get_expense_by_id(self, expense_id):
        for expense in self.database:
            if expense.id == expense_id:
                return expense
        return None

    """
    This method retrieves a list of expenses from the database based on expense title
    """
    def get_expenses_by_title(self, expense_title):
        return [expense for expense in self.database if expense.title == expense_title]

    """
    This method retrieves a list of dictionaries representing expenses.
    """
    def to_dict(self):
        return [expense.to_dict() for expense in self.database]





# Instantiating the classes
if __name__ == "__main__":
    pass

