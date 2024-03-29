"""
while True:
    user =input("Type add, show ,edit,complete or exit: ")
    user = user.strip()
    #This method is often used to clean up user input or manipulate strings in a way that removes unnecessary whitespace. Additionally, there are variants of this method, such as .lstrip() (remove leading whitespace) and .rstrip() (remove trailing whitespace), if you only want to strip whitespace from one side of the string.


    match user :
        case 'add':
            todo = input("Enter a todo: ") + "\n"


            with  open('files/todos.txt', 'r') as file:
                todos = file.readlines()#when we use with , we don't have to close in read or write files

            todos.append(todo)

            file=open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()


        case 'show':
            file=open('files/todos.txt', 'r')#by default if no w, r ,it is read only
            todos=file.readlines()
            file.close()

            for index,items in enumerate(todos):
                row=f"{index+1}-{items}"
                print(row)
        case 'edit':
            number=int(input("Number of todo to edit: "))
            number=number-1
            new_todo= input("Enter new todo: ")
            todos[number]= new_todo

        case 'complete':
            number=int(input("Number of todo to complete: "))
            todos.pop(number-1)

        case 'exit':
            break
        case whatever:
            print("Not from given options")
print("bye!")
"""

date=input("Enter today's date: ")
mood=input("rate your mood from 1 to 10: ")
thoughts= input("Let your thoughts flow :\n")

with open(f"../journal/{date}.txt" ,"w") as file:
    file.write(mood + 2*"\n")
    file.write(thoughts)
