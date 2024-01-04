#!/usr/bin/python3
"""Module 2-export_to_JSON.py

Python script to export data in the JSON format.
"""

if __name__ == "__main__":
    from sys import argv
    from requests import get
    from json import dumps, loads

    url = "https://jsonplaceholder.typicode.com/"
    with open("{}.json".format(argv[1]), "w+") as file, \
         get(url + "users/", params={"id": argv[1]}) as user, \
         get(url + "todos/", params={"userId": argv[1]}) as todos:
        users = loads(user.text)
        value = loads(todos.text)
        dict_val = {f"{argv[1]}": []}
        for todo in value:
            dict_val.get(f"{argv[1]}").append({"task": todo.get("title"),
                                               "completed": todo.get(
                                               "completed"), "username":
                                               users[0].get("username")})
        file.write(dumps(dict_val))
