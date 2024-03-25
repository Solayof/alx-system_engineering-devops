#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users").json()
    with open("todo_all_employees.json", "w") as f:
        json.dump({u.get("id"): [{
            "username": u.get("username"),
            "task": t.get("title"),
            "TASK_COMPLETED_STATUS": t.get("completed")
        } for t in get(url + "todos",
                       params={"userId": u.get("id")}).json()]
                        for u in users}, f)
