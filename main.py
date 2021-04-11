## Filename: main.py
 # Author: Marcelo Feitoza Parisi
 # 
 # Description: Main component
 # of gcs-reporting tool.
 # 
 # ###########################
 # # DISCLAIMER - IMPORTANT! #
 # ###########################
 # 
 # Stuff found here was built as a
 # Proof-Of-Concept or Study material
 # and should not be considered
 # production ready!
 # 
 # USE WITH CARE!
##
from lib import cmd
from lib import sc 
from lib import size 
from lib import date
from lib import name

def main():
    # Parsing command line arguments
    arguments = cmd.args()

    # Invoking the correct subsystem
    if(arguments.command == "storageclass"):
        # Check usage by storage class
        sc.exec(arguments.bucket[0], arguments.project[0])
    elif(arguments.command == "name"):
        # List by name
        name.exec(arguments.bucket[0], arguments.project[0], arguments.reverse)
    elif(arguments.command == "size"):
        # List by size
        size.exec(arguments.bucket[0], arguments.project[0], arguments.reverse, arguments.number)
    elif(arguments.command == "date"):
        # List by date
        date.exec(arguments.bucket[0], arguments.project[0], arguments.reverse, arguments.number)
    else:
        # No subsystem provided
        # we should not get here
        print("ERROR: internal error")
    
if __name__ == '__main__':
    main()