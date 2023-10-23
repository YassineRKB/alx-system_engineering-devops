#!/usr/bin/python3
"""Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
export into JSON format"""

from json import dump
import requests
from sys import argv

if __name__ == '__main__':
    domain = 'https://jsonplaceholder.typicode.com'
    param = argv[1]
    todo = domain + f"/user/{param}/todos"
    user = domain + f"/users/{param}"
    todoJSON = requests.get(todo).json()
    userJSON = requests.get(user).json()
    JSONROWDATA = []
    JSONDATA = {}
    with open(f"{param}.json", mode="w") as stream:
        for taskdone in todoJSON:
            row = {
                "task": taskdone.get('title'),
                "completed": taskdone.get("completed"),
                "username": userJSON.get("username")
            }
            JSONROWDATA.append(row)
        JSONDATA[param] = JSONROWDATA
        dump(JSONDATA, stream)
