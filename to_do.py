# For displaying colored output
from termcolor import colored

# For checking date formatting
from datetime import datetime

def display_menu():
  """Displays menu options.

  Args:
      None.
  
  Returns:
      None.
  """
  # Print menu options
  print("\n1. Add Task")
  print("2. View All Tasks")
  print("3. Complete Task")
  print("4. Remove Task")
  print("5. Save Tasks")
  print("6. Load Tasks")
  print("7. Quit")

def get_user_choice():
  """Calls the display_menu function and asks the user for their choice.

  Args:
      None.

  Returns:
      menu_choice: An integer that the user inputs that represents the action 
      from the menu that they'd like to take.
  """
  # Loop to keep prompting the user unil a valid int is entered
  while True:

    display_menu()

    try:

      # Prompt the user for their choice
      menu_choice = int(input("Select an option from the menu: "))

      # Verify that menu_choice is between 1 and 7
      if menu_choice in range(1, 8):
        return menu_choice
      else:
        print(colored("\nError - Please enter a number between 1 and 7", "red"))

    # Catch if a user enters something other than an int
    except ValueError:
        print(colored("\nError - Please enter a number between 1 and 7", "red"))

def validate_date(date):
  """Checks if the user entered date is formatted as MM/DD/YYYY.

  Args:
      date: User entered task date.
  
  Returns:
      True or False.
  """
  try:

    # Check the length of the string to enforce leading zeros in dates
    if len(date) == 10:
      datetime.strptime(date, "%m/%d/%Y")
      return True
    else:
      return False

  except ValueError:
    return False

def add_task(tasks):
  """Allow the user to enter task data and add it to the task list.

  Args:
      tasks: A list of task dictionaries.

  Returns:
      None.
  """
  # Loop to keep prompting the user until a valid date is entered
  while True:

      # Prompt user for task date
      task_date = input("Enter task date (MM/DD/YYYY): ")

      # Verify that the task date is formatted correctly before continuing
      formatted = validate_date(task_date)

      if formatted:
        task_name = input("Enter task name: ")

        # Create task dictionary and add it to task list
        task_status = False

        task_dictionary = {
          "status": task_status, 
          "date": task_date, 
          "name": task_name}

        tasks.append(task_dictionary)

        # Print a success message
        print(f"\n[{task_date} - {task_name}] has been added to the task list!")

        # End the loop
        break
      else:
        print(colored("\nError - Please enter a valid date in MM/DD/YYYY format.\n", 
                      "red"))

def view_tasks(tasks):
  """Display all tasks in a readable format.

  Args:
      tasks: A list of task dictionaries to display.

  Returns:
      None.
  """
  for i, task in enumerate(tasks):

    # Get task info from dictionary
    task_status = task.get("status")
    task_date = task.get("date")
    task_name = task.get("name")

    # Check completion status for checkbox display
    if task_status:
      checkbox = "[X]"
    else:
      checkbox = "[ ]"

    # Print task with index + 1 for readability
    print(f"{i + 1}. {checkbox} {task_date} - {task_name}")

def complete_task(tasks):
  """Allow the user to select a task and mark it as complete.

  The selected task's status is changed from False (incomplete)
  to True (complete).

  Args:
      tasks: A list of task dictionaries to modify.

  Returns:
      None.
  """
  # Display the task list
  view_tasks(tasks)

  # Keep prompting the user until a valid task is entered
  while True:

    # Prompt the user for their choice
    task_to_complete = int(input("Select a task to complete: "))

    try:

      # Convert input into index
      index_to_complete = task_to_complete - 1

      # Change status of the task to True
      tasks[index_to_complete]["status"] = True

      # End loop
      break

    except IndexError:
      print(colored("\nError - Please enter a task from the task list.\n", "red"))

def remove_task(tasks):
  """Allow the user to select a task and remove it from the task list.

  Args:
      tasks: A list of task dictionaries to modify.

  Returns:
      None.
  """
  pass

def save_tasks(tasks):
  """Allow the user to enter a JSON filename and write the task list to it.

  Args:
      tasks: A list of task dictionaries to write to a JSON file.

  Returns:
      None.
  """
  pass

def load_tasks():
  """Load task data from a JSON file.

  Returns:
      A list of dictionaries populated with task data.
  """
  pass

def main():
  print("\n=== To-Do List Manager ===")

  # Initialize empty task list
  tasks = []

  # Boolean flag for loop control
  active = True

  # Continue displaying menu and gathering input until the user quits
  while active:
    user_choice = get_user_choice()

    # Perform logic for the user's entered menu choice
    match user_choice:
      case 1:
        print("\n--- Add Task ---\n")
        add_task(tasks)
      case 2:
        print("\n--- View All Tasks ---\n")
        view_tasks(tasks)
      case 3:
        print("\n--- Complete Task ---\n")
        complete_task(tasks)
      case 4:
        print("\n--- Remove Task ---")
      case 5:
        print("\n--- Save Tasks ---")
      case 6:
        print("\n--- Load Tasks ---")
      case 7:
        print("\nQuitting...")
        active = False
        print("Thank you. Goodbye\n")

main()