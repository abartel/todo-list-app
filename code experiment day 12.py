def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local # filepath would cause an attribute error because it would be bringing back the filename, and not the todos list


def write_todos(filepath, todos_arglocal):
    with open(filepath, 'w') as file:
        file.writelines(todos_arglocal)


while True:
    user_action = input("Type add, show, edit, remove, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + "\n")

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        # new_todos = [item.strip("\n") for item in todos] - could use as a list comprehension
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("What would you like to change it to?")
            todos[number] = new_todo + "\n"

            write_todos("todos.txt", todos)

        except ValueError:
            print("Invalid command.")
            continue

    elif user_action.startswith("remove"):
        try:
            number = int(user_action[7:])

            todos = get_todos("todos.txt")
            remove_index = number - 1
            todo_to_remove = todos[remove_index].strip("\n")
            todos.pop(remove_index)

            write_todos("todos.txt", todos)

            message = f"The {todo_to_remove} item has been vanquished."
            print(message)

        except IndexError:
            print("No item with that number!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Wrong command Bubba!")

print("Friggin' Bye!!")
