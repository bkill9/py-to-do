# Python To-Do List Manager

## Description

A simple command-line to-do list application written in Python. Users can create and manage tasks, mark tasks as complete, and save or load their tasks using JSON files.

## Features

- Add tasks
- View all tasks
- Complete tasks
- Remove tasks
- Save tasks to a JSON file
- Load tasks from a JSON file
- Validate task dates
- Validate user input

## Requirements

- Python 3.14.4
- `termcolor 3.3.0`
- `datetime` and `json` from the Python standard library

## Installation / Setup

Clone the repository:

```bash
git clone https://github.com/bkill9/py-to-do.git
```

Navigate into the project directory:

```bash
cd py-to-do
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Usage

Run `to_do.py` with Python:

```bash
python to_do.py
```

### App Menu

```
1. Add Task
2. View All Tasks
3. Complete Task
4. Remove Task
5. Save Tasks
6. Load Tasks
7. Quit
Select an option from the menu:
```

The program provides the following options:

1. **Add Task** — Add a new task with a name and due date.
2. **View All Tasks** — Display all current tasks.
3. **Complete Task** — Mark a task as completed.
4. **Remove Task** — Remove a task from the list.
5. **Save Tasks** — Save the current task list to a JSON file.
6. **Load Tasks** — Load a previously saved task list.
7. **Quit** — Exit the program.

## Data Storage

Tasks are stored as dictionaries and can be saved to a JSON file. Each task contains:

```json
{
  "status": false,
  "date": "12/31/2026",
  "name": "Example task"
}
```

When loading a JSON file, the saved tasks are added back into the program so they can be managed normally.

## Input Rules

- Dates must be entered using the `MM/DD/YYYY` format.
- Task dates cannot be in the past.
- Task names cannot be empty.
- JSON filenames must end with `.json`.
- Menu and task selections must be valid numbers.

## Example (Adding, Viewing, Completing, and Removing Tasks)

```text
=== To-Do List Manager ===

1. Add Task
2. View All Tasks
3. Complete Task
4. Remove Task
5. Save Tasks
6. Load Tasks
7. Quit
Select an option from the menu: 1

--- Add Task ---

Enter task date (MM/DD/YYYY): 12/31/2026
Enter task name: Finish Python Project

[12/31/2026 - Finish Python Project] has been added to the task list!

1. Add Task
2. View All Tasks
3. Complete Task
4. Remove Task
5. Save Tasks
6. Load Tasks
7. Quit
Select an option from the menu: 2

--- View All Tasks ---

1. [ ] 12/31/2026 - Finish Python Project

1. Add Task
2. View All Tasks
3. Complete Task
4. Remove Task
5. Save Tasks
6. Load Tasks
7. Quit
Select an option from the menu: 3

--- Complete Task ---

1. [ ] 12/31/2026 - Finish Python Project
Select a task to complete: 1

[12/31/2026 - Finish Python Project] has been marked as complete!

1. Add Task
2. View All Tasks
3. Complete Task
4. Remove Task
5. Save Tasks
6. Load Tasks
7. Quit
Select an option from the menu: 4

--- Remove Task ---

1. [X] 12/31/2026 - Finish Python Project
Select a task to remove: 1

[12/31/2026 - Finish Python Project] has been removed from the task list!

1. Add Task
2. View All Tasks
3. Complete Task
4. Remove Task
5. Save Tasks
6. Load Tasks
7. Quit
Select an option from the menu: 7

Quitting...
Thank you. Goodbye.
```
