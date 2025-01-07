from functions import get_todos,write_todos
import time
now= time.strftime("%b %d, %Y %H:%M:%S")




print("It is", now)
print("Your To DO List:")




while True:
  user_action=input("Type add, show, edit, complete or exit: ")
  user_action=user_action.strip()
  if user_action.startswith("add"):




#list splicing [x:] basically shows everything past x, letter
      new_task = user_action[4:]




      toDosList= get_todos()




      toDosList.append(new_task +'\n')




      write_todos(toDosList, "toDosList.txt")




  elif user_action.startswith("show"):
      toDosList=get_todos(filepath="toDosList.txt")




      for index,item in enumerate(toDosList):
          item=item.strip('\n')
          row= f"{index+1}:{item}"
          print(row)




  elif user_action.startswith("edit"):
      try:
          number = int(user_action[5:])
          print(number)




          number=number-1




          toDosList = get_todos()




          new_toDosList=input("Enter new To Do:")
          toDosList[number]=new_toDosList + '\n'




          write_todos(toDosList, "toDosList.txt")




      except ValueError:
          print("Your command is not valid. Type the number of the To Do you would like to edit")
          continue








  elif user_action.startswith("complete"):
      try:
          number=int(user_action[9:])




          toDosList = get_todos()




          index=number-1
          toDoList_to_remove=toDosList[index].strip('\n')
          toDosList.pop(index)




          write_todos(toDosList, "toDosList.txt")




          message= f"To do {toDoList_to_remove} was removed from the list"
          print(message)
      except IndexError:
          print("There is no item with that number.")




  elif user_action.startswith("exit"):
      break




  else:
      print("Command is invalid, please try again!")




print("Good Luck with Your Tasks!")
