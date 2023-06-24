q=[]
def enq():
    ele=input("Enter Element")
    q.append(ele)
    print(ele,"is added in q")
    print(q)
def dq():
    if not q:
        print("Q is Empty")
    else:
        e=q.pop(0)
        print("Removed element:",e)
        print(q)
def display():
    print(q)
print("Select any One option 1. Enqueue 2.dequeue 3.Display 4.Quit")
while True:
    ch=int(input("Enter the Choice:"))
    if ch==1:
        enq()
    elif ch==2:
        dq()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("Enter Correct option")
