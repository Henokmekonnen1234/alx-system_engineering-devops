#!/usr/bin/python3
"""
Module 3-dictionary_of_list_of_dictionaries.py

In this module a python script will export all data in the JSON format
"""

if __name__ == "__main__":
    from requests import get
    from json import dumps

    url = "https://jsonplaceholder.typicode.com/"
    with get(url + "users") as users, \
         get(url + "todos") as todos, \
         open("todo_all_employees.json", "w+") as file:
        value = {}
        for user in users.json():
            value["{}".format(user.get("id"))] = []
            for todo in todos.json():
                if user.get("id") == todo.get("userId"):
                    key = "{}".format(user.get("id"))
                    value.get(key).append({"username":
                                           user.get("username"),
                                           "task": todo.get("title"),
                                           "completed": todo.get(
                                                "completed")})
        file.write(dumps(value))
