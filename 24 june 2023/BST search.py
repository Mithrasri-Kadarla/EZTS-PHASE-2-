class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key: 
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
#Inorder Traverse
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
def search(root ,key):
    if root is None or root.val==key:
        return root
    if root.val<key:
        return search(root.right,key)
    return search(root.left,key)
r = None
while True:
    value = input("Enter a value to insert (or 'done' to finish): ")
    if value == "done":
        break
    try:
        value = int(value)
        r = insert(r, value)
    except ValueError:
        print("Invalid input. Please enter an integer or 'done'.")
print("Inorder traversal:")
inorder(r)
x=int(input("Enter the element to search:"))
if search(r, x):
    print("Element is present")
else:
    print("Not present")

