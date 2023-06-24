#create 2 LL and display whether they are same LL are not
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

def are_same_lists(llist1, llist2):
    curr_node1 = llist1.head
    curr_node2 = llist2.head

    while curr_node1 and curr_node2:
        if curr_node1.data != curr_node2.data:
            return False
        curr_node1 = curr_node1.next
        curr_node2 = curr_node2.next

    if curr_node1 is None and curr_node2 is None:
        return True
    else:
        return False

# Create the first linked list
llist1 = LinkedList()
n = int(input("Enter the number of elements for the first linked list: "))
for i in range(n):
    data = int(input("Enter the element: "))
    llist1.insert(data)

# Create the second linked list based on user input
llist2 = LinkedList()
n = int(input("Enter the number of elements for the second linked list: "))
for i in range(n):
    data = int(input("Enter the element: "))
    llist2.insert(data)

# Check if the linked lists are the same
if are_same_lists(llist1, llist2):
    print("The linked lists are the same.")
else:
    print("The linked lists are different.")
