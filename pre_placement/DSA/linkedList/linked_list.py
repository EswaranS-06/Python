class Node():
    def __init__(self,val):
        self.next=None
        self.val=val
class Linkedlist():
    def __init__(self):
        self.head = None
    
    def insert(self, val, index = None):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        
        # if index:
        #     c = 0
        #     curr = self.head
        #     while c <= index:
        #         new_node.next = curr
        #         curr = new_node
        
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node
        
        
    def display(self):
        tmp = self.head
        while tmp:
            print(tmp.val, end="->")
            tmp = tmp.next
        print("None")
            
    def beggining(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def len(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count
    
            
l = Linkedlist()
l.insert("One")
l.insert("Two")
l.insert("Three")
l.display()
l.beggining("Zero")
l.display()
print(l.len())
l.insert("One.five",1)
l.display()