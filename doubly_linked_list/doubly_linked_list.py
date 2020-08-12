"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    #def delete(self):
        #if self.prev:
            #self.prev.next = self.next
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length


    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value, next=self.head)
        if self.head is None and self.tail is None:
            # set head and tail to the new node 
            self.head = new_node
            self.tail = new_node
            
        # otherwise, the list has at least one node 
        else:
            # update the last node's `next_node` to the new node 
            self.head.prev = new_node
            # update `self.tail` to point the new node we just added 
            self.head = new_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1
        # wrap the value in a Node
        new_node = ListNode(value, prev=self.tail)
        # check if the Linked List is empty 
        if self.head is None and self.tail is None:
            # set head and tail to the new node 
            self.head = new_node
            self.tail = new_node
        # otherwise, the list has at least one node 
        else:
            # update the last node's `next_node` to the new node 
            self.tail.next = new_node
            # update `self.tail` to point the new node we just added 
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # check if the linked list is empty 
        if self.head is None and self.tail is None:
            return None
        
        # check if the linked list has only one node 
        if self.head == self.tail:
            # store the node we're going to remove's value 
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        # otherwise, the linked list has more than one Node 
        else:
            # store the last Node's value in a nother variable so we can return it 
            val = self.tail.get_value()
            # we need to set `self.tail` to the second-to-last Node
            # the only way we can do this, is by traversing the whole linked list
            # from the beginning 
            
            # starting from the head, we'll traverse down to the second-to-last Node 
            # init another reference to keep track of where we are in the linked 
            # list as we're iterating 
            current = self.head 

            # keep iterating until the node after `current` is the tail
            while current.get_next() != self.tail:
                # keep iterating 
                current = current.get_next()

            # set `self.tail` to `current`
            self.tail = current
            # set the new tail's `next_node` to None
            self.tail.set_next(None) 
            return val

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is None:
            return
        if node.prev is None and node.next is None:
            self.head = None
            self.tail = None
            return
        #check if the node is the head
        if node.prev is None:
            self.head = node.next
            self.head.prev = None
            return
        #check if the node is the tail
        if node.next is None:
            self.tail = node.prev
            self.tail.next = None
            return
    
        node.prev.next = node.prev
        node.next.prev = node.prev
            
            
       
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        #if list is empty, return None
        if self.head is None and self.tail is None:
            return
        #keep track of the largest value we've seen so far
        max_value =  self.head.value
        #traverse the entirety of the linked list
        current = self.head.next

        while current is not None:
            #if we see a value > the largest value we've seen so far
            if current.value > max_value:
            #update the largest value
                max_value = current.value
            #update current to point to the next node
                current = current.next 
        #return the largest value
        
        #return max_value