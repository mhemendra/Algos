from Stack import Stack
class SetOfStacks(Stack):
    def __init__(self):
        super().__init__()
        self.switch_size = 20
        self.extraStackArray = []

    def push(self,item):
        if not self.extraStackArray:# if the extra Array is Empty
            current_stack_size = self.size
        else:
            current_stack_size = self.extraStackArray[-1].size

        if current_stack_size == self.switch_size:
            stack = Stack()
            stack.push(item)
            self.extraStackArray.append(stack)
        else:
            if self.extraStackArray:
                self.extraStackArray[-1].push(item)
            else:
                super().push(item)

    def pop(self):
        if self.extraStackArray:
            if self.extraStackArray[-1].size==0:
                self.extraStackArray.pop()
        if not self.extraStackArray:
            value = super().pop()
        else:
            value = self.extraStackArray[-1].pop()
        return value

    def out(self):
        return self.extraStackArray

if __name__ == '__main__':
    setOfStacks = SetOfStacks()
    for i in range(100):
        setOfStacks.push(i)
    for i in range(11):
        setOfStacks.pop()

    stackArr = setOfStacks.out()
    print(len(stackArr))

