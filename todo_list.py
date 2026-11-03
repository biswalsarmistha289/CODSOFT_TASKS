

import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def view_tasks():
    if not tasks:
        print("\nNo tasks found!")
        return

    print("\n====== YOUR TODO LIST ======")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")

# Add a new task
def add_task():
    title = input("\nEnter your task: ").strip()

    if not title:
        print("Task cannot be empty!")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    save_tasks()
    print("Task added successfully!")

# Mark task as completed
def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks()
            print("Task completed successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")

# Delete a task
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print(f"Task '{removed['title']}' deleted successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")

# Main program
tasks = load_tasks()

while True:
    print("\n========== TODO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank you for using Todo List!")
        break

    else:
        print("Invalid choice! Please try again.")
      