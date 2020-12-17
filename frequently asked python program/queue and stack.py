
# pyton queue and stack implementation 

# python stack implementation
from collections import deque 

class stack:

    def __init__(self):
        self.stk = deque()

    def push(self,val):
        self.stk.append(val)

    def pop(self):
        return self.stk.pop()

    def peek(self):
        return self.stk[-1]

    def is_empty(self):
        return len(self.stk) == 0

    def size(self):
        return len(self.stk)

mystack = stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
pk = mystack.peek()
p = mystack.pop()
c = mystack.is_empty()
s = mystack.size()

print(pk,p,c,s)

#------------------------------------------
# python queue implementation
from collections import deque

class queue:

    def __init__(self):
        self.que = deque()

    def enque(self,val):
        self.que.appendleft(val)

    def deque(self):
        return self.que.pop()

    def is_empty(self):
        return len(self.que) == 0

    def size(self):
        return len(self.que)

myqueue = queue()
myqueue.enque(1)
myqueue.enque(2)
myqueue.enque(3)
myqueue.enque(4)
p = myqueue.deque()
c = myqueue.is_empty()
s = myqueue.size()

print(p,c,s)

