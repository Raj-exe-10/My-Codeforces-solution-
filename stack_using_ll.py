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
            self.top = self.top.next

s=stack()
print(s.is_empty())
s.push(1)
print(s.is_empty())
s.push(2)
s.push(3)
s.push(4)
s.traverse()
print('-------')
s.pop()
s.traverse()