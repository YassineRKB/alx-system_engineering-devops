#!/usr/bin/python3
"""Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == '__main__':
    domain = 'https://jsonplaceholder.typicode.com'
    param = argv[1]
    todo = domain + f"/user/{param}/todos"
    user = domain + f"/users/{param}"
    todoJSON = requests.get(todo).json()
    userJSON = requests.get(user).json()
    done = 0
    for taskdone in todoJSON:
        if taskdone.get("completed"):
            done += 1
    username = f"{userJSON.get('name')}"
    progress = f"{done}/{len(todoJSON)}"
    print(f"Employee {username} "
          f"is done with tasks({progress}):")
    for taskdone in todoJSON:
        if taskdone.get("completed"):
            taskTitle = taskdone.get('title')
            print(f"\t {taskTitle}")
