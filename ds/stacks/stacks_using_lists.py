def push(a):
    stack.append(a)

def pop():
    if len(stack) > 0:
        return stack.pop()
    print("stack is empty")
    return


def peek():
    if len(stack) > 0:
        return stack[len(stack) - 1]
    print("stack is empty")
    return

def print_s():
    for ele in stack:
        print(ele,end =" ")

stack = []
for i in range(5):
    push(i+1)

print_s()
