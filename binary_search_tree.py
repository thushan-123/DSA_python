class BST():
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode,data):
    if rootNode.data is None:
        rootNode.data = BST(data)
    elif data <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BST(data)
        else:
            insertNode(rootNode.leftChild,data)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BST(data)
        else:
            insertNode(rootNode.rightChild,data)
            
    return "Data inserted"

# root -> left -> right
def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data, end=' ')
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
# left -> root -> right
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=' ')
    inOrderTraversal(rootNode.rightChild)
    
# left -> right -> root
def postOrderTravesl(rootNode):
    if not rootNode:
        return
    postOrderTravesl(rootNode.leftChild)
    postOrderTravesl(rootNode.rightChild)
    print(rootNode.data, end=' ')
    
    
def searchNode(rootNode,value):
    if rootNode is None:
        return False
    
    if rootNode.data == value:
        return True
    elif rootNode.data > value:
        return searchNode(rootNode.leftChild,value)
    else:
        return searchNode(rootNode.rightChild,value)
    
# find the right sub tree min value
def minNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current
        
        
def deleteNode(rootNode, value):
    if rootNode is None:
        return None
    if rootNode.data > value:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif rootNode.data < value:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else:
        # Case: Node with only one child or no child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None  # Delete the current node
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None  # Delete the current node
            return temp

        # Case: Node with two children
        temp = minNode(rootNode.rightChild)
        rootNode.data = temp.data  # Copy the inorder successor's value to this node
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)  # Delete the inorder successor

    return rootNode
   
        
    
    
        
            
bst = BST(10)
insertNode(bst,20)
insertNode(bst,40)
insertNode(bst,3)
insertNode(bst,56)
insertNode(bst,12)
insertNode(bst,4)
insertNode(bst,6)

print("PreOrder Traversal :" , end='')
preOrderTraversal(bst)
print("\n")
print("InOrder Traversal :" , end='')
inOrderTraversal(bst)
print("\n")
print("PostOrder Traversal :" , end='')
postOrderTravesl(bst)
print("\nSearch item in tree :",searchNode(bst,4))

deleteNode(bst,3)

preOrderTraversal(bst)
