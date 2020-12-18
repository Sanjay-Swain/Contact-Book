from colorama import Fore, Style


help_str = """
Commands:
    create <email> <Phone> <Name>
    delete <ID>
    update <data to be changed: name|phone|email> <old name to be changed>
    find <data to be found: name|phone|email> <data to search>
    preview
    clear
    exit
You can also type help <command> to get a little more info
""" + Fore.RED +"""NOTE: For commands like create and delete the trailing data will be considered as a part of name.
NOTE: The command must be run on same order it is shown.
NOTE: commands are case sensitive""" + Style.RESET_ALL
create_help_str = """Command:
    create <email> <phone> <name>
For example to add a contact:
    create abc@domain.com 1234567890 <full name>
""" + Fore.RED + "NOTE: All of the details be separated by spaces and all last trailing data will be considered as a part of name." + Style.RESET_ALL

delete_help_str = """Command:
    delete <ID>
""" + Fore.RED + "NOTE: You must enter the exact ID." + Style.RESET_ALL

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

exit_help_str = """This will commit recent changes to the database and will stop the program."""

clear_help_str = """This will clear the console window"""

help_func = {
    "create": create_help_str,
    "delete": delete_help_str,
    "update": update_help_str,
    "find": find_help_str,
    "exit": exit_help_str,
    "preview": preview_help_str,
    "clear": clear_help_str,
    "help": help_str
}

def help_command(command=None):
    if command is None:
        command = "help"
    try:
        print(help_func[command])
    except KeyError:
        print("Well it seems like your command doesn't exist.. :(")



if __name__ == "__main__":
    print("=====You are running the program directly=====")
    help_command("create")
    help_command("gjvasd")