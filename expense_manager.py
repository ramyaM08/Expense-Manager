from expense import Expense

class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def list_expenses(self):
        if len(self.expenses)==0:
            print("No expenses found")
            return
        for expense in self.expenses:
            expense.display()

    def search_expense(self, field, value):
        found = False

        for expense in self.expenses:
            field_value = getattr(expense, field)
            if str(field_value).lower() == str(value).lower():
                expense.display()
                found = True

        if not found:
            print("No Expense Found")

    def delete_expense(self, field, value):
        found = False

        for expense in self.expenses:
            field_value = getattr(expense, field)
            if str(field_value).lower() == str(value).lower():
                self.expenses.remove(expense)
                found = True
                print(field_value, "Expense deleted")

        if not found:
            print(value, "expense not found to delete")

    def save_expenses(self):
        with open("expenses.txt", "w") as file:
            for expense in self.expenses:
                file.write(f"{expense.amount},{expense.category},{expense.description}\n")

    def load_expenses(self):

        try:
            with open("expenses.txt", "r") as file:
                lines = file.readlines()

            for line in lines:
                parts = line.strip().split(",")

                expense = Expense(
                    int(parts[0]),
                    parts[1],
                    parts[2]
                )

                self.add_expense(expense)

        except FileNotFoundError:
            print("No saved expenses found")
