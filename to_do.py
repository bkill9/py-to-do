# For displaying colored output
from termcolor import colored

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
        print(colored("\nError: invalid input. Please enter a number between 1 and 7.", "red"))

    # Catch if a user enters something other than an int
    except ValueError:
        print(colored("\nError: invalid input. Please enter a number between 1 and 7.", "red"))

def add_task(tasks):
  """Allow the user to enter task data and add it to the task list.

  Args:
      tasks: A list of task dictionaries.

  Returns:
      None.
  """
  pass

def view_tasks(tasks):
  """Display all tasks in a readable format.

  Args:
      tasks: A list of task dictionaries to display.

  Returns:
      None.
  """
  pass

def complete_task(tasks):
  """Allow the user to select a task and mark it as complete.

  The selected task's status is changed from False (incomplete)
  to True (complete).

  Args:
      tasks: A list of task dictionaries to modify.

  Returns:
      None.
  """
  pass

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
  # Boolean flag for loop control
  active = True

  # Continue displaying menu and gathering input until the user quits
  while active:
    user_choice = get_user_choice()

    # Perform logic for the user's entered menu choice
    match user_choice:
      case 1:
        print("\n--- Add Task ---")
      case 2:
        print("\n--- View All Tasks ---")
      case 3:
        print("\n--- Complete Task ---")
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