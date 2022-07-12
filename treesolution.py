class BST:

    class Node:

        def __init__(self, data): #initialize the node
            self.data = data
            self.left = None
            self.right = None

    def __init__(self): #initialize the tree
        self.root = None

    def insert(self, data): #insert a node into the tree
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  

    def _insert(self, data, node): #insert a node into the tree
        if data < node.data: #if the data is less than the node data, go left
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data: #if the data is greater than the node data, go right
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right) 
        else: #if the data is equal to the node data, do nothing
            print("Value already in tree!")
            pass

    def __iter__(self): #iterate through the tree
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node): #iterate through the tree

        if node is not None: #if the node is not empty
            yield from self._traverse_forward(node.left) #go left
            yield node.data #print the node data
            yield from self._traverse_forward(node.right) #go right

#test case 1
print("Test case 1:")
print("------------")
tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(7)
tree.insert(17)
tree.insert(2)
tree.insert(2)
tree.insert(12)
for x in tree:
    print(x)