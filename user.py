from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"user",
        "message":"New User: ",
    },
]

def add_user():
    infos = prompt(user_questions)
    print(infos)

    # This function should create a new user, asking for its name
    with open('users.csv', 'a') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow([infos["user"]])

    return