queue = []

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice==1:
        element=int(input("Enter element to insert: "))
        queue.append(element)
        print( element , " inserted into queue")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty. Deletion not possible")
        else:
            removed = queue.pop(0)
            print(removed, " removed from queue")

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements:", queue)

    elif choice == 4:
        print("Exiting program")
        break

    else:
        print("Invalid choice. Please try again.")
