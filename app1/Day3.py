todos=[]

while True:
    user =input("Type add, show or exit: ")
    user = user.strip()
    """This method is often used to clean up user input or manipulate strings in a way that removes unnecessary whitespace. Additionally, there are variants of this method, such as .lstrip() (remove leading whitespace) and .rstrip() (remove trailing whitespace), if you only want to strip whitespace from one side of the string.
"""

    match user :
        case 'add':
            todos.append(input("Enter a todo:"))
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case whatever:
            print("Not from given options")
print("bye!")