# Expense Manager


## Project Description
The Expense Manager is a Python program that models and manages financial expenses. It consists of two classes: Expense and ExpenseDB.


### Expense Class
Represents an individual financial expense.


##### Attributes:
The Expense Class has the following attributes:

`id`: A unique identifier generated as a UUID string.
`title`: A string representing the title of the expense.
`amount`: A float representing the amount of the expense.
`created_at`: A timestamp indicating when the expense was created (UTC).
`updated_at`: A timestamp indicating the last time the expense was updated (UTC).


##### Methods:

__init__: Initializes the attributes.
`update`: Allows updating the title and/or amount, and updating the \updated_at\ timestamp.
`to_dict`: Returns a dictionary representation of the expense.


### ExpenseDB Class
Manages a collection of Expense objects.

##### Attributes:
`database`: A list storing Expense instances.


##### Methods:

__init__: Initializes the ExpenseDB attributes.
`add_expense`: Adds an expense.
`remove_expense`: Removes an expense.
`get_expense_by_id`: Retrieves an expense by ID.
`get_expense_by_title`: Retrieves expenses by title (returning a list).
`to_dict`: Returns a list of dictionaries representing expenses.


## How to clone the repository
1. Open your terminal.
2. Run: `git clone https://github.com/ififrank2013/expense-manager.git`



## How to Run the code:

Ensure you have Python installed.

```bash
cd expense-manager
python main.py