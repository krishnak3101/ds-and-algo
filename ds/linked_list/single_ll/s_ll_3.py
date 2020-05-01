# searching if an ele is present in ll iteratively and recursively
# get n th node
# finding the middle node(s)


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ll:
    def __index__(self):
        self.head = None

    def insert_many(self, str):
        l = str.split(" ")
        for i in range(len(l)):
            l[i] = int(l[i])

        self.head = node(l[0])
        temp = self.head
        for j in range(1, len(l)):
            temp.next = node(l[j])
            temp = temp.next

    def insert_at(self, pos, key):
        if pos == 0:  # insertion at head
            temp = node(key)
            temp.next = self.head
            self.head = temp

        if pos > 0 and pos <= self.length():
            c = 0
            temp = self.head
            while c != pos - 1:
                temp = temp.next
                c += 1

            n = node(key)
            n.next = temp.next
            temp.next = n

        if pos < 0 or pos > self.length():
            print('invalid position')

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def length(self):
        temp = self.head
        l = 0
        while (temp):
            l += 1
            temp = temp.next
        return l

    def length_rec(self, root):
        if root is None:
            return 0

        else:
            return 1 + self.length_rec(root.next)

    # delete the first occurance of the node with given key
    def delete_with_key(self, key):

        if self.head != None:

            temp = self.head

            if self.head.data == key:
                self.head = temp.next
                temp = None
                print('\n\n')
                print('linked list after deletion is')
                self.print()
                print(f"\n length is : {self.length()}")

                return

            while (temp):
                prev = temp
                temp = temp.next
                if temp != None and temp.data == key:
                    prev.next = temp.next
                    temp = None
                    print('\n\n')
                    print('linked list after deletion is')
                    self.print()
                    print(f"\n length is : {self.length()}")
                    return
            print('key doesnt exists')

        else:
            print('ll is empty')

    # delete the node at the given index
    def delete_at_index(self, idx):

        if self.length() == 0:
            print('ll is empty ')
            return

        if idx < 0 or idx > self.length() - 1:
            print('invalid index')
            return

        temp = self.head

        if idx == 0:
            self.head = temp.next
            temp = None
            print('\n\n')
            print('linked list after deletion is')
            self.print()
            print(f"\n length is : {self.length()}")

            return
        i = 1

        while (idx <= self.length()):
            prev = temp
            temp = temp.next
            if temp != None and idx == i:
                prev.next = temp.next
                temp = None
                print('\n\n')
                print('linked list after deletion is')
                self.print()
                print(f"\n length is : {self.length()}")
                return
            i += 1

    # function to delete the ll
    def delete_ll(self):
        if self.length() == 0:
            print('ll is empty')
            return

        while (self.head):
            pre = self.head
            self.head = self.head.next
            print(f'\nnode {pre.data} is deleted')
            del pre.data
            pre.next = None

            del pre
            self.head = self.head

            print(f'\n len of ll is {self.length()}')

    def find_ele_iter(self, ele):
        temp = self.head
        while temp:
            if temp.data == ele:
                print('present')
                return
            temp = temp.next

        print("not present")

    def find_ele_rec(self, ele, root):
        if root == None:
            return False

        if root.data == ele:
            return True

        return self.find_ele_rec(ele, root.next)

    def get_nth_node(self, idx):
        if idx < 0 or idx >= self.length():
            print('invalid index')
            return

        temp = self.head
        c = 0
        while (temp):
            if idx == c:
                print(temp.data)
                return
            c += 1
            temp = temp.next

    def find_middle(self):
        temp = self.head
        l = self.length()
        if l == 0 or l==1 or l == 2:
            print("middle element doesnt exists")
            return

        print('middle element is \n')
        m = (l-1)//2
        c = 0
        while c != m:
            c += 1
            temp = temp.next

        if l%2 == 0:
            print(f'{temp.data} and {temp.next.data}\n')
            return

        print(temp.data)
        return


l = ll()
# s = input("enter the elements")
l.insert_many('1 2 4')
l.print()

print('\nlength of ll is:' + str(l.length()))

print('\n')

# deleting the entire ll
# l.delete_ll()


# finding length
# print(f'lnth through interative method : {l.length()}')
# print(f'lnth through recursive method : {l.length_rec(l.head)}')


# searching element
# while True:
#     a = int(input("enter 0 to exit or any other no to continue"))
#     if a == 0:
#         break
#
#     else:
#         print('enter the element to be searched')
#         ele = int(input())
#         l.find_ele_iter(ele)
#         print(f'res_searching : {l.find_ele_rec(ele,l.head)}')


# get nth node
# while True:
#     a = int(input("enter 0 to exit or any other no to continue"))
#     if a == 0:
#         break
#
#     else:
#         print('enter the index')
#         idx = int(input())
#         l.get_nth_node(idx)


# print middle
l.find_middle()
























