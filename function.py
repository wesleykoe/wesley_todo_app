FILEPATH = "todos.txt"


def get_todos(filepath="todos.txt"):
    """ Reads a text file and returns a list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Writes the to-do item list into the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)





