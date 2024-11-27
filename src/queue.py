class static_queue:
    def __init__(self, limit: int = 0):
        self.data: list[int | None] = [None]*limit
        self.limit: int = limit
        self.front: int = 0
        self.rear: int = 0
        self.size: int = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit

    def enQueue(self, item: int) -> None:
        if self.isFull:
            raise ValueError("Queue is full")
        
        self.data[self.rear] = item
        self.rear = (self.rear+1)%self.limit
        self.size += 1

    def deQueue(self) -> int:
        if self.size == 0:
            raise ValueError("Queue is empty")
        
        item = self.data[self.front]
        self.front = (self.front+1)%self.limit
        self.size -= 1
        
        assert item is not None, "For some reason item is None"
        return item

    def queueRear(self):
        pass

    def queueFront(self):
        pass
