# v1.1
from Modules.MainModules import execute, running, os, c, conn


os.makedirs('Contacts', exist_ok=True)

print("Welcome")
print("Type help to know the commands")
# This part is broken for now after back-end update!

while running:
    Command = input("---> ").lower().strip()
    if Command in command_list.keys():
        command_list[Command](c)
    elif Command == 'save' or Command == 'exit':
        break
    else:
        print('Command not found try again.')

conn.commit()
conn.close()
