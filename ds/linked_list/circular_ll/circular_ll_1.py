# implementing circular ll
# inserting many elements in circular_ll
# print the elements
# length of circular_list
# insertion at beginning,last and at a given position
# split into halves
# sorted insert for a circular linked list


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circular_ll:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_many(self, str):
        l = str.split(" ")
        for i in range(len(l)):
            l[i] = int(l[i])

        self.head = node(l[0])
        temp = self.head
        for j in range(1, len(l) + 1):
            if j == len(l):
                self.tail = temp
                temp.next = self.head
            else:
                temp.next = node(l[j])
                temp = temp.next

    def print(self, head):
        if head is None:
            return
        temp = head.next
        print(head.data, end=" ")
        while temp != head:
            print(temp.data, end=" ")
            temp = temp.next
        print('\n')

    def length(self):
        l = 0
        if self.head:
            l += 1

        else:
            return 0

        temp = self.head.next

        while temp != self.head:
            l += 1
            temp = temp.next

        return l

    def insert_at_beg(self, data):
        n = node(data)
        self.tail.next = n
        n.next = self.head
        self.head = n
        n = None

    def insert_at_last(self, data):
        n = node(data)
        self.tail.next = n
        self.tail = n
        n.next = self.head

        n = None

    def insert_at_pos(self, data, pos):
        l = self.length()
        if pos < 0 or pos >= l:
            print('invalid position')
            return
        if pos == 0:
            self.insert_at_beg(data)
            return
        if pos == l - 1:
            self.insert_at_last(data)
            return

        prev = self.head
        temp = self.head.next
        c = 1
        while c != pos:
            c += 1
            prev = temp
            temp = temp.next

        prev.next = node(data)
        prev.next.next = temp

    def split_into_2(self):
        l = self.length()
        if l == 0 or l == 1:
            print('splitting not possible')
            return None,None

        temp = self.head

        s = (l - 1) // 2
        i = 0
        while (i != s):
            i += 1
            temp = temp.next

        self.tail.next = temp.next
        head2 = self.tail.next
        temp.next = self.head
        return self.head, head2


    def sorted_insert(self,data):
        if self.head is None:
            self.head = node(data)
            self.head.next = self.head
            self.tail = self.head
            return

        if self.head.data >= data:
            self.insert_at_beg(data)
            return

        if self.tail.data <= data:
            self.insert_at_last(data)
            return

        temp = self.head
        while(temp.data <= data):
            prev = temp
            temp = temp.next

        n = node(data)
        n.next = temp
        prev.next = n
        n = None






l = circular_ll()
#l.insert_many("")
l.print(l.head)
# print(l.length())

# l.insert_at_last(0)
# l.print(l.head)
# l.insert_at_beg(1)
# l.print(l.head)
# l.insert_at_pos(2, 1)
# l.print(l.head)

#split_int_2
# h1, h2 = l.split_into_2()
# l.print(h1)
# l.print(h2)

# sorted insert
# l.insert_many("1 4 6 7 9 12 45 752 5275 78516 789321")
# l.sorted_insert(1)
# l.sorted_insert(0)
# l.sorted_insert(78)
# l.sorted_insert(45)
# l.sorted_insert(789322)
# l.sorted_insert(789321)


l.print(l.head)


