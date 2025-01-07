FILEPATH= "toDosList.txt"




def get_todos(filepath=FILEPATH):
  """ Read a text file and return the
  list of to-do items.
  """
  with open(filepath, 'r') as file_local:
      todos_list_local = file_local.readlines()
  return todos_list_local








""" Write the to-do item list in the text file"""
def write_todos(todos_list_arg, filepath=FILEPATH):
  with open(filepath, 'w') as file:
      file.writelines(todos_list_arg)
