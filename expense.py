from PyInquirer import prompt
import csv
import json

def get_users(n):
    with open('users.csv', 'r') as f:
        next(f)
        infos = []
        for line in f:
            infos.append(line.rstrip())

    return infos

def get_users_json(n):
    with open('users.csv', 'r') as f:
        next(f)
        infos = []
        chk = n["spender"]

        for line in f:
            tmp = line.rstrip()

            if tmp == chk :
                infos.append({'name':tmp,'disabled':'the buyer'})
            else :
                infos.append({'name':tmp})
     
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
    {
        "type":"checkbox",
        "name":"involved",
        "message": "New Expense - Select involved: ",
        "choices":get_users_json,
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
    with open('debt_report.csv', 'a') as f:
        # create the csv writer
        writer = csv.writer(f)

        new_price = int(infos["amount"]) / len(infos["involved"])
        # write a row to the csv file
        writer.writerow([infos["involved"]] + [new_price] + [infos["spender"]])
    print("Expense Added !")
    return True
