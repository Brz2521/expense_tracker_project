from email.policy import default
import json
from datetime import date, datetime

# View all function
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

# Delete function










    



