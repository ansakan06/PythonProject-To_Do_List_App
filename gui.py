import FreeSimpleGUI as sg
import functions
import time
import os


file_path = "C:\\Users\\ansak\\PycharmProjects\\PythonProject\\user_interface.py"
print(f"Path: {file_path}")
print(f"Exists: {os.path.exists(file_path)}")


# List files in the directory
directory = "C:\\Users\\ansak\\PycharmProjects\\PythonProject"
print(f"Directory contents: {os.listdir(directory)}")


if not os.path.exists("toDosList.txt"):
   with open("toDosList.txt","w") as file:
       pass


sg.theme("LightBrown5")
# Define GUI layout
clock= sg.Text('', key='clock')
label = sg.Text("Type in a To-Do:")
label1= sg.Text("To Edit, click on the To-Do you wish to edit, "
               "and then type your edit, and press Edit button!")
input_box = sg.InputText(tooltip="Enter a To-Do", key='To-Do')
add_button = sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(), key='To-Dos',
                   enable_events=True,size=[45,10])
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button= sg.Button("Exit")


# Create a window
window = sg.Window("My To-Do List APP",
                   layout=[[clock],
                       [label],
                       [label1],
                       [input_box, add_button],
                       [list_box,edit_button, complete_button],
                       [exit_button]],
                   font=("Helvetica", 15))


while True:
   event, values = window.read(timeout=300)
   window['clock'].update(value=time.strftime("%b %d,%Y %H:%M%S"))


   match event:
       case "Add" :
       # Fetch and append to the to-do list
           toDosList = functions.get_todos()
           new_toDosList = values['To-Do'] + "\n"
           toDosList.append(new_toDosList)
           functions.write_todos(toDosList)
           window['To-Dos'].update(values=toDosList)
       case "Edit":
           try:
               toDosList_to_edit = values['To-Dos'][0]
               new_toDosList=values['To-Do']


               toDosList=functions.get_todos()
               index=toDosList.index(toDosList_to_edit)
               toDosList[index]=new_toDosList
               functions.write_todos(toDosList)
               window['To-Dos'].update(values=toDosList)
           except IndexError:
               sg.popup("Please select an item first!", font=("Helvetica", 20))


       case "Complete":
           try:
               toDosList_to_complete=values['To-Dos'][0]
               toDosList=functions.get_todos()
               toDosList.remove(toDosList_to_complete)
               functions.write_todos(toDosList)
               window['To-Dos'].update(values=toDosList)
               window['To-Do'].update(value='')
           except IndexError:
               sg.popup("Please select an item first!", font=("Helvetica", 20))


       case "Exit":
           break
       case 'To-Dos':
           window['To-Do'].update(value=values['To-Dos'][0])
       case sg.WIN_CLOSED:
           break
window.close()
