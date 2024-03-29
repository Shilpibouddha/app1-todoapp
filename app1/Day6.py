"""

# Because when we were closing the app,data was getting lost , so we need to store it
while True:
    user =input("Type add, show ,edit,complete or exit: ")
    user = user.strip()
    #This method is often used to clean up user input or manipulate strings in a way that removes unnecessary whitespace. Additionally, there are variants of this method, such as .lstrip() (remove leading whitespace) and .rstrip() (remove trailing whitespace), if you only want to strip whitespace from one side of the string.


    match user :
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file= open('files/todos.txt', 'r')
            todos=file.readlines()
            file.close()

            todos.append(todo)

            file=open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()


        case 'show':
            file=open('files/todos.txt', 'r')
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
contents= ["All carrots are ", "the carrots are sliced","The slicing process is done"]
filenames = ["doc.txt", "report.txt", "presentation.txt"]


for content, filename in zip(contents,filenames):
    file = open(f"/Users/shilpibouddha/PycharmProjects/Endgame_python/files/{filename}" , "w")
    file.write(content)


