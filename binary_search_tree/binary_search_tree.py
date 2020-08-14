"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #find value
       
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else: 
                self.left = BSTNode(value)
                
 
        else:
            if self.right is not None:
                self.right.insert(value)
            else: 
                self.right = BSTNode(value)


       

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)

        else:
            if self.right is not None:
                return self.right.contains(target)
        
        return False
        


    # Return the maximum value found in the tree
    def get_max(self):
        #the max value is always going to be the right-mosst ree node
        #Recursive version
        if not self.right:
            return self.value
        return self.right.get_max()
        

        #Iterative version

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Recursive 
        # call fn on self.value 
        fn(self.value)
        # # check if self has a left child 
        if self.left:
        #     # call `for_each` on the left child, passing in the fn 
             self.left.for_each(fn)
        # # check if self has a right child 
        if self.right:
        #     # call `for_each` on the right child, passing in the fn 
             self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        #depth first, from top to bottom
        #Last in First out

        if self.left:
            self.left.in_order_print()
        print(self.value)    
        if self.right:
            self.right.in_order_print()
        
        


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        #First in first out
        #levels
        nodes = []
        stack = [root]
        while stack:
            cur_node = stack[0]
            stack = stack[1:]
            nodes.append(cur_node)
        for child in cur_node.get_children():
            stack.append(child)
        return nodes

    # Print the value of every node, starting with the given node, 
    # in an iterative depth first traversal
    def dft_print(self):
         #depth first, from top to bottom
        #Last in First out
        # # Depth-First Iterative 
        # # how do we achieve the same ordering that recursion gave us for free? 
        # # use a stack to achieve the same ordering 
         stack = [] 
        # # add the root node to our stack 
         stack.append(self)
​
        # # continue popping from our stack so long as there are nodes in it 
         while len(stack) > 0:
             current_node = stack.pop()
​
        #     # check if this node has children 
             if current_node.right:
                 stack.append(current_node.right)
             if current_node.left:
                 stack.append(current_node.left)
            
             fn(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods

bst = BinarySearchTree(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
"""