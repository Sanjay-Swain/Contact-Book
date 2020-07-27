def data_insertion(cursor):
    name = input('Enter the name: ')
    phone = input('Enter the phone number :')
    email = input('Enter the email ID :')
    cursor.execute(f"INSERT INTO contact_info VALUES('{name}', '{phone}', '{email}')")


def check_all_contacts(cursor):
    for row in cursor.execute("SELECT * FROM contact_info "):
        if len(row) > 0:
            print(row)


def get_contact_details(cursor):
    name_id = input("Enter the name: ")
    if name_id == 'all':
        check_all_contacts(cursor)
    else:
        cursor.execute(f"SELECT * FROM contact_info WHERE name = '{str(name_id)}'")
        print(cursor.fetchall())


def delete_data(cursor):
    data = input('Enter the name: ')
    if data == 'all':
        cursor.execute(f"DROP TABLE contact_info")
    else:
        cursor.execute(f"DELETE FROM contact_info WHERE name = '{data}'")


def help(cursor):
    print(cursor)
    print(command_list.keys())


command_list = {
    'create': data_insertion,
    'delete': delete_data,
    'find': get_contact_details,
    'help': help,
}
