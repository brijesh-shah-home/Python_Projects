# Question: Todo List Application
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' Added.") 

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' Removed.")
        else:
            print("Task Not Found..!")

    def view_tasks(self):
        if not self.tasks:
             print("Your Todo List is empty.")
        else:
           print("---- Your Todo List ----")
           for idx,task in enumerate(self.tasks,start=1):
               print(f"'{idx}' Task : '{task}'")

todo=TodoList()
todo.view_tasks()
todo.add_task("Buy Fruits")
todo.add_task("Complete Homework")
todo.add_task("Call Darpan")
todo.view_tasks()
todo.remove_task("Play Ludo")
todo.view_tasks()
