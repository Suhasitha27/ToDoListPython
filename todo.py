import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks):
        status, desc = task.split("|")
        status_text = "[✓]" if status == "1" else "[ ]"
        print(f"{idx+1}. {status_text} {desc}")

def add_task():
    desc = input("Enter task description: ").strip()
    if desc:
        tasks = load_tasks()
        tasks.append(f"0|{desc}")
        save_tasks(tasks)
        print("Task added.")

def delete_task():
    tasks = load_tasks()
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            del tasks[idx]
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

def complete_task():
    tasks = load_tasks()
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= idx < len(tasks):
            status, desc = tasks[idx].split("|")
            tasks[idx] = f"1|{desc}"
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

def main():
    while True:
        print("\n=== To-Do List ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            display_tasks(load_tasks())
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
