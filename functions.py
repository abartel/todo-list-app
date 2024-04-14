def get_todos(filepath="todos.txt"):  # by adding file name, no need to repeat it throughout
    # the code whenever get_todos is called
    """ Read text file and return list of items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arglocal, filepath="todos.txt"):  # non-default parameters always go before default
    """ Write list items in text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arglocal)

