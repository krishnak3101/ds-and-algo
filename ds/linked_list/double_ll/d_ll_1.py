# declaration
# insertion
# finding length
# insert at a given position
# delete ele in a doubly ll
# reverse the double LL


class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class double_ll():
    def __init__(self):
        self.head = None
        # self.length = None

    def insert(self, data):
        if self.head is None:
            self.head = node(data)
            return

        temp = self.head
        # prev = temp
        while (temp.next):
            #   prev = temp
            temp = temp.next

        n = node(data)
        node.prev = temp
        temp.next = n

    def print(self):
        if self.length() == 0:
            print('ll is empty')

        temp = self.head

        while (temp):
            print(temp.data,end = " ")
            temp = temp.next

        return

    def length(self):
        temp = self.head
        len = 0
        while (temp):
            len += 1
            temp = temp.next
        return len

    def insert_at(self, pos, data):
        if pos < 0 or pos > self.length() - 1:
            print('invalid index' , end =" ")
            return
        if self.head is None:
            self.head = node(data)

        if pos == 0:
            n = node(data)
            n.next = self.head
            self.head.prev = n
            self.head = n
            return

        temp = self.head
        i = 0
        while i != pos:
            i += 1
            prev = temp
            temp = temp.next

        n = node(data)
        n.next = temp
        temp.prev = n
        prev.next = n


    def delete(self,pos):
        l = self.length()
        if pos < 0 or pos > l - 1:
            print('invalid position')
            return

        if l == 0:
            print('ll is empty')
            return


        if pos == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            temp = None
            return

        count = 1
        temp = self.head.next
        prev = self.head
        while count != pos:
            count += 1
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = temp.next

    def reverse(self):
        if self.length() == 0:
            print('ll is empty')
            return

        temp = self.head

        while(temp.next):
            temp = temp.next

        self.head = temp

        while(temp):
            temp.prev,temp.next = temp.next,temp.prev
            temp = temp.next

        return




list = [4,8]

l = double_ll()

for i in range(len(list)):
    l.insert(list[i])

# print('\n')
# l.print()
# l.insert_at(0,0)
# print('\n')
# l.print()
# l.insert_at(6,6)
# print('\n')
# l.print()
# l.insert_at(4,8)
# print('\n')
# l.print()

# print('\n')
# l.print()
# l.delete(0)
# print('\n')
# l.print()
# l.delete(3)
# print('\n')
# l.print()
# l.delete(1)
# print('\n')
# l.print()

l.print()
l.reverse()
print('\n')
l.print()
