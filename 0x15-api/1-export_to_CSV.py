#!/usr/bin/python3
"""Module 1-export_to_CSV.py

in this module using this REST API, for a given employee ID,
will export data in the CSV format.
"""

if __name__ == "__main__":
    from json import loads
    from requests import get
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/"
    value = {1: {"userId": argv[1]}, 2: {"id": argv[1]}}
    with get(url + "/todos/", params=value.get(1)) as response, \
         get(url + "/users/", params=value.get(2)) as u:
        if response.status_code == 200 and u.status_code == 200:
            value = loads(response.text)
            user = loads(u.text)
        else:
            value = {}
    if value:
        with open("{}.csv".format(user[0].get("id")), "w", newline="") \
             as csv_file:
            for todo in value:
                csv_file.write("\"{}\",\"{}\",\"{}\",\"{}\"".format(user\
                               [0].get("id"), user[0].get("username"),
                               todo.get("completed"), todo.get("title")))
