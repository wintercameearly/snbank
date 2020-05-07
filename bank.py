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
            session_create()
            staff_actions()

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
    3. Logout
    """)
    action = int(input(">-"))
    if action == 1:
        create_bank_account()
    elif action == 2:
        check_bank_details()
    else:
        logout()


def create_bank_account():
    print("Collecting user details")
    acc_name = input("Customer account name >- ")
    opening_balance = input("Customer opening balance >- ")
    acc_type = input("Customer account type >- ")
    acc_email = input("Customer account email >- ")
    acc_number = "".join(random.choice(string.digits) for i in range(10))
    account = open("customer.txt", "a")
    account.write(acc_number)
    account.write(",")
    account.write(acc_name)
    account.write(",")
    account.write(opening_balance)
    account.write(",")
    account.write(acc_type)
    account.write(",")
    account.write(acc_email)
    account.write("\n")
    print(f"The account number is {acc_number}")
    staff_actions()


def check_bank_details():
    check_acc_number = input("What is the users account number")
    details = open("customer.txt", "r")
    for row in details:
        data = row.split(",")
        acc_number = data[0]
        print(data)
        if acc_number == check_acc_number:
            print(row)
    staff_actions()


def session_create():
    session = open("session.txt","a")
    session.write("User has logged in")


def logout():
    os.unlink("session.txt")
    start()


def close():
    return 0


start()
