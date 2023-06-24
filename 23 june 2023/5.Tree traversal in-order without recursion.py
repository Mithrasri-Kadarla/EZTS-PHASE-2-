class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    #set current to root of binary tree
    current=root
    stack=[]#initialize  stack
    done=0
    while True:
            #Reach the left most Node of the current
        if current is not None:
            stack.append(current)
        #Place pointer to a tree node on the stack
        #before traversing the node's left subtree
            current=current.left
#BackTrack from empty sub tree & visit Node
#at the top of the stack
#However ,if the stack is empty you are done
        elif(stack):
            current=stack.pop()
            print(current.data,end=' ')
#we have visited the node and its left
            current=current.right
        else:
            break
print()
root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)
inorder(root)

            
                
