class stack:
    def __init__(self, n):
        self.s = [None for i in range(n)]
        self.top1 = -1
        self.top2 = n

    def push1(self, data):
        if self.top1 < self.top2:
            self.top1 += 1
            self.s[self.top1] = data
            print(f"{data} pushed into stack 1")

        else:
            print('stacks over flow')
            return

    def push2(self, data):
        if self.top1 < self.top2:
            self.top2 -= 1
            self.s[self.top2] = data
            print(f"{data} pushed into stack 2")


        else:
            print('stacks over flow')
            return

    def pop1(self):
        if self.top1 == -1 :
            print('stack1 is empty ,  popping not possible')
            return
        p = self.s[self.top1]
        self.s[self.top1] = None
        self.top1 -=1
        return p

    def pop2(self):
        if self.top2 == len(self.s) :
            print('stack2 is empty , popping not possible')
            return
        p = self.s[self.top2]
        self.s[self.top2] = None
        self.top2 +=1
        return p

    def len_1(self):
        return self.top1 + 1

    def len_2(self):
        return len(self.s) - self.top2

    def print1(self):
        if self.top1 == -1:
            print('stack1 is empty')
            return
        print(self.s[0:self.top1 + 1])

    def print2(self):
        if self.top1 == -1:
            print('stack1 is empty')
            return

        print(self.s[len(self.s) - 1:self.top2 - 1: -1])


s = stack(14)
s.push1(1)
s.push2(6)
s.push1(2)
s.push2(7)
s.push1(3)
s.push2(8)

s.pop1()
s.pop2()

s.pop1()
s.pop2()

s.pop1()
s.pop2()

print(s.top1)
print(s.top2)

s.print1()
s.print2()

print(s.len_1())
print(s.len_2())
