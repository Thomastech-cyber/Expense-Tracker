expense = []

def add_expense(expense, amount):
  expense.append(amount)


def calculate_total(expenses):
  return sum(expenses)

def main():
  amount = float(input("Enter the amount of the expense: "))
  add_expense(expense, amount)
  total = calculate_total(expense)
  print("Total expenses:", total)