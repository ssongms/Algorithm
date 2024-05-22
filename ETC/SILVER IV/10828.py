import sys
input = sys.stdin.readline

N = int(input())

class Stack():
    def __init__(self):
        self.stack = [0 for i in range(10000)]
        self.top = -1
        self.stackSize = 0
    
    def pushItem(self, newItem):
        self.top += 1
        self.stack[self.top] = newItem
        self.stackSize += 1

    def popItem(self):
        if self.stackSize == 0:
            print(-1)
            return
        print(self.stack[self.top])
        self.top -= 1
        self.stackSize -= 1

    def getSize(self):
        print(self.stackSize)
    
    def isEmpty(self):
        if self.stackSize == 0:
            print(1)
        else:
            print(0)
    
    def getTop(self):
        if self.top == -1:
            print(-1)
            return
        print(self.stack[self.top])
    
stack = Stack()
for i in range(N):
    commandList = list(input().split())

    if commandList[0] == 'push':
        stack.pushItem(int(commandList[1]))
    if commandList[0] == 'pop':
        stack.popItem()
    if commandList[0] == 'size':
        stack.getSize()
    if commandList[0] == 'empty':
        stack.isEmpty()
    if commandList[0] == 'top':
        stack.getTop()