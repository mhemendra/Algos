class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self,item):
        itemNode = Node(item)
        itemNode.next = self.top
        self.top = itemNode
        self.size+=1

    def isEmpty(self):
        return self.size==0

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from a Empty stack")
        else:
            item = self.top.data
            self.top = self.top.next
            self.size-=1
            return item

    def getSize(self):
        return self.size

    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an Empty Stack")
        else:
            return self.top.data

if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    for i in range(10):
        print(stack.pop())
    stack.peek()
