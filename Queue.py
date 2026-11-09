class Queue:

    def __init__(self, size):
        self.size = size
        self.count = 0
        self.front = 0
        self.back = 0
        self.table = [None] * size

    def isEmpty(self):
        if self.count == 0:
            return True
        return False

    def isFull(self):
        if self.count == self.size:
            return True
        return False

    def enqueue(self, record):
        if not self.isFull() and not (record[1] < 1 or record[1] > 100):
            self.table[self.back] = record
            self.back  = (self.back + 1) % self.size
            self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        
        first = self.table[self.front]
        self.front = (self.front + 1) % self.size 
        self.count -= 1
        return first