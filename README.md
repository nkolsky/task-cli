# Task Tracker CLI

A simple command-line tool for managing tasks, including adding, listing, updating, and deleting tasks. Tasks are saved to a JSON file, preserving data between sessions.

This project is based on the challenge from: https://roadmap.sh/projects/task-tracker

## Features
- **Add** new tasks with unique IDs
- **List** all tasks or filter by status (`todo`, `in-progress`, `done`)
- **Update** task descriptions or mark as in-progress/done
- **Delete** tasks by ID, with automatic ID adjustment
- **Atomic Save** for reliable data integrity

## Setup

1. **Requirements**: Python 3.6+
2. **Installation**:
   ```bash
   git clone https://github.com/your-username/task-tracker-cli.git
   cd task-tracker-cli
   ```

## Usage

Run `task_cli.py` with these commands:

- **Add a Task**: `python task_cli.py add "Task description"`
- **List Tasks**: `python task_cli.py list`
- **List by Status**: `python task_cli.py list <status>`
  - `<status>` can be one of `todo`, `in-progress`, or `done`
- **Mark as In-Progress**: `python task_cli.py mark-in-progress <task_id>`
- **Mark as Done**: `python task_cli.py mark-done <task_id>`
- **Update Description**: `python task_cli.py update <task_id> "New description"`
- **Delete a Task**: `python task_cli.py delete <task_id>`

### Example Workflow

  ```bash
  python task_cli.py add "Buy groceries"
  python task_cli.py list
  python task_cli.py mark-in-progress 1
  python task_cli.py update 1 "Buy groceries and snacks"
  python task_cli.py delete 1
  ```

### Notes
- **Error Handling**: Commands check for missing arguments, invalid IDs, and status validation.
- **File Structure:
  -`task_cli.py`: CLI for user commands
  - `task_cli_funcs.py`: Core task management functions
