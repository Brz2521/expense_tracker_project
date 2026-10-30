from main import main
import json

def load_data():
    with open("expenses.json", "r") as file:
        data = json.load(file)

    return data

def add_cmd(args):
    data = load_data()
    new_expense = {
        "desc": args.description,
        "amount": args.amount
    }

    data["expenses"].append(new_expense)

    with open("expense.json", "w") as file:
        json.dump(data, file, indent=4)



    



