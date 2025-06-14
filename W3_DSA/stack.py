'''
         start           end
stack --> | 1 | 2 | 3 | 4 |    <--- | 5 | now adding five which is the lastly added

stacks is a Last In First Out ( LIFO )

stack as functions like 
1. pop -> to remove the last element
2. push  -> to add the element at the last
3. peek -> to check which element is now on the top
4. isEmpty  -> to check wehter the stack is empty or not (bool type)
5. size -> to return the no of element in the stack
'''

'''
stack class 
'''
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0 
    
    def size(self):
        return len(self.stack)
    
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())