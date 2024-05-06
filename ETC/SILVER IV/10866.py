import sys
class Deque:
    def __init__(self):
        self.size = 0
        self.deque = []

    def isEmpty(self):
        if len(self.deque) == 0:
            return 1
        else:
            return 0
    
    def pushBack(self, num):
        self.deque.append(num)
        self.size += 1
    
    def pushFront(self, num):
        self.deque.insert(0, num)
        self.size += 1
    
    def popFront(self):
        if self.isEmpty() == 1:
            return -1
        popItem = self.deque[0]
        del self.deque[0]
        self.size -= 1
        return popItem
    
    def popBack(self):
        if self.isEmpty() == 1:
            return -1
        popItem = self.deque[self.size-1]
        self.deque.pop(self.size-1)
        self.size -= 1
        return popItem

    def getSize(self):
        return self.size

    def getFront(self):
        if self.isEmpty() == 1:
            return -1
        return self.deque[0]
    
    def getBack(self):
        if self.isEmpty() == 1:
            return -1
        return self.deque[self.size-1]


dq = Deque()
N = int(input())
for i in range(N):
    commandLine = sys.stdin.readline()
    command = commandLine.split()

    if command[0] == 'push_back':
        dq.pushBack(command[1])
    
    if command[0] == 'push_front':
        dq.pushFront(command[1])
    
    if command[0] == 'front':
        print(dq.getFront())
    
    if command[0] == 'back':
        print(dq.getBack())
    
    if command[0] == 'size':
        print(dq.getSize())
    
    if command[0] == 'empty':
        print(dq.isEmpty())
    
    if command[0] == 'pop_back':
        print(dq.popBack())
    
    if command[0] == 'pop_front':
        print(dq.popFront())