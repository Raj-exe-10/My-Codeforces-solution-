class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top==None

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def traverse(self):
        temp = self.top
        while(temp!=None):
            print(temp.data)
            temp= temp.next

    def peek(self):
        return self.top.data

    def pop(self):
        if self.top == None:
            return 'Not Possible'
        else:
            t = self.top.data
            self.top = self.top.next
            return t

s=stack()
a=input('Enter your String: ')
for i in a:
    s.push(i)
str1=''
while(not s.is_empty()):
    str1 += str(s.pop())
print(str1)