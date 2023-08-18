class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.n = 0

    def insert_head(self,val):
        new_node = node(val)
        if self.head is None:
            self.head = new_node
            self.n += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.n += 1

    def insert_tail(self,val):
        new_node = node(val)
        if self.head is None:
            self.head = new_node
            self.n += 1
        else:
            temp = self.head
            while temp.next != None:
                temp =temp.next
            temp.next = new_node
            self.n += 1

    def insert_at_index(self,val,index):
        if index>self.n:
            return 'Not possible'
        if index==0:
            l.insert_head(val)
            self.n += 1
        elif index == self.n:
            l.insert_tail(val)
            self.n += 1
        else:
            new_node = node(val)
            temp = self.head
            for i in range (index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.n+=1

    def __str__(self):
        if self.head is None:
            return []
        else:
            str1 = ''
            temp = self.head
            while temp != None:
                str1 = str1 + str(temp.val) + '->'
                temp = temp.next
            return str1[:-2]

    def clear(self):
        self.head == None
        self.n =0

    def delete_head(self):
        if self.head == None:
            return "Empty Linked List"
        self.head = self.head.next
        self.n -= 1

    def delete_tail(self):
        if self.head == None:
            return "Empty Linked List"
        if self.head.next ==None:
            self.delete_head()
            return
        temp = self.head
        while (temp.next.next !=None):
            temp = temp.next
        temp.next = None
        self.n -= 1

    def delete_by_val(self,val1):
        if self.head == None:
            return "Empty Linked List"
        if self.head.val==val1:
            self.delete_head()
            return
        temp = self.head
        while (temp.next!= None):
            if temp.next.val==val1:
                break
            temp = temp.next
        if temp.next == None:
            return "No value Found"
        else:
            temp.next = temp.next.next

l = linkedlist()
l.insert_head(1)
l.insert_tail(3)
l.insert_head(0)
l.insert_at_index(2,2)
print(l)
l.delete_by_val(2)
print(l)
l.delete_head()
print(l)
l.delete_tail()
print(l)