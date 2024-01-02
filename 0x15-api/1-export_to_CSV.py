#!/usr/bin/python3
"""Module 1-export_to_CSV.py

in this module using this REST API, for a given employee ID,
will export data in the CSV format.
"""

if __name__ == "__main__":
    from csv import DictWriter
    from json import loads
    from requests import get
    from sys import argv

    url_1 = "https://jsonplaceholder.typicode.com/todos/"
    url_2 = "https://jsonplaceholder.typicode.com/users/"
    value = {1: {"userId": argv[1]}, 2: {"id": argv[1]}}
    with get(url_1, params=value.get(1)) as response, \
         get(url_2, params=value.get(2)) as u:
        if response.status_code == 200 and u.status_code == 200:
            value = loads(response.text)
            user = loads(u.text)
        else:
            value = {}
    if value:
        with open("{}.csv".format(user[0].get("id")), "w", newline="") \
             as file:
            fieldname = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS",\
                         "TASK_TITLE"]
            csv_file = DictWriter(file, fieldname)
            for content in value:
                csv_file.writer.writerow([str(user[0].get("id")), user\
                                         [0].get("name"), content.get(\
                                         "completed"), content.get(\
                                         "title")])
