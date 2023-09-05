class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n =0

    def enqueue(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.n+=1

        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head ==None:
            return 'empty'
        self.head = self.head.next

    def traverse(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.next
        print()
q= queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.traverse()

q.dequeue()

q.traverse()
