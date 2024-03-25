#!/usr/bin/python3
#A script that return info a given employee id
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(argv[1])).json()
    todos = get(url + "todos", params={"userId": argv[1]}).json()
    done_todos = [t for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_todos), len(todos)))
    [print("\t {}".format(t.get("title"))) for t in done_todos]
