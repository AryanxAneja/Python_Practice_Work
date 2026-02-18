# Create a To Do list manager where users can add, view and remove tasks. Use list for storing.
tasks = []
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task to add: ")
        tasks.append(task)
        print("Task added.")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("Your Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task removed.")
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
