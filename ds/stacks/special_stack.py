# operations are push(), pop(), isEmpty() and an additional operation getMin() which should return minimum element from the SpecialStack. All these operations of SpecialStack must be O(1)

def push(data):
    s1.append(data)
    s2.append(min(s1))


def pop():
    s2.pop()
    return s1.pop()

def get_min():
    return s2[-1]


def is_empty():
    return len(s1)==0



s1 = []
s2 = []

a = [6,8,5,20,4,7]

for ele in a:
    push(ele)

print(get_min())
pop()
print(get_min())
pop()
print(get_min())
pop()
print(get_min())
pop()
print(get_min())

