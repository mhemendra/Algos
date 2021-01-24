import sys
from Stack import Stack
class StackWithMin(Stack):
    def __init__(self):
        super().__init__()# To make sure the Child has all the variables in parent
        self.minStack = Stack()

    def push(self,item):
        if(item<=self.getMin()):
            self.minStack.push(item)
        super().push(item)

    def pop(self):
        value = super().pop()
        if(value==self.getMin()):
            self.minStack.pop()
        return value

    def getMin(self):
        if(self.minStack.isEmpty()):
            return sys.maxsize
        else:
            return self.minStack.peek()

if __name__ == '__main__':
    stack = StackWithMin()
    stack.push(4)