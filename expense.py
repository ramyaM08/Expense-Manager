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