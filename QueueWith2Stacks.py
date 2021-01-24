from Stack import *

class QueueWith2Stacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.size = 0

    def add(self,item):
        self.stack1.push(item)
        self.size+=1

    def remove(self):
        for i in range(self.size):
            value = self.stack1.pop()
            self.stack2.push(value)
        firstElem = self.stack2.pop()
        self.size-=1
        for i in range(self.size):
            value = self.stack2.pop()
            self.stack1.push(value)
        return firstElem

if __name__ =='__main__':
    queue =  QueueWith2Stacks()
    for i in range(10):
        queue.add(i)
    for i in range(5):
        print(queue.remove())