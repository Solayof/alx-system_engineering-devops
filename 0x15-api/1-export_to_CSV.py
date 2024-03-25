#!/usr/bin/python3
# A script that return info a given employee id
import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(argv[1])).json()
    todos = get(url + "todos", params={"userId": argv[1]}).json()
    with open("{}.csv".format(argv[1]), "w", newline="") as f:
        pen = csv.writer(f, quoting=csv.QUOTE_ALL)
        [pen.writerow(
            [argv[1], user.get("username"), t.get("completed"), t.get("title")]
         ) for t in todos]
