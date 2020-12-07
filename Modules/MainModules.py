from prettytable import PrettyTable
from colorama import Fore, Style
import sqlite3
try:
    from Modules.HelpModule import help
except ModuleNotFoundError:
    from HelpModule import help
import os


def add(name, phone, email):
    cursor.execute(f"INSERT INTO contact_info VALUES('{name}', '{phone}', '{email}')")


def delete(name):
    cursor.execute(f"DELETE FROM contact_info WHERE name = '{name}'")


def preview():
    if check_contact_exist(None, None, True):
        for row in cursor.execute("SELECT * FROM contact_info "):
            if len(row) > 0:
                tab.add_row(list(row))
        print(tab)
        tab.clear_rows()
    else:
        print('There are no contacts in your contact book.')


def search(data_type, data_val):
    if check_contact_exist(data_type, data_val):
        for row in cursor.execute(f"SELECT * FROM contact_info WHERE {data_type.capitalize()} = '{data_val}'"):
            tab.add_row(list(row))
        print(tab)
        tab.clear_rows()
    else:
        print('The data you are searching for does not exist. Please check the spelling.')


def check_contact_exist(data_type, data_val, everything=False):
    if not everything:
        cursor.execute(f"SELECT * FROM contact_info WHERE {data_type.capitalize()} = '{data_val}'")
        return not len(cursor.fetchall()) == 0
    else:
        cursor.execute(f"SELECT * FROM contact_info")
        return not len(cursor.fetchall()) == 0


def update(name, data_type, new_data):
    try:
        while True:
            if not(check_contact_exist("name", name)):
                print('The data you are searching for does not exist. Please check the spelling.')
                break
            for old_data in cursor.execute(f"SELECT {data_type} FROM contact_info WHERE Name = '{name}'"):
                print('changes:')
                print(Fore.RED + old_data[0], end='')
                print(Style.RESET_ALL, end='')
                print('   --->   ', end='')
                print(Fore.LIGHTGREEN_EX + new_data, end='')
                print(Style.RESET_ALL)
            cursor.execute(f"UPDATE contact_info SET {data_type.capitalize()} = '{new_data}' WHERE Name = '{name}'")
            break
    except sqlite3.OperationalError:
        print(f'Oops!! There are no columns named {data_type}')
        print('You must select from Name, Phone & Email')


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def execute(commands: list):
    """
    :param func: This is a list containing [function, data]
    """
    command_len = len(commands)
    if command_len > 0 and commands[0] in command_list:
        if (command_len < command_requirments[commands[0]]):
            print("More information required to execute the given command")
            print("Type help for more information")
        elif commands[0] == "create":
            add(commands[1], commands[2], commands[3])
        elif commands[0] == "delete":
            delete(commands[1])
        elif commands[0] == "update":
            update(commands[1], commands[2], commands[4])
        elif commands[0] == "find":
            search(commands[1], commands[2])
        elif commands[0] == "preview":
            preview()
        elif commands[0] == "save":
            conn.commit()
        elif commands[0] == "exit":
            running = False
        elif commands[0] == "help":
            try:
                help(commands[1])
            except IndexError:
                help()
        elif commands == "clear":
            clear()
        print("Invalid command")


tab = PrettyTable(['Name', 'Phone', 'Email'])

command_list = ["create", "delete", "update", "find", "preview", "save", "exit"]
command_requirments = {
    "create": 4,
    "delete": 2,
    "update": 3,
    "find": 3,
    "preview": 1,
    "save": 1,
    "exit": 1,
    "help": 1,
    "clear": 1
}

conn = sqlite3.connect('Contacts/contacts.db')

cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS contact_info (Name char(25), Phone char(25), Email char(40))')
running = True

if __name__ == '__main__':
    print('You are currently running the module directly.')
