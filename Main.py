# v0.1.1-alpha
from Modules.MainModules import *
import sqlite3
import os


os.makedirs('C:/Contact Book', exist_ok=True)
conn = sqlite3.connect('C:/Contact Book/contacts.db')

c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS contact_info (Name char(25), Phone char(25), Email char(40))')

print("Welcome")
print("Type help to know the commands")
while True:
    Command = input("--> ").lower()
    if Command.split()[0] in command_list.keys():
        command_list[Command]()
    elif Command == 'save' or Command == 'exit':
        break
    else:
        print('Command not found try again.')

conn.commit()
conn.close()
