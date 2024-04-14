#  from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The current time is",now)
while True:
    user_action = input("Type add, show, edit, remove, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)  # no need to include file since it's a default argument

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos] - could use as a list comprehension
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("What would you like to change it to?")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Invalid command.")
            continue

    elif user_action.startswith("remove"):
        try:
            number = int(user_action[7:])

            todos = functions.get_todos()
            remove_index = number - 1
            todo_to_remove = todos[remove_index].strip("\n")
            todos.pop(remove_index)

            functions.write_todos(todos)

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
