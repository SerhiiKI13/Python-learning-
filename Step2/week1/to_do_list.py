def main():
     list_task = []
     while True:
         num = int(input(
    """
    1.Add task
    2.Show tasks
    3.Complete task
    4.Delete task
    5.Exit
    """
         ))
         if num == 1:
             task = input("Enter the task: ")
             add_task(list_task,task,status=False)
         elif num == 2:
            show_task(list_task)
         elif num == 3:
             print(complete_task(list_task))
         elif num == 4:
             print(delete_task(list_task))
         else:
             print("End")
             break
         
def add_task(tasks,task,status=False):
    t = {"task": task ,"status": status}
    tasks.append(t)
    return tasks

def show_task(tasks):
    if tasks:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["status"] else "❌"
            print(f"{i}. {task['task']} - {status}")
        
    else: 
        print("Tasks not found")
    
def complete_task(tasks):
    num = int(input("Enter the task number for completed: "))
    index = num - 1
    tasks[index]['status'] = True 
    return " Задание завершено"

def delete_task(tasks):
    num = int(input("Entrr the task number for delete: "))
    index = num - 1
    tasks.remove(tasks[index])
    return "Task is deleted"
    
main()