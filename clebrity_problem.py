class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
        self.n =0

    def is_empty(self):
        return self.top==None

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.n+=1

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
            self.n-=1
            return t

    def size(self):
        return self.n
l1 = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]

def find_celeb(l):
    s=stack()
    for i in range(len(l)):
        s.push(i)

    while (s.size()>=2):
        i=s.pop()
        j=s.pop()

        if l[i][j] == 0:
            s.push(i)
        else:
            s.push(j)

    celeb = s.pop()

    for i in range (len(l)):
        if i!=celeb:
            if l[i][celeb] ==0 or l[celeb][i]==1:
                return 'There is no celebrity'
    return f'The celebrity is :{celeb}'

print(find_celeb(l1))