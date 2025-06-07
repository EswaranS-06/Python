class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        self.st1.append(x)
        
    def pop(self):
        self.st2 = self.st1.reverse()
        self.st1 = []
        return self.st2.pop()

    def peek(self):
        if(not self.st2):
            while(self.st2):
                self.st2.append(self.st1.pop())
        return self.st2[-1]

    def empty(self):
        return [] is self.st2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()