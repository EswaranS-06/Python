class Node():
    def __init__(s,data):
        s.next=None
        s.data=data
class Linkedlist():
    def __init__(s):
        s.head=None
        
    def insert(s,data):
        newnode=Node(data)
        if not s.head:
            s.head = newnode
        else:
            temp=s.head
            while temp.next:
                temp = temp.next
            temp.next=newnode
            
    def display(s):
        temp = s.head
        print('head',end='->')
        while(temp):
            print(temp.data,end='->')
            temp=temp.next
        print('None')

l=Linkedlist()
l.insert(100)
l.insert(200)
l.insert(300)
l.insert(400)
l.insert(500)
l.insert(600)
l.display()