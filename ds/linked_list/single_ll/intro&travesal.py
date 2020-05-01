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
            l[i] = float(l[i])

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



l = ll()
s = input("enter the elements")
l.insert_many(s)
l.print()
print('length of ll is:' + str(l.length()))

a = [[0,5],[6,484],[3,-854]]

print('\n')

for ele in a:
    print('ele to be inserted is :' + str(ele[1]) + 'at' + str([ele[0]]))
    print('\n')
    l.insert_at(ele[0],ele[1])
    print("updated ll :" ,end = "  ")
    l.print()



