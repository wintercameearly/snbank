import json
import random
import os
import string
import ast


def start():
    """Options for user actions"""
    print("""
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    WELCOME TO SN BANK
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    1. Staff Login
    2. Close App
    """)
    action = int(input(">- "))
    if action == 1:
        login()
    else:
        close()


def login():
    username = input("Username  ").lower()
    password = input("Password  ")
    with open("staff.txt", "r") as staff_file:

        staff = json.load(staff_file)
        for n in staff["db"]:
            if username == n["username"].lower() and password == n["password"]:
                session(create, loggedin)
                staff_actions()
            else:
                print("Wrong details")
                login()


def staff_actions():
    print("""
    STAFF ACTIONS
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    1. Create new bank account
    2. Check account details
    2. Logout
    """)
    action = int(input(">-"))


def session():
    print("me")


start()
