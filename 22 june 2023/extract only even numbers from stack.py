o=[]
e=[]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                if temp.data % 2 == 0:
                    e.append(temp.data)
                else:
                    o.append(temp.data)
                temp = temp.next
            ch=int(input("Enter the choice 1(even) or 2(odd):"))
            if ch==1:
                print(e)
            elif ch==2:
                print(0)
            else:
                print("Enter correct choice!!!")
            '''print(o)
            print(e)'''
obj_stack = Stack()
n = int(input("Enter the number of elements: "))
for i in range(n):
    x = int(input("Enter a number: "))
    obj_stack.push(x)
obj_stack.display()
