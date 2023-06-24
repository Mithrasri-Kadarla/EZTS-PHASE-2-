#Creating node declaration and defination
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(slef):
        slef.head=None
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                 if temp.next!=None:
                    print(temp.data,end=" -> ")
                 else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                 temp=temp.next
                #print(temp.data,"->",end=" ")
                #temp.data means first node's data
                #temp=temp.next#establishing link
    def delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
obj=singlelinkedlist()
#Node creation-initialising
n=Node(10)# so n.data in Node class will be 10
obj.head=n#assigning first node as head
n1=Node(20)
obj.head.next=n1#next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
print("Before deletion:\n")
obj.display()
print("\n")
'''print("After deleting at beginning:")
obj.delete_beg()
obj.display()
print("\n")
print("After deleting at end:")
obj.delete_end()
obj.display()
print("\n")
print("After deleting at position 2:")
obj.delete_position(2)
obj.display()'''
print("1.Delete at end:")
print("2.delete at begining:")
print('3.Delete at position:')
ch=int(input("Enter ur choice:"))
if ch==1:
    print("After deleting at end:")
    obj.delete_end()
    obj.display()
elif ch==2:
    print("After deleting at beginning:")
    obj.delete_beg()
    obj.display()
elif ch==3:
    x=int(input())
    obj.delete_position(x)
    obj.display()
