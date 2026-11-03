from email.policy import default
import json
from datetime import date, datetime

# Load all data function
def load_data():
    with open("expenses.json", "r") as file:
        data = json.load(file)

    return data

# Add function
def add_cmd(args):
    data = load_data()
    next_id = max((e["id"] for e in data["expenses"]), default=0) + 1
    new_expense = {
        "id": next_id,
        "date": date.today().isoformat(),
        "desc": args.description,
        "amount": args.amount
        
    }

    data["expenses"].append(new_expense)

    with open("expenses.json", "w") as file:
        json.dump(data, file, indent=4)

# Update function
def update_cmd(args):
    data = load_data()

    for expense in data["expenses"]:
        if expense["id"] == args.id:

            if args.description is not None:
                expense["desc"] = args.description

            if args.amount is not None:
                expense["amount"] = args.amount

            expense["date"] = date.today().isoformat()
            
            with open("expenses.json", "w") as file:
                json.dump(data, file, indent=4)

            print(f"Expense {args.id}, updated successfully")
            return

    print(f"Expense with ID {args.id} was not found")

# Delete command
def delete_cmd(args):
    data = load_data()

    for expense in data["expenses"]:

        if expense["id"] == args.id:
            data["expenses"].remove(expense)

            with open("expenses.json", "w") as file:
                json.dump(data, file, indent=4)

            print(f'Expense {args.id} deleted successfully')
            return

    print(f"Expense with ID {args.id} was not found")


# List command
def list_cmd(args):
    data = load_data()

    if not data["expenses"]:
        print("No expenses found")
        return

    print("ID | Date | Description | Amount")
    print("-" * 50)

    for expense in data["expenses"]:
        print(
            f'{expense["id"]} | '
            f'{expense["date"]} | '
            f'{expense["desc"]} | '
            f'${expense["amount"]:.2f}'
        )

# Summary command
def summary_cmd(args):
    data = load_data()

    if args.month is not None:
        if not 1 <= args.month <= 12:
            print("Month must be between 1 and 12")
            return

        total = sum(
            expense["amount"]
            for expense in data["expenses"]
            if datetime.fromisoformat(expense["date"]).year == date.today().year
            and datetime.fromisoformat(expense["date"]).month == args.month
        )

        print(f"Total expenses for month {args.month}: ${total:.2f}")

    else:
        total = sum(
            expense["amount"]
            for expense in data["expenses"]
        )

        print(f"Total expenses: ${total:.2f}")



















    



