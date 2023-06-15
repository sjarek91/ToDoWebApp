FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Return a list of todos from the txt file """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write todos to the txt file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == '__main__':
    print('Hello from the other side')
    print(get_todos())
