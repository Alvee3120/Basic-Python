tasks =[]

def show_menu():
    print("===== To Do List App ======")
    print("1. View Tasks ")
    print("2. Add Tasks")
    print("3. Remove Tasks")
    print("4. Exit")

def view_task():
    if not tasks:
        print("No Task Added")
    else:
        print("Your Task: ")
        for i in range(len(tasks)):
            print(tasks[i])
        

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task Added Successfully")


def remove_task():
    view_task()
    try:
        task_no = int(input("Enter a task num you want to remove"))
        removed = tasks.pop(task_no - 1 )
        print(f"Task '{removed}' removed successfully")
    except(IndexError, ValueError):
        print("Invalid Task Number")



def main():
    while True:
        show_menu()
        choice = input("\n Choose an option from 1 to 4")

        if choice == '1':
            view_task()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Tata")
            break
        else:
            print("Invalid Choice! Please try again!")


if __name__ == "__main__":
    main()