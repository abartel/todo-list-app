from typing import List

while True:
    user_action = input("Type add, show, edit, remove, or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
            # do not need to close file if using With

    elif "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # new_todos = [item.strip("\n") for item in todos] - could use as a list comprehension
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif "edit" in user_action:
        number = int(user_action[5:])

        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("What would you like to change it to?")
        todos[number] = new_todo + "\n"

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "remove" in user_action:
        number = int(user_action[7:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()
        remove_index = number - 1
        todo_to_remove = todos[remove_index].strip("\n")
        todos.pop(remove_index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"The {todo_to_remove} item has been vanquished."
        print(message)

    elif "exit" in user_action:
        break

    else:
        print("Wrong command Bubba!")

print("Friggin' Bye!!")
