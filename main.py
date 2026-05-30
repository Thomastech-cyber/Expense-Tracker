from random import choice


expense = []

def add_expense(expense, amount):
  expense.append(amount)


def calculate_total(expenses):
  return sum(expenses)


def main():
  while True:
    action = input("Enter 'add' to add an expense, 'total' to calculate total expenses, or 'exit' to quit: ")
    
    if action == 'add':
      amount = float(input("Enter the expense amount: "))
      add_expense(expense, amount)
      print(f"Added expense: {amount}")
    
    elif action == 'total':
      total = calculate_total(expense)
      print(f"Total expenses: {total}")
    
    elif action == 'exit':
      print("Exiting the program.")
      break
    
    else:
      print("Invalid action. Please try again.")

main()