class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('To-Do List:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.completed_tasks.append(self.tasks[task_index])
            completed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{completed_task}" marked as completed.')
            ch = int(input("Enter 1 to view the completed tasks else 0:"))
            if ch==1:
                print("Completed_task")
                for index, task in enumerate(self.completed_tasks, start=1):
                    print(f'{index}. {task}')
        else:
            print('Invalid task index.')

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{removed_task}" removed from the to-do list.')
        else:
            print('Invalid task index.')


def main():
    todo_list = ToDoList()
    print("                  To Do List Application")
    while True:
        print('\nOptions:')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Complete Task')
        print('4. Remove Task')
        print('5. Exit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input('Enter the task number to mark as completed: '))
            todo_list.complete_task(task_index)
        elif choice == '4':
            task_index = int(input('Enter the task number to remove: '))
            todo_list.remove_task(task_index)
        elif choice == '5':
            print('Exiting the To-Do List application.Thank You!!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')



if __name__ == "__main__":
    main()
