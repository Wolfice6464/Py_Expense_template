from PyInquirer import prompt
import csv

def status():
    with open('debt_report.csv', 'r') as f:
        next(f)
        infos = []
        for line in f:
            tmp = line.rstrip()

            infos.append(line.rstrip())
            print(tmp)

    return infos
