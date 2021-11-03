from PyInquirer import prompt
import csv

def get_users(answers):
    with open('users.csv', 'r') as f:
        next(f)
        infos = []
        for line in f:
            infos.append(line.rstrip())

    return infos

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices":get_users,
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    print(infos)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow([infos["amount"]] + [infos["label"]] + [infos["spender"]])
    print("Expense Added !")
    return True
