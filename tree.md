# The Binary Tree Data Structure
The `Binary Tree` Data Structure can be used to store sorted data within a list.

For example, You have a data set that is disorganized from your quick note taking skills from a test you completed some time ago. You now want to create an organized method to make your data interpretable but you don't want duplicate data entered. An example of this in code would be:
```python
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
            if node.left is None: #if the left node is empty, insert the data
                node.left = BST.Node(data) #create a new node
            else: #if the left node is not empty, go left
                self._insert(data, node.left) #go left
        else:
            if node.right is None: #if the right node is empty, insert the data
                node.right = BST.Node(data) #create a new node
            else: #if the right node is not empty, go right
                self._insert(data, node.right) #go right
```

The code above does not take into account the fact that there may be duplicate entries nor does it allow for the BST to be printed. The following code will allow for the BST to be iterated through and printed out to get the relevant data:
```python
def __iter__(self): #iterate through the tree
        yield from self._print_ordered(self.root)  # Start at the root
    
    def _print_ordered(self, node): #iterate through the tree
        if node is not None: #if the node is not empty
            yield from self._print_ordered(node.left) #go left
            yield node.data #print the node data
            yield from self._print_ordered(node.right) #go right
```

# Your Task
Your task is to make sure that if there are any duplicates in the tree, they are ignored and the program will let the user know as such so the data can be organized efficiently

[Tree Task](https://github.com/NicholasBoss/DataStructureTutorial/blob/master/treetask.py)

[Tree Solution](https://github.com/NicholasBoss/DataStructureTutorial/blob/master/treesolution.py)

# Back to Home

[Return to Home](https://github.com/NicholasBoss/DataStructureTutorial/blob/master/0-welcome.md)
