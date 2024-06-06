import sys
input = sys.stdin.readline

N = int(input())

class Stack(): # 스택 클래스 정의
    def __init__(self):
        self.stack = [0 for i in range(10000)] # 메모리 펑펑 써버리기
        self.top = 0 # top 포인터 역할
    
    def switchCommand(self, command, item): # 명령을 분배해주는 역할
        if command == 'push':
            self.pushItem(item)
        if command == 'pop':
            self.popItem()
        if command == 'size':
            self.getSize()
        if command == 'empty':
            self.isEmpty()
        if command == 'top':
            self.getTop()

    def pushItem(self, newItem): # Push
        self.stack[self.top] = newItem
        self.top += 1

    def popItem(self): # Pop
        if self.top == 0: # 스택이 비어있으면 -1 출력
            print(-1)
            return
        self.top -= 1 # top 포인터를 하나 줄여줌
        print(self.stack[self.top]) # pop된 아이템 출력

    def getSize(self): # Size가 몇인지 알려줌 
        print(self.top) # 현재 top 포인터의 위치가 곧 스택의 크기
    
    def isEmpty(self): # 스택이 비어있는지 확인
        if self.top == 0: # top이 0이면 스택이 비어있음 (초기값)
            print(1)
        else:
            print(0)
    
    def getTop(self): # 스택의 top에 있는 값을 출력
        if self.top == 0: # 스택이 비어있으면 -1 출력
            print(-1)
            return
        print(self.stack[self.top-1]) # top 포인터가 가리키는 값 출력 (-1 해줘야함)
    
stack = Stack() # stack 인스턴스 생성
for i in range(N):
    commandList = list(input().split())
    command = commandList[0]
    item = int(commandList[1]) if command == 'push' else 0 # push 명령어일 경우에만 item이 존재
    
    stack.switchCommand(command, item)