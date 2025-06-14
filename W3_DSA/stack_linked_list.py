'''
here we have a stack that implemented with linked list

using stack for every node and the data at the top for easy changes
each node's next points the next node's data like the linked list 

head --> | data |  / | data |  / | data |  / | data |
         | next | /  | next | /  | next | /  | next | --> Null
         
here we going to create a stack the using nodes and manipulated like the linked list
'''

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pop(self, value):
        pass
                