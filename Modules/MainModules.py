from prettytable import PrettyTable
from colorama import Fore, Style


def data_insertion(cursor):
    name = input('Enter the name: ')
    phone = input('Enter the phone number :')
    email = input('Enter the email ID :')
    cursor.execute(f"INSERT INTO contact_info VALUES('{name}', '{phone}', '{email}')")


def check_all_contacts(cursor):
    for row in cursor.execute("SELECT * FROM contact_info "):
        if len(row) > 0:
            tab.add_row(list(row))
    print(tab)
    tab.clear_rows()


def get_contact_details(cursor):
    name_id = input("Enter the name: ")
    if name_id == 'all':
        check_all_contacts(cursor)
    else:
        for row in cursor.execute(f"SELECT * FROM contact_info WHERE name = '{str(name_id)}'"):
            tab.add_row(list(row))
        print(tab)
        tab.clear_rows()


def delete_data(cursor):
    data = input('Enter the name: ')
    if data == 'all':
        cursor.execute(f"DROP TABLE contact_info")
        cursor.execute("CREATE TABLE IF NOT EXISTS contact_info (Name char(25), Phone char(25), Email char(40))")
    else:
        cursor.execute(f"DELETE FROM contact_info WHERE name = '{data}'")


def update(cursor):
    identity = input('Enter the name of the entry you want to change: ').lower()
    data_type = input('What do you want to change: Name, Phone, Email: ').lower()
    new_data = input(f"Enter the {data_type} of {identity} you want to change to: ").lower()
    for old_data in cursor.execute(f"SELECT {data_type} FROM contact_info WHERE Name = '{identity}'"):
        print('changes:')
        print(Fore.RED + old_data[0], end='')
        print(Style.RESET_ALL, end='')
        print('   --->   ', end='')
        print(Fore.LIGHTGREEN_EX + new_data, end='')
        print(Style.RESET_ALL)
    cursor.execute(f"UPDATE contact_info SET {data_type.capitalize()} = '{new_data}' WHERE Name = '{identity}'")


def help(cursor):
    print(cursor)
    print(command_list.keys())


tab = PrettyTable(['Name', 'Phone', 'Email'])

command_list = {
    'create': data_insertion,
    'delete': delete_data,
    'find': get_contact_details,
    'help': help,
    'update': update,
}
