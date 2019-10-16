class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.sub = key[2]
        self.empid = key[0]
        self.value = key[1]
# A utility function to insert a new node with the given key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.sub == node.empid: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
  
# A utility function to do inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.sub) 
        inorder(root.right) 
  
def size(root):
    if root is None:
        return 0
    else:
        llength = size(root.left)+1
        rlength = size(root.right)+1
        if llength > rlength:
            return llength
        elif llength == rlength:
            return llength
        else:
            return rlength
# Driver program to test the above functions 
# Let us create the following BST 
#      50 
#    /      \ 
#   30     70 
#   / \    / \ 
#  20 40  60 80 
r = Node([1,15,2]) 
insert(r,Node([2,10,4])) 
insert(r,Node([3,10,0])) 
insert(r,Node([4,5,0])) 
 
  
# Print inoder traversal of the BST 
inorder(r)
n=size(r)
print(n)
