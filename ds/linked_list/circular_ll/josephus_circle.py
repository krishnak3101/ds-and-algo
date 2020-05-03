class node():
    def __init__(self,data):
        self.data = data
        self.next = None



class circular_ll():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,data):
        if self.head is None:
            self.head = node(data)
            self.head.next = self.head
            self.tail = self.head
            return

        temp = self.head
        while(temp.next != self.head):
            temp = temp.next

        n = node(data)
        n.next = temp.next
        temp.next = n
        n = None

    def length(self):
        if self.head is None:
            return 0

        temp = self.head.next
        len = 1

        while temp is not self.head:
            len += 1
            temp = temp.next

        return len


print(1)
n = int(input('enter the value of n'))
m = int(input('enter the value of m'))

l = circular_ll()
for i in range(n):
    l.insert(i)

temp = l.head

while l.length() != 1:
    for k in range(m-1):
        temp = temp.next
    if temp.next == l.head:
        l.head = l.head.next

    if temp.next == l.tail:
        l.tail = temp

    temp.next = temp.next.next




print(l.head.data)



















