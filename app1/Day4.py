"""
todos=[]

while True:
    user =input("Type add, show ,edit or exit: ")
    user = user.strip()
   # This method is often used to clean up user input or manipulate strings in a way that removes unnecessary whitespace. Additionally, there are variants of this method, such as .lstrip() (remove leading whitespace) and .rstrip() (remove trailing whitespace), if you only want to strip whitespace from one side of the string.


    match user :
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number=int(input("Number of todo to edit: "))
            number=number-1
            new_todo= input("Enter new todo: ")
            todos[number]= new_todo

        case 'exit':
            break
        case whatever:
            print("Not from given options")
print("bye!")



"""
filenames= ["1.Raw data.txt" ,"2.Reports.txt", "3.presentation.txt"]

for files in filenames:
    files= files.replace('.','-',1)
    print(files)