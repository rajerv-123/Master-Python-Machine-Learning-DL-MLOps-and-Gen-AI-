import os

# file to store tasks
FILE_NAME = "tasks.txt"

# load tasks from file
def load_tasks():
    tasks= {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split("  | ")
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks            


# ?savetasks to file
def  save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id}  | {task['title']}  | {task['status']}\n")
            

# addnew task

def add_task(tasks, title):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1 
    tasks[task_id] = {"title": title, "status": "pending"}
    print(f"Task '{title}' added with ID {task_id}.")
    
    
# view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("ID  | Title  | Status")
    print("-----------------------")
    for task_id, task in tasks.items():
        print(f"{task_id}  | {task['title']}  | {task['status']}")
        
        
        
        
# mark task as completed
def mark_task_completed(tasks):
    task_id = int(input("Enter task ID to mark as completed: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "completed"
        print(f"Task ID {task_id} marked as completed.")
    else:
        print(f"Task ID {task_id} not found.")
        
#delete task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task ID {task_id} deleted.")
    else:
        print(f"Task ID {task_id} not found.")
        
        
# main menu
def main():
    tasks = load_tasks()
    try:
        while True:
            print("\n1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                title = input("Enter task title: ")
                add_task(tasks, title)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                mark_task_completed(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                save_tasks(tasks)
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        save_tasks(tasks)
        print("\nInterrupted. Tasks saved. Goodbye!")
            
if __name__ == "__main__":
    main()