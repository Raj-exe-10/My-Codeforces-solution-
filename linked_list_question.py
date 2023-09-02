'''
Given a linked list of characters . write a python program to return a new string that is created by appending all 
characters given in a linked list as per the rule given below:
1-Replace '*' or '/' by a single space.
2-In case of two consecutive occurence of '*'or '/',replaec these two occurence with a asingle space and convert trhe next character to uppercase.
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self,val):
        new_node = Node(val)
        if self.head==None:
            self.head = new_node
            self.count+=1
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next = new_node
            self.count+=1

    def __str__(self):
        str1=''
        temp = self.head
        while(temp!=None):
            if temp.data == "*" or temp.data=="/":
                if temp.next.data=="*" or temp.next.data=="/":
                    temp.next.next.data = temp.next.next.data.upper()
                else:
                    str1 += " "
            else:
                str1 += str(temp.data)
            temp=temp.next
        return str1

l=linkedlist()
l.insert('A')
l.insert('n')
l.insert('*')
l.insert('/')
l.insert('a')
l.insert('p')
l.insert('p')
l.insert('l')
l.insert('e')
l.insert('*')
l.insert('a')
l.insert('/')
l.insert('d')
l.insert('a')
l.insert('y')
l.insert('*')
l.insert('*')
l.insert('k')
l.insert('e')
l.insert('e')
l.insert('p')
l.insert('s')
l.insert('/')
l.insert('*')
l.insert('a')
l.insert('/')
l.insert('/')
l.insert('d')
l.insert('o')
l.insert('c')
l.insert('t')
l.insert('o')
l.insert('r')
l.insert('*')
l.insert('A')
l.insert('w')
l.insert('a')
l.insert('y')
print(l)