tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choose option:")

    if choice == "1":
        task = input("Enter Task:")
        tasks.append(task)
    elif choice == "2":
        print("Your Tasks:")
        for i, t in enumerate(tasks, 1):
            print(i, "-", t)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

