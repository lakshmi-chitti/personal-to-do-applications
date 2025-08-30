import json

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True


def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)


def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            data = json.load(f)
            return [Task(**d) for d in data]
    except FileNotFoundError:
        return []


def main():
    tasks = load_tasks()
    while True:
        print("\n--- Personal To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter category (Work/Personal/Urgent): ")
            tasks.append(Task(title, description, category))
            print("✅ Task Added Successfully!")

        elif choice == '2':
            for i, task in enumerate(tasks):
                status = "✔ Completed" if task.completed else "❌ Pending"
                print(f"{i+1}. {task.title} - {task.description} [{task.category}] --> {status}")

        elif choice == '3':
            num = int(input("Enter task number to mark completed: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num].mark_completed()
                print("✅ Task marked as completed.")

        elif choice == '4':
            num = int(input("Enter task number to delete: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
                print("🗑 Task deleted successfully.")

        elif choice == '5':
            save_tasks(tasks)
            print("📂 Tasks saved. Exiting...")
            break

        else:
            print("❌ Invalid option, try again!")


if __name__ == "__main__":
    main()