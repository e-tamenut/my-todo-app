# use help(name_of_function) in the Python console to learn and also write PyDocs for their use, (memory practice)

# Pythons version of Java's STATIC
FILEPATH = "../../PycharmProjects/todo_app/todos.txt"

# custom function to replace repetitive code
# takes an argument
def get_todos(filepath=FILEPATH): # new skill, default parameter for copies of same param
    """ Read a text file and return the list of
    to-do items.
    """

    ### with context manager: new skill unlocked. Optimized version of commented code above
    with open(filepath, "r") as file_local:
        todos = file_local.readlines()
    return todos

def write_todos(todos_arg, filepath=FILEPATH): # non-default parameters cannot follow defaults
    """ Write the to-do items list in the text file."""
    # with context manager with writing command
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())