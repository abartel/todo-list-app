from typing import List

while True:
    user_action = input("Type add, show, edit, remove, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()
                # do not need to close file if using With

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
                # do not need to close file if using With

        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            # new_todos = [item.strip("\n") for item in todos] - could use as a list comprehension
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)
        case "edit":
            number = int(input("Number of item to edit: "))
            number = number - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("What would you like to change it to?")
            todos[number] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "remove":
            number = int(input("Number of item to remove: "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            remove_index = number - 1
            todo_to_remove = todos[remove_index].strip("\n")
            todos.pop(remove_index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"The {todo_to_remove} item has been vanquished."
            print(message)
        case "exit":
            break

print("Friggin' Bye!!")
