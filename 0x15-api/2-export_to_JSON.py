#!/usr/bin/python3
"""script to export data in the JSON format."""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(argv[1])).json()
    todos = get(url + "todos", params={"userId": argv[1]}).json()
    with open("{}.json".format(argv[1]), "w") as f:
        json.dump({argv[1]: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": argv[1]
            } for t in todos]}, f)
