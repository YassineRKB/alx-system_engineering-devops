#!/usr/bin/python3
"""Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
export into csv format"""

from csv import QUOTE_ALL, writer
import requests
from sys import argv

if __name__ == '__main__':
    domain = 'https://jsonplaceholder.typicode.com'
    param = argv[1]
    todo = domain + f"/user/{param}/todos"
    user = domain + f"/users/{param}"
    todoJSON = requests.get(todo).json()
    userJSON = requests.get(user).json()
    with open("{}.csv".format(param), mode="w") as stream:
        write = writer(stream, quoting=QUOTE_ALL)
        for taskdone in todoJSON:
            rows = [
                param,
                userJSON.get("username"),
                taskdone.get("completed"),
                taskdone.get("title")
                ]
            write.writerow(rows)
