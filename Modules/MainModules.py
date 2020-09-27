from prettytable import PrettyTable
from colorama import Fore, Style
import sqlite3


def data_insertion(cursor):
    name = input('Enter the name: ')
    phone = input('Enter the phone number :')
    email = input('Enter the email ID :')
    cursor.execute(f"INSERT INTO contact_info VALUES('{name}', '{phone}', '{email}')")


def check_all_contacts(cursor):
    if check_contact_exist(cursor, None, True):
        for row in cursor.execute("SELECT * FROM contact_info "):
            if len(row) > 0:
                tab.add_row(list(row))
        print(tab)
        tab.clear_rows()
    else:
        print('There are no contacts in your contact book add some data to check everything.')


def get_contact_details(cursor):
    name_id = input("Enter the name: ")
    if name_id == 'all':
        check_all_contacts(cursor)
    else:
        if check_contact_exist(cursor, name_id):
            for row in cursor.execute(f"SELECT * FROM contact_info WHERE name = '{str(name_id)}'"):
                tab.add_row(list(row))
            print(tab)
            tab.clear_rows()
        else:
            print('The data you are searching for does not exist. Please check the spelling.')


def delete_data(cursor):
    data = input('Enter the name: ')
    if data == 'all':
        cursor.execute(f"DROP TABLE contact_info")
        cursor.execute("CREATE TABLE IF NOT EXISTS contact_info (Name char(25), Phone char(25), Email char(40))")
    else:
        cursor.execute(f"DELETE FROM contact_info WHERE name = '{data}'")


def check_contact_exist(cursor, name, everything=False):
    if not everything:
        cursor.execute(f"SELECT * FROM contact_info WHERE Name = '{name}'")
        return not len(cursor.fetchall()) == 0
    else:
        cursor.execute(f"SELECT * FROM contact_info")
        return not len(cursor.fetchall()) == 0


def update(cursor):
    try:
        while True:
            identity = input('Enter the name of the entry you want to change: ').lower()
            if not(check_contact_exist(cursor, identity)):
                print('The data you ae searching for does not exist. Please check the spelling.')
                break
            data_type = input('What do you want to change: Name, Phone, Email: ').lower()
            new_data = input(f"Enter the {data_type} of {identity} you want to change to: ")
            for old_data in cursor.execute(f"SELECT {data_type} FROM contact_info WHERE Name = '{identity}'"):
                print('changes:')
                print(Fore.RED + old_data[0], end='')
                print(Style.RESET_ALL, end='')
                print('   --->   ', end='')
                print(Fore.LIGHTGREEN_EX + new_data, end='')
                print(Style.RESET_ALL)
            cursor.execute(f"UPDATE contact_info SET {data_type.capitalize()} = '{new_data}' WHERE Name = '{identity}'")
            break
    except sqlite3.OperationalError:
        print(f'Oops!! There are no columns named {data_type}')
        print('You must select from Name, Phone & Email')


def help(cursor):
    print(command_list.keys())
    print("If you want to print/delete every data just type 'all' in the enter name prompt")


tab = PrettyTable(['Name', 'Phone', 'Email'])

command_list = {
    'create': data_insertion,
    'delete': delete_data,
    'find': get_contact_details,
    'help': help,
    'update': update,
}

if __name__ == '__main__':
    print('You are currently running the module directly.')
