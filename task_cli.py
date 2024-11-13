from task_cli_funcs import *
import sys

# If no task file, create the file in the current directory
if not file_path.is_file():
    file_path.write_text(json.dumps([]))

if len(sys.argv) < 2: # No command was given
    print("Welcome to your task manager. Please input a command to update or check your task list.")
else:
    command = sys.argv[1] # Save command to variable
    
    command = command.lower() #convert the command to lowercase

    if command == "add":
        if len(sys.argv) > 2: # Make sure a task was actually given to add
            add(sys.argv[2])
        else:
            print("Please enter a task to add and try again.")
    elif command == "list":
        # Check which tasks the user wants listed
        if len(sys.argv) > 2: # User has specific tasks they want listed
            status = sys.argv[2]
            list_tasks_by_status(status)
        else: # The user wants all tasks listed
            list_tasks()
    elif command == "mark-in-progress":
        if len(sys.argv) > 2: # Make sure the user provides an ID
            try:
                mark_in_progress(sys.argv[2])
            except ValueError:
                print("Invalid ID. Please enter a valid, positive integer ID and try again.") 
        else:
            print("Please provide the ID of the task you want to update and try again.")
    elif command == "mark-done":
        if len(sys.argv) > 2: # Make sure the user provides an ID
            try:
                mark_done(sys.argv[2])
            except ValueError:
                print("Invalid ID. Please enter a positive integer ID and try again.")
        else:
            print("Please provide the ID of the task you want to update and try again.")
    elif command == "update":
        if len(sys.argv) < 4: # The user either forgot to put an id or forgot to give the update
            print("Please provide the ID followed by the update you'd like to make and try again.")
        else:
            try:
                update(sys.argv[2], sys.argv[3])
            except ValueError:
                print("Please enter a positive integer ID, followed by the desired update and try again.")
    elif command == "delete":
        if len(sys.argv) > 2: # Make sure the user provided the ID of the task to delete
            try:
                delete(sys.argv[2])
            except ValueError:
                print("Invalid ID. Please enter a positive integer ID and try again.")
        else:
            print("Please provide the ID of the task you want to delete and try again.")
    else:
        print("Invalid command. Please try again.")



    

