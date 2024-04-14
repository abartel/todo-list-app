while True:
    user_action = input("Type add, show, edit, remove, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt","r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            file = open("todos.txt","r")
            todos = file.readlines()
            file.close()
            #new_todos = [item.strip("\n") for item in todos]
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)
        case "edit":
            number = int(input("Number of item to edit: "))
            number = number - 1
            new_todo = input("What would you like to change it to?")
            todos[number] = new_todo
        case "remove":
            number = int(input("Number of item to remove: "))
            todos.pop(number-1)
        case "exit":
            break

print("Friggin' Bye!!")