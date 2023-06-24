stack=[]
def push():
    ele=int(input("Enter the element to push:"))
    stack.append(ele)
    print(stack)
def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed element:",e)
        print(stack)
def Top():
    if len(stack)==0:
        print("Empty ,No element to delete")
    else:
        print(stack[len(stack)-1])
        print(stack.pop(len(stack)-1))
print("Select Options: 1.push 2.pop 3.display() 4.Top 5.display()")
while True:
    ch=int(input("Enter the choice:"))
    if ch==1:
        push()
    elif ch==2:
        pop_element()
    elif ch==3:
        print(stack)
    elif ch==4:
        Top()
    elif ch==5:
        break
    else:
        print("Enter correct choice")
