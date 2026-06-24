class Expense:
    def __init__(self, amount, category, description):
        if amount<=0:
            raise ValueError("Invalid amount")
        if category.strip() == "":
            raise ValueError("Category cannot be empty")
        self.amount = amount
        self.category = category
        self.description = description

    def display(self):
        print(f"Amount : {self.amount}")
        print(f"Category : {self.category}")
        print(f"Description : {self.description}")    
        print("--------------")


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

    def search_by_amount(self, amount):
        found = False

        for expense in self.expenses:
            if expense.amount == amount:
                expense.display()
                found = True
                print(found)
        
        if not found:
            print("No Expense Found")
        
    def search_by_category(self, category):
        found = False

        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                expense.display()
                found = True
                print(found)
        
        if not found:
            print("No Expense Found")

    def search_by_description(self, description):
        found = False

        for expense in self.expenses:
            if expense.description.lower() == description.lower():
                expense.display()
                found = True
                print(found)
        
        if not found:
            print("No Expense Found")

    def delete_expense_by_amount(self, amount):
        found = False

        for expense in self.expenses:
            if expense.amount == amount:
                self.expenses.remove(expense)
                found = True
                print(expense.amount, "Expense deleted")

        if not found:
            print(amount, "expense not found to delete")

    def delete_expense_by_category(self, category):
        found = False

        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                self.expenses.remove(expense)
                found = True
                print(expense.category.upper(), "Expense deleted")

        if not found:
            print(category.upper(), "expense not found to delete")

    def delete_expense_by_description(self, description):
        found = False

        for expense in self.expenses:
            if expense.description.lower() == description.lower():
                self.expenses.remove(expense)
                found = True
                print(expense.description.upper(), "Expense deleted")

        if not found:
            print(description.upper(), "expense not found to delete")

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

# expense1 = Expense(1000, "food", "coffee")

# expense2 = Expense(500, "stationery", "books")

# expense3 = Expense(5000, "Hospital", "Checkup")

# expenses = ExpenseManager()


# expenses.add_expense(expense1) 

# expenses.add_expense(expense2) 

# expenses.add_expense(expense3) 
# expenses.save_expenses()

# try:
#     expense4 = Expense(
#         -500,
#         "Food",
#         "Burger"
#     )

#     expenses.add_expense(expense4)

# except ValueError as e:
#     print("Error:", e)

#expenses.search_by_amount(2000)
#expenses.search_by_category("Shopping")
#expenses.search_by_description("Books")
#expenses.delete_expense_by_category("Hospital")
#expenses.delete_expense_by_category("laptop")
#expenses.delete_expense_by_description("coffee")
#expenses.list_expenses()

# Main Function 
expenses = ExpenseManager()

expenses.load_expenses()

expenses.list_expenses()
