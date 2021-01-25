from Stack import Stack
class SetOfStacks(Stack):
    def __init__(self):
        super().__init__()
        self.switch_size = 10
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
                self.extraStackArray.pop()#removing the extra Stack
        if not self.extraStackArray:
            value = super().pop()
        else:
            value = self.extraStackArray[-1].pop()
        return value

    """def popAt(self,index):
        totalStacks = self.size #The first stack size
        for i in range(len(self.extraStackArray)):
            totalStacks+=self.extraStackArray[i].size
        if(index>totalStacks):#index to start at 1
            raise Exception(f"Index {index} greater than stack size {totalStacks}")
        elem = self.top

        if(index<=self.switch_size):
            indexFromTop = self.switch_size - index
            #elem = self.top
            for i in range(indexFromTop):
                elem = elem.next
        else:
            stackNum = int(index/self.switch_size)
            indexInStack = index%self.switch_size
            if(indexInStack==0):
                stackNum -= 1 #20 belongs to first stack
                indexFromTop = 0
            else:
                indexFromTop = self.switch_size - indexInStack
            elem = self.extraStackArray[stackNum-1].top
            for i in range(indexFromTop):
                elem = elem.next
            print(stackNum, indexInStack)
        return elem.data"""

    def popAt(self,index):
        if(self.size>index):
            indexFromTop = self.size-index
            elem = self.top
            for i in range(indexFromTop-1):
                elem=elem.next
            item = elem.next.data
            elem.next = elem.next.next
            self.size -=1
            return item
        elif(self.size==index):
            item = self.top.data
            self.top = self.top.next
            self.size -= 1
            return item
        else:
            sizeTillI=self.size
            stackNum=0
            for i in range(len(self.extraStackArray)):
                sizeTillI += self.extraStackArray[i].size
                if(sizeTillI>=index):
                    stackNum = i
                    break
            if(sizeTillI<index):
                raise Exception(f"Index {index} greater than total stack size {sizeTillI}")
            indexFromTop = sizeTillI-index
            if not indexFromTop==0:
                elem = self.extraStackArray[stackNum].top
                for i in range(indexFromTop-1):
                    elem = elem.next
                item = elem.next.data
                elem.next = elem.next.next
                self.extraStackArray[stackNum].size-=1
                return item
            else:
                elem = self.extraStackArray[stackNum].top.data
                self.extraStackArray[stackNum].top = self.extraStackArray[stackNum].top.next
                self.extraStackArray[stackNum].size -= 1
                return elem

    def out(self):
        return self.extraStackArray

if __name__ == '__main__':
    setOfStacks = SetOfStacks()
    for i in range(1,101):
        setOfStacks.push(i)
    #for i in range(11):
     #
    #setOfStacks.popAt(15)
    #setOfStacks.popAt(14)
    for i in range(100,0, -10):
        print(setOfStacks.popAt(i))
    print(setOfStacks.popAt(90))


