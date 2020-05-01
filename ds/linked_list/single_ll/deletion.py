# inserting many elements in a ll
# inserting at a particular postion of ll
# printing a  ll
# delete node of a ll with a given key
# delete node of a ll at a particular index
# deleting the entire ll
# finding length iterative and recursive

class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class ll:
    def __index__(self):
        self.head = None

    def insert_many(self,str):
        l = str.split(" ")
        for i in range(len(l)):
            l[i] = int(l[i])

        self.head = node(l[0])
        temp = self.head
        for j in range(1,len(l)):
            temp.next = node(l[j])
            temp = temp.next


    def insert_at(self,pos,key):
        if pos==0:  #insertion at head
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
            print(temp.data,end = ' ')
            temp = temp.next


    def length(self):
        temp = self.head
        l = 0
        while(temp):
            l += 1
            temp = temp.next
        return l

    def length_rec(self,root):
        if root is None:
            return 0

        else:
            return 1 + self.length_rec(root.next)





    #delete the first occurance of the node with given key
    def delete_with_key(self,key):

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

            while(temp):
                prev = temp
                temp = temp.next
                if temp!=None and temp.data == key:
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


    #delete the node at the given index
    def delete_at_index(self,idx):

        if self.length()==0:
            print('ll is empty ')
            return

        if idx<0 or idx > self.length()-1:
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
        while(idx<=self.length()):
            prev = temp
            temp = temp.next
            if temp!=None and idx == i :
                prev.next = temp.next
                temp = None
                print('\n\n')
                print('linked list after deletion is')
                self.print()
                print(f"\n length is : {self.length()}")
                return
            i+=1

    #function to delete the ll
    def delete_ll(self):
        if self.length()==0:
            print('ll is empty')
            return


        while(self.head):
            pre = self.head
            self.head = self.head.next
            print(f'\nnode {pre.data} is deleted')
            del pre.data
            pre.next = None

            del pre
            self.head = self.head

            print(f'\n len of ll is {self.length()}')







l = ll()
#s = input("enter the elements")
l.insert_many('4 9 2 7 3 6 1 71 515')
l.print()

print('\nlength of ll is:' + str(l.length()))

print('\n')

# deleting the entire ll
l.delete_ll()


# finding length
print(f'lnth through interative method : {l.length()}')
print(f'lnth through recursive method : {l.length_rec(l.head)}')



# while True:
#     a = int(input("enter 0 to exit or any other no to continue"))
#     if a == 0:
#         break
#
#     else:
#         print('enter the index to be deleted')
#         b = int(input())
#         l.delete_at_index(b)



