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
    staff_file = open("staff.txt", "r")
    for row in staff_file:
        data = row.split(",")
        db_username = data[0]
        db_password = data[1]
        if username == db_username and password == db_password:
            staff_actions()
            session_create()
        else:
            print("Incorrect Login Details")
            print("Try Again")
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
    if action == 1:
        create_bank_account()


def create_bank_account():
    print("Collecting user details")
    acc_name = input("Customer account name >- ")
    opening_balance = input("Customer opening balance >- ")
    acc_type = input("Customer account type >- ")
    acc_email = input("Customer account email >- ")

def session_create():
    print("me")


start()
