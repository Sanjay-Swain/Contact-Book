def data_insertion(name, cursor):
    phone = input('Enter the phone number :')
    email = input('Enter the email ID :')
    cursor.execute(f"INSERT INTO contact_info VALUES('{name}', '{phone}', '{email}')")


def check_all_contacts(cursor):
    for row in cursor.execute("SELECT * FROM contact_info "):
        print(row)


def get_contact_details(name_id, cursor):
    cursor.execute(f"SELECT * FROM contact_info WHERE name = '{str(name_id)}'")
    print(cursor.fetchall())
    if name_id == 'all':
        check_all_contacts(cursor)


def delete_data(data, cursor):
    cursor.execute(f"DELETE FROM contact_info WHERE name = '{data}'")
    if data == 'all':
        cursor.execute(f"DROP TABLE contact_info")
