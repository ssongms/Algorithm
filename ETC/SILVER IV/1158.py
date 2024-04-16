class CircleQueue: # 원형 큐 클래스 정의
    front = 0
    size = 5000 # 최대 사이즈
    queue = list()

    def __init__(self, size):
        self.front = -1 # 0번 인덱스부터 시작하기 때문
        self.size = size
        self.queue = [i+1 for i in range(size)] # 리스트 컴프리헨션 -> [1, 2, 3, 4, ...]
    
    def dequeue(self, K):
        for _ in range(K):
            self.front = (self.front + 1) % self.size
            while self.queue[self.front] == 0: # 0이 나오지 않을 때까지 front를 증가시켜줌
                self.front = (self.front + 1) % self.size
        poppedItem = self.queue[self.front]
        self.queue[self.front] = 0
        return poppedItem

# main
size, K = map(int, input().split())
circleQue = CircleQueue(size)
sequence = []
for i in range(size):
    sequence.append(circleQue.dequeue(K))

print("<" + ", ".join(map(str, sequence)) + ">")