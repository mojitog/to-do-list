class Task:
    def __init__(self, name, definition, prio):
        self.name = name
        self.definition = definition
        self.prio = prio
    def __str__(self):
        s = f"{self.name} | {self.definition} | {self.prio}"
        return s   


class To_do_list:
    """
    The basic to_do_list class that needs to get more efficient and functional
    """
    def __init__(self, task_list):
        self.task_list = task_list
    def add_task(self, task):
        self.task_list.append(task)
    def rmv_task(self, task):
        self.task_list.remove(task)
    def show_task(self):
        print(self.task_list)    


t1 = Task("Dinner", "Cooking proper meal for dinner, then just eat it", "high")
t2 = Task("Chess Club", "Attend the chess club and have fun", "medium")
print(t1)
task_list = [t1, t2]
print(task_list)
#print(task_list)

mylist = To_do_list(task_list)

mylist.show_task()
