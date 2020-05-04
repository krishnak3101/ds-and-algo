class node():
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = node(data)
            return

        n = node(data)
        n.next = self.head
        self.head = n

    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.data

    def peek(self):
        return self.head.data

    def print(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


s = stack()
for i in range(6):
    s.push(i+1)


s.print()
print(s.pop())
s.print()
print(s.peek())
