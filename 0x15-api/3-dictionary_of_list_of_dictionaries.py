#!/usr/bin/python3
"""Python script that, using this REST API,
for all employee ID, returns information
about his/her TODO list progress.
export into JSON format"""

from json import dump
import requests

if __name__ == '__main__':
    domain = 'https://jsonplaceholder.typicode.com'
    param = 1
    totalParamUsers = len(requests.get(domain + "/users/").json()) + 1
    with open("todo_all_employees.json", mode="w") as stream:
        JSONDATA = {}
        while (param != totalParamUsers):
            userJSON = requests.get(domain + f"/users/{param}").json()
            todoJSON = requests.get(domain + f"/user/{param}/todos").json()
            JSONROWDATA = []
            for taskdone in todoJSON:
                row = {
                    "username": userJSON.get("username"),
                    "task": taskdone.get("title"),
                    "completed": taskdone.get("completed")
                }
                JSONROWDATA.append(row)
            JSONDATA[param] = JSONROWDATA
            param += 1
        dump(JSONDATA, stream)
