class MyCircularQueue:

    def __init__(self, k: int):
        self.st = [0] * k
        self.top, self.tail, self.size, self.length = -1, 0, 0, k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.top = (self.top + 1) % self.length
        self.st[self.top] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail + 1) % self.length
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.st[self.tail] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.st[self.top] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size >= self.length
