from node import Node

class Linked_Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
           
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.set_next(self.head)
            self.head = newNode
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_data = self.head.get_data()
            next_node = self.head.get_next()
            self.head = next_node
            return popped_data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.get_data()
