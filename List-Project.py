tasks=[]
h
def add_task():
  task=input("What task do you want to add? ")
  tasks.append(task)
  print(f"{task} has been added to your list")

def show_task():
  if tasks:
    count=1
    for i in tasks:
      print(count,i)
      count=count+1
  else:
    print("No tasks are added")

def remove_task():
  show_task()
  remove1=int(input("Enter the task number you want to remove: "))
  if remove1 in range(1,len(tasks)+1):
    a=tasks.pop(remove1-1)
    print(f"{a} was removed succesfuly")
  else:
    print("Enter a valid number")



def mark_task_complete():
  show_task()
  complete=int(input("Enter the task number you completed: "))
  if complete in range(1,len(tasks)+1):
     tasks[complete-1]=tasks[complete-1]+" ✔"
  else:
     print("Enter a valid number")

def choice():
  print("Choose 1 for add_task")
  print()
  print("Choose 2 for show_task")
  print()
  print("Choose 3 for remove_task")
  print()
  print("Choose 4 for mark_task_complete")
  print()
  print("Choose 5 for exit")
  print()

choice()
while True:

  i = int(input("Enter your choice: "))
  if i == 1:
    add_task()
    print("--------")

  elif i == 2:

   show_task()
   print("--------")

  elif i == 3:

   remove_task()
   print("--------")

  elif i == 4:

    mark_task_complete()
    print("--------")

  elif i == 5:
    print("Bye!")
    break
  else:
    print("Enter a valid choice from 1-5")



