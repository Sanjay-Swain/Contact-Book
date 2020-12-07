from colorama import Fore, Style


help_str = """
Commands:
    create <email> <Phone> <Name>
    delete <name>
    update <data to be changed: name|phone|email> <old name to be changed>
    find <data to be found: name|phone|email> <data to search>
    preview
    clear
    save
    exit
You can also type help <command> to get a little more info
""" + Fore.RED +"""NOTE: For commands like create and delete the trailing data will be considered as a part of name.
NOTE: The command must be run on same order it is shown.
NOTE: commands are case sensitive""" + Style.RESET_ALL
create_help_str = """Command:
    create <name> <phone> <email>
For example to add a contact:
    create abc@domain.com 1234567890 <full name>
""" + Fore.RED + "NOTE: All of the details be separated by spaces and all last trailing data will be considered as a part of name." + Style.RESET_ALL

delete_help_str = """Command:
    delete <name>
""" + Fore.RED + "NOTE: You must enter the complete exact name (it is case sensitive too)." + Style.RESET_ALL

update_help_str = """Command:
    update <data to be changed: name|phone|email> <old name to be changed>
Example to change phone number of a contact:
    update phone <Name>
""" + Fore.RED + """NOTE: Here name is used as an identifier to identify which contact you need to change.
There will be issues if you have two contact with same exact name.""" + Style.RESET_ALL

find_help_str = """Command:
    find <data to be found: name|phone|email> <data to search>
Example:
    find email abc@domain.com"""

preview_help_str = "This will simply print the current live database"

save_help_str = """This simple command will commit every recent changes to the database.
If you directly close the console without using save command then the recent changes will be lost."""

exit_help_str = """This will commit recent changes to the database and will stop the program."""

clear_help_str = """This will clear the console window"""

def help(command=None):
    if command is None:
        print(help_str)
    elif command == "create":
        print(create_help_str)
    elif command == "delete":
        print(delete_help_str)
    elif command == "update":
        print(update_help_str)
    elif command == "save":
        print(save_help_str)
    elif command == "find":
        print(find_help_str)
    elif command == "exit":
        print(exit_help_str)
    elif command == "preview":
        print(preview_help_str)
    elif command == "clear":
        print(clear_help_str)
    else:
        print("Well it seems like your command doesn't exist.. :(")

if __name__ == "__main__":
    print(help_str)
    print(update_help_str)
    print(create_help_str)