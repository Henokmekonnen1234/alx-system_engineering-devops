#!/usr/bin/python3
"""Module 0-gather_data_from_an_API.py

in this module using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    from json import loads
    from requests import get
    from sys import argv

    url_1 = "https://jsonplaceholder.typicode.com/todos/"
    url_2 = "https://jsonplaceholder.typicode.com/users/"
    value = {1: {"userId": argv[1]}, 2: {"id": argv[1]}}
    count = 0
    with get(url_1, params=value.get(1)) as response, \
         get(url_2, params=value.get(2)) as u:
        if response.status_code == 200 and u.status_code == 200:
            value = loads(response.text)
            user = loads(u.text)
        else:
            value = {}
    if value:
        for todos in value:
            if todos.get("completed") is True:
                count += 1
        print("Employee {} is done with tasks({}/{}):".format(
              user[0].get("name"), count, len(value)))
        for todos in value:
            if todos.get("completed") is True:
                print("     {}".format(todos.get("title")))
