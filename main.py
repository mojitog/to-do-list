import csv
class Task:
    def __init__(self, name, definition, prio):
        self.name = name
        self.definition = definition
        self.prio = prio
    def __str__(self):
        s = f"Task: {self.name}\nDefinition: {self.definition}\nPriority: {self.prio}\n"
        return s
    def __repr__(self):
        return str(self)   


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
    def save(self):
        with open('to_do_list.csv', 'w', newline='') as csv_file:
            fieldnames = ['task', 'definition', 'priority']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for task in self.task_list:
                writer.writerow({'task': task.name, 'definition': task.definition,
                                 'priority': task.prio})
    def load(self, csv_addr):
        with open(csv_addr, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.task_list.append(Task(row['task'], row['definition'], row['priority']))


# define tasks
t1 = Task("Dinner", "Cooking proper meal for dinner, then just eat it", "high")
t2 = Task("Chess Club", "Attend the chess club and have fun", "medium")

# create lists out of tasks
task_list = [t1, t2]
task_list_test = []

# create to-do-list out of task lists
mylist = To_do_list(task_list)
mylist_test = To_do_list(task_list_test)

# test to-do-list functions
mylist_test.load('test.csv')
mylist_test.show_task()
mylist.save()
