#!/usr/bin/python3
"""Module 2-export_to_JSON.py
Python script to export data in the JSON format.
"""

from sys import argv
from requests import get
from json import dumps, loads

url = "https://jsonplaceholder.typicode.com/"
with open("{}.json".format(argv[1]), "w+") as file, \
     get(url + "users/", params={"id": argv[1]}) as user, \
     get(url + "todos/", params={"userId": argv[1]}) as todos:
    users = loads(user.text)
    value = loads(todos.text)
    values = {"\"{}\"".format(users[0].get("id")): []}
    for todo in value:
        values.get("\"{}\"".format(users[0].get("id")))\
              .append({"task": todo.get("title"), "completed":
                       todo.get("completed"), "username":
                       users[0].get("username")})
    file.write(dumps(values))
