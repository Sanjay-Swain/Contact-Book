def data_insertion(cursor):
    name = input('Enter the name: ')
    phone = input('Enter the phone number :')
    email = input('Enter the email ID :')
    cursor.execute(f"INSERT INTO contact_info VALUES('{name}', '{phone}', '{email}')")


def check_all_contacts(cursor):
    for row in cursor.execute("SELECT * FROM contact_info "):
        print(row)


def get_contact_details(cursor):
    name_id = input("Enter the name: ")
    cursor.execute(f"SELECT * FROM contact_info WHERE name = '{str(name_id)}'")
    print(cursor.fetchall())
    if name_id == 'all':
        check_all_contacts(cursor)


def delete_data(cursor):
    data = input('Enter the name: ')
    cursor.execute(f"DELETE FROM contact_info WHERE name = '{data}'")
    if data == 'all':
        cursor.execute(f"DROP TABLE contact_info")


def help():
    print(command_list.keys())


command_list = {
    'create': data_insertion,
    'delete': delete_data,
    'find': get_contact_details,
    'help': help
}
