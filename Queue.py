class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def isEmpty(self):
        return self.size==0

    def add(self,item):
        itemNode = Node(item)
        #Here both first and last are set to same node when null, so when we update last.next the first.next is also updated
        #But since last=itemNode the next addition, its value changes so first.next goes till end but last has only last element
        if self.isEmpty():
            self.first = itemNode
            self.size+=1
        else:
            self.last.next = itemNode
            self.size+=1
        self.last = itemNode

    def remove(self):
        if self.isEmpty():
            raise Exception("Empty Queue")
        else:
            item = self.first.data
            self.first = self.first.next
            #Else last still has last value
            if self.first is None:
                self.last=None
            self.size-=1
            return item
    def out(self):
        return self.first,self.last

if __name__ =='__main__':
    queue = Queue()
    for i in range(10):
        queue.add(i)
    for i in range(10):
        queue.remove()
    first,last = queue.out()
    print(first,last)



