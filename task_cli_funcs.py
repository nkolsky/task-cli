import json
from pathlib import Path
from datetime import datetime

file_path = Path("tasks.json")

def load_tasks():
    """
    Load tasks from JSON file if it exists. 

    Returns:
        list: A list of dictionaries, each containing 'id', 'description',
              'status', 'createdAt', and 'updatedAt' fields.
    """

    if file_path.is_file():
        with file_path.open("r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """
    Saves a list of tasks to a JSON file atomically.

    Writes tasks to a temporary file and renames it to the target file, 
    ensuring data integrity by avoiding partial writes.

    Args:
        tasks (list): List of task dictionaries with fields like 'id', 
                      'description', 'status', 'createdAt', and 'updatedAt'.
                      
    Raises:
        IOError: If there is an issue with file writing or renaming.
    """

    temp_file_path = file_path.with_suffix(".tmp")  # Create a temporary file path
    
    # Write to the temporary file first
    with temp_file_path.open("w") as temp_file:
        json.dump(tasks, temp_file, indent=2)
    
    # Rename the temp file to the original file (atomic operation)
    temp_file_path.replace(file_path)

def get_next_id(tasks):
    """
    Returns the next task ID based on the highest ID in the provided task list.

    Args:
        tasks (list): List of task dictionaries, each with an 'id' key.

    Returns:
        int: The next available task ID, starting at 1 if the list is empty.
    """
    
    if tasks:
        max_id = max(task["id"] for task in tasks)
        return max_id + 1
    
    return 1  # Start IDs from 1 if no tasks exist

def add(task):
    """
    Adds a new task to the task list with a unique ID and default status.

    Args:
        task (str): The description of the new task.

    Creates a task with 'todo' status, timestamps, and a unique ID, then saves 
    it to the JSON file and confirms the addition.
    """

    tasks = load_tasks()

    new_task = {
        "id": get_next_id(tasks),
        "description": task,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(new_task)

    save_tasks(tasks)

    print(f"Task \"{task}\" added with ID {new_task['id']}.")

def list_tasks():
    """
    Displays all tasks with their ID, description, and status.

    If no tasks are available, prints a message indicating so.
    """

    tasks = load_tasks()

    if tasks:
        for task in tasks:
            print(f"{task['id']}: {task['description']} - Status: {task['status']}")
    else:
        print("No tasks available.")

def list_tasks_by_status(status):
    """
    Displays tasks that match the specified status.

    Args:
        status (str): The task status to filter by. Must be 'todo', 'in-progress', or 'done'.

    If no tasks match or an invalid status is provided, prints an appropriate message.
    """
    status = status.lower()

    if not (status == "todo" or status == "in-progress" or status == "done"):
        print("Status invalid. Please enter a valid status and try again.")
        return
    
    tasks = load_tasks()

    tasks_to_list = []
    
    for task in tasks:
        if task['status'] == status:
            tasks_to_list.append(task)
    
    if not tasks_to_list: # No tasks were added to the list to print
        print(f"There are no tasks with '{status}' status.")
    else:
        print(f"The following tasks are on your '{status}' list:")
        
        for task in tasks_to_list:
            print(f"{task['id']}: {task['description']}")

def mark_in_progress(id):
    """
    Marks the task with the given ID as 'in-progress' and updates its timestamp.

    Args:
        id (int): The ID of the task to update.

    If the ID is invalid, prints an error message.
    """

    tasks = load_tasks()

    task_updated = False

    for task in tasks:
        if task['id'] == int(id):
            task['status'] = "in-progress"
            task['updatedAt'] = datetime.now().isoformat()
            print(f"{task['id']}: {task['description']} - Status: {task['status']}")
            save_tasks(tasks)
            task_updated = True
            break
    
    if not task_updated:
        print("Invalid ID. Please enter a valid ID and try again.")

def mark_done(id):
    """
    Marks the task with the given ID as 'done' and updates its timestamp.

    Args:
        id (int): The ID of the task to update.

    If the ID is invalid, prints an error message.
    """

    tasks = load_tasks()
    
    task_updated = False
    
    for task in tasks:
        if task['id'] == int(id):
            task['status'] = "done"
            task['updatedAt'] = datetime.now().isoformat()
            print(f"{task['id']}: {task['description']} - Status: {task['status']}")
            save_tasks(tasks)
            task_updated = True
            break
    
    if not task_updated:
        print("Invalid ID. Please enter a valid ID and try again.")

def update(id, description):
    """
    Updates the description of the task with the given ID and updates its timestamp.

    Args:
        id (int): The ID of the task to update.
        description (str): The new description for the task.

    If the ID is invalid, prints an error message.
    """
    
    tasks = load_tasks()
    
    task_updated = False
    
    for task in tasks:
        if task['id'] == int(id):
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            print(f"{task['id']}: {task['description']} - Status: {task['status']}")
            save_tasks(tasks)
            task_updated = True
            break
    
    if not task_updated:
        print("Invalid ID. Please enter a valid ID and try again.")

def delete(id):
    """
    Deletes the task with the given ID and adjusts IDs of subsequent tasks.

    Args:
        id (int): The ID of the task to delete.

    If the ID is invalid, prints an error message.
    """
    
    tasks = load_tasks()
    
    task_deleted = False
    
    tasks_updated = []

    for task in tasks:
        if task['id'] == int(id):
            task_deleted = True
            deleted_task = task
        else:
            tasks_updated.append(task)
    
    if task_deleted:
        for task in tasks_updated:
            if task['id'] > deleted_task['id']:
                task['id'] -= 1
    
    save_tasks(tasks_updated)

    if not task_deleted:
        print("Invalid ID. Please enter a valid ID and try again.")
    else:
        print(f"Task {deleted_task['id']}: {deleted_task['description']} deleted successfully.")
