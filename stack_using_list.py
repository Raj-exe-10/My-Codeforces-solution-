class Stack:

    def __init__(self,size):
        self.size = size
        self.stack = [None]*self.size
        self.top = -1

    def push(self,val):
        if self.top == self.size-1:
            return 'Overflow'
        else:
            self.top +=1
            self.stack[self.top]=val

    def pop(self):
        if self.top ==-1:
            return 'Underflow'
        data = self.stack[self.top]
        self.top-=1
        print(data)

    def traverse(self):
        for i in range (self.top+1):
            print(self.stack[i],end=' ')


s= Stack(3)
s.push(1)
s.push(2)
s.push(3)
s.traverse()
s.pop()
s.traverse()