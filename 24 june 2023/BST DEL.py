'''
LOGIC:
1.Using "insert" create BST
2.Input node to be deleted
3.Spot or find the node which u want to delete(search)
4.once u find the node,check it comes under which category of delete
5.apply the delete concept
6.find inorder successor using seperate function to replace with node to be deleted

'''

class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
#Given a non-empty binary
#search tree,return the node
#with min key value
#found in that tree.Note that the #entire tree does not need to be searched
def minValueNode(node):
    current=node
    #loop down to find the leftmost leaf
    while(cutrrent.left is not None):
        current=current.left
    return current
'''Given a binary search tree and  a key this function delete the
key and treturns the new root'''
def DeleteNode(root,key):
    if root is None:
        return root
    #key<root,it lies in left subtree
    if key<root.key:
        root.left=DeleteNode(root.left,key)
    elif(key>root.key):
        root.right=DeleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            temp=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        '''Node with 2 children
            get the inorder successor
            smallest in the right subtree'''
        temp=minValueNode(root.right)
        root.key=temp.key
        root.right=DeleteNode(root.right,temp.key)
    return root
'''
                    50
                  /   \
                 30   70
                /  \ /  \
              20  40 60 80'''
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print("Inorder:")
inorder(root)
print("\nDelete 20")
root=DeleteNode(root,20)
print("Inorder:Modified tree")
inorder(root)
print("\nDelete 30")
root=DeleteNode(root,30)
print("Inorder:Modified tree")
inorder(root)
print("\nDelete 50")
root=DeleteNode(root,50)
print("Inorder:Modified tree")
inorder(root)
