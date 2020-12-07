
help_str = """Note: commands are case sensitive
NOTE: For commands like create and delete the trailing data will be considered as a part of name.
Commands:
    create <email> <Phone> <Name>
    delete <name>
    update <old name to be changed> <data to be changed: name|phone|email> <new data>
    find <data to be found: name|phone|email> <data to search>
    save
    exit
    """


create_help_str = """Command:
    create [email] [name] [phone]
For example to add a contact:
    create abc@domain.com 1234567890 <full name>
NOTE: All of the details be separated by spaces and all last trailing data will be considered as a part of name."""

delete_help_str = """Command:
    delete <name>
NOTE: You must enter the complete exact name (it is case sensitive too)."""

update_help_str = """Command:
    update <old name to be changed> <data to be changed: name|phone|email> <new data>
Example to change phone number of a contact:
    update <Name> phone 5555555555
NOTE: Here name is used as an identifier to identify which contact you need to change.
There will be issues if you have two contact with same exact name."""

find_help_str = """Command:
    find <data to be found: name|phone|email> <data to search>
Example:
    find email abc@domain.com"""

save_help_str = """This simple command will commit every recent changes to the database.
If you directly close the console without using save command then the recent changes will be lost."""

exit_help_str = """This will commit recent changes to the database and will stop the program."""