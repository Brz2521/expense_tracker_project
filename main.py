from argparse import ArgumentParser, Namespace
import pathlib

parser = ArgumentParser(
    description="Track and manage expenses"
)

sub = parser.add_subparsers(dest="command", required=True)

# Add command
add_parser = sub.add_parser("add", help="Add an expense")
add_parser.add_argument('--description', required=True, help="Expense description")
add_parser.add_argument('--amount', type=float, required=True, help="Expense amount")

# List command to view all expenses
sub.add_parser("list", help="View all expenses")

# Update command
update_parser = sub.add_parser("update", help="Update an expense")
update_parser.add_argument('--id', type=int, required=True, help="Expense ID")
update_parser.add_argument('--description', help="New expense description")
update_parser.add_argument('--amount', type=float, help="New expense amount")

# Delete command
delete_parser = sub.add_parser("delete", help="Deletes an expense")
delete_parser.add_argument('--id', type=int, required=True, help="Expense ID")

# Summary command to view an expense
summary_parser = sub.add_parser("summary", help="View expense summary")
summary_parser.add_argument("--month", type=int, help="Month number (1-12)")


#Read the command line arguments
args = parser.parse_args()

#print(args)

'''
# Choosing a command (Test area)
match args.command:
    case "add":
        print(f'Your desc is {args.description} and amount is {args.amount}')
    case "update":
        print("update expense")
    case "delete":
        print("Delete expense")
    case "list":
        print("view all, list command")
    case "summary":
        print("Summary of the expense")
'''