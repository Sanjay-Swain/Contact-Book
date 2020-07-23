# v0.1
import sqlite3


def data_insertion(name):
    global changes
    phone = input('Enter the phone number :')
    email = input('Enter the email ID :')
    changes += 1
    c.execute(f"INSERT INTO contact_info VALUES('{name}', '{phone}', '{email}')")


def check_all_contacts():
    for row in c.execute("SELECT * FROM contact_info "):
        print(row)


def get_contact_details(name_id):
    c.execute(f"SELECT * FROM contact_info WHERE name = '{str(name_id)}'")
    print(c.fetchall())
    if name_id == 'all':
        check_all_contacts()


def delete_data(data):
    global changes
    changes += 1
    c.execute(f"DELETE FROM contact_info WHERE name = '{data}'")
    if data == 'all':
        c.execute(f"DROP TABLE contact_info")


conn = sqlite3.connect('contacts.db')

c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS contact_info (Name char(25), Phone char(25), Email char(40))')
changes = 0

command_list = {
    'create': data_insertion,
    'delete': delete_data,
    'find': get_contact_details,
}

while True:
    Command = input("--> ").lower()
    if Command.split()[0] in command_list.keys():
        command_list[Command.split()[0]](Command.split()[1])
    elif Command == 'save' or Command == 'exit':
        break
    else:
        print('Command not found try again.')

if changes > 0:
    print('Your data is added successfully')
conn.commit()
conn.close()
