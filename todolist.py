# A simple To-Do List application in Python

# We use a list to store our tasks.
# Each task will be a dictionary containing the task description and its completion status.
# Example: [{"task": "Buy groceries", "completed": False}, {"task": "Do laundry", "completed": True}]
tasks = []

def display_menu():
    """
    Displays the main menu of the application to the user.
    This function doesn't take any arguments and doesn't return anything.
    It simply prints the available options to the console.
    """
    print("\n-------------------------")
    print("  Simple To-Do List App")
    print("-------------------------")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Remove a task")
    print("5. Exit")
    print("-------------------------")

def add_task():
    """
    Prompts the user to enter a new task and adds it to the tasks list.
    The new task is stored as a dictionary with 'task' and 'completed' keys.
    """
    task = input("Enter the new task: ")
    # Append a new dictionary to the tasks list. 'completed' is initially False.
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def view_tasks():
    """
    Displays all current tasks to the user, showing their index, completion status, and description.
    """
    if not tasks:
        # Check if the list is empty and inform the user.
        print("Your to-do list is empty.")
        return

    print("\nYour To-Do List:")
    # Loop through the tasks list using enumerate to get both the index (i) and the task item.
    for i, task_item in enumerate(tasks):
        # Determine the status character: '✓' for completed, ' ' (space) for not completed.
        status = "✓" if task_item["completed"] else " "
        # Print the task number (i+1 for human-readable indexing), status, and task description.
        print(f"{i+1}. [{status}] {task_item['task']}")

def mark_task_complete():
    """
    Allows the user to mark a specific task as complete by its number.
    It first displays the tasks and then asks for the number to update.
    """
    # First, show the user the list of tasks so they know which number to choose.
    view_tasks()
    if not tasks:
        # If the list is empty, there's nothing to mark.
        return

    try:
        # Get the task number from the user. We subtract 1 to get the correct list index.
        task_num = int(input("Enter the number of the task to mark as complete: "))
        # Validate that the entered number is within the valid range of tasks.
        if 1 <= task_num <= len(tasks):
            # Update the 'completed' status of the selected task to True.
            tasks[task_num - 1]["completed"] = True
            print(f"Task {task_num} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        # Handle the case where the user enters non-numeric input.
        print("Invalid input. Please enter a number.")

def remove_task():
    """
    Allows the user to remove a specific task from the list by its number.
    It first displays the tasks and then asks for the number to remove.
    """
    # First, show the user the list of tasks.
    view_tasks()
    if not tasks:
        # If the list is empty, there's nothing to remove.
        return

    try:
        # Get the task number from the user. We subtract 1 to get the correct list index.
        task_num = int(input("Enter the number of the task to remove: "))
        # Validate that the entered number is within the valid range of tasks.
        if 1 <= task_num <= len(tasks):
            # Use the .pop() method to remove the item at the specified index.
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        # Handle the case where the user enters non-numeric input.
        print("Invalid input. Please enter a number.")

def main():
    """
    The main function that controls the application's flow.
    It runs an infinite loop to repeatedly display the menu and handle user input
    until the user chooses to exit.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        # Use if/elif/else to check the user's choice and call the appropriate function.
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Thank you for using the To-Do List App!")
            # Break the loop to exit the application.
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# This is the entry point of the script. The code inside this block will only run
# if the script is executed directly (not when imported as a module).
if __name__ == "__main__":
    main()