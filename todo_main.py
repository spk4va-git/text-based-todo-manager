def load_tasks():
    """Load tasks from CSV file (not implemented yet)."""
    pass

def save_tasks(tasks):
    """Save tasks to CSV file (not implemented yet)."""
    pass

def add_task(tasks):
    pass

def view_tasks(tasks):
    pass

def mark_task_completed(tasks, index):
    pass

def delete_task(tasks, index):
    pass

def main():
    tasks = []
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            idx = input("Enter task number: ")
            # placeholder; index handling not yet implemented
            pass
        elif choice == "4":
            idx = input("Enter task number to delete: ")
            pass
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
