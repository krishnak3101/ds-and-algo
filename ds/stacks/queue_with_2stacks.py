def enque(data):
    s1.append(data)


def deque():
    if len(s1) == 0:
        print("queue is empty")
        return
    while len(s1) > 0:
        s2.append(s1.pop())
    d = s2.pop()
    while len(s2) > 0:
        s1.append(s2.pop())
    return d

def length():
    return len(s1)


s1 = []
s2 = []

for i in range(9):
    s1.append(i+1)

enque(10)
enque(12)
#print(s1)
while len(s1)>0:
    print(deque())
