from prettytable import PrettyTable
from colorama import Fore, Style
import sqlite3


def add(cursor, name, phone, email):
    cursor.execute(f"INSERT INTO contact_info VALUES('{name}', '{phone}', '{email}')")


def delete(cursor, name):
    cursor.execute(f"DELETE FROM contact_info WHERE name = '{name}'")


def preview(cursor):
    if check_contact_exist(cursor, None, None, True):
        for row in cursor.execute("SELECT * FROM contact_info "):
            if len(row) > 0:
                tab.add_row(list(row))
        print(tab)
        tab.clear_rows()
    else:
        print('There are no contacts in your contact book.')


def search(cursor, data_type, data_val):
    if check_contact_exist(cursor, data_type, data_val):
        for row in cursor.execute(f"SELECT * FROM contact_info WHERE {data_type.capitalize()} = '{data_val}'"):
            tab.add_row(list(row))
        print(tab)
        tab.clear_rows()
    else:
        print('The data you are searching for does not exist. Please check the spelling.')


def check_contact_exist(cursor, data_type, data_val, everything=False):
    if not everything:
        cursor.execute(f"SELECT * FROM contact_info WHERE {data_type.capitalize()} = '{data_val}'")
        return not len(cursor.fetchall()) == 0
    else:
        cursor.execute(f"SELECT * FROM contact_info")
        return not len(cursor.fetchall()) == 0


def update(cursor, name, data_type, new_data):
    try:
        while True:
            if not(check_contact_exist(cursor, "name", name)):
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


tab = PrettyTable(['Name', 'Phone', 'Email'])

command_list = ["create", "delete", "update", "find", "preview", "save", "exit"]

if __name__ == '__main__':
    print('You are currently running the module directly.')
