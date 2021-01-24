class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

def printLL(head):
    while head.next is not None:
        print(head.data)
        head = head.next

def iterateLinkedList():
    llist = SLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(1)
    node50 = Node(50)
    node40 = Node(40)
    llist.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node40
    node40.next = node50
    #removeDuplicates(llist.head)
    #deleteMidElement(node5)
    #printLL(llist.head)
    splitbyK(llist.head,)

def removeDuplicates(head):
    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if(runner.next.data == current.data):
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    printLL(head)

def kthFromLast(head,k):
    kthRunner=head
    for i in range(k):
        if kthRunner.next is None:
            print(f'Linked List doesnt have {k+1} elements')
            return False
        kthRunner = kthRunner.next
    while kthRunner.next is not None:
        kthRunner = kthRunner.next
        head = head.next
    print(head.data)

def kthFromLastRec(head, k):
    if (head.next is None):
        return 0
    index = kthFromLastRec(head.next, k) + 1
    print(index)
    #if (index == k):
    #    print(head.data)
    return index

def deleteMidElement(node):
    if(node.next==None):
        return False
    node.data = node.next.data
    node.next = node.next.next

def intersetPoint(head1,head2):
    length1 = 0
    length2 = 0
    head1Copy = head1
    head2Copy = head2
    while head1.next is not None:
        length1+=1
        head1 = head1.next

    while head2.next is not None:
        length2+=1
        head2= head2.next
    length = abs(length1-length2)
    if(length1>length2):
        for i in range(length):
            head1Copy = head1Copy.next
        while head1Copy is not None:
            if(head1Copy==head2Copy):
                return head1Copy.data
            else:
                head1Copy=head1Copy.next
                head2Copy=head2Copy.next
    else:
        for i in range(length):
            head2Copy = head2Copy.next
        while head2Copy is not None:
            if (head1Copy == head2Copy):
                return head2Copy.data
            else:
                head1Copy = head1Copy.next
                head2Copy = head2Copy.next
    return -1

def splitbyK(node, k=2):

    newLL = SLinkedList()
    newNode = Node(node.data)
    newLL.head = newNode
    tail = newNode

    while node.next is not None:
        if(node.next.data > k):
            headNode = Node(node.next.data)
            headNode.next = newLL.head
            newLL.head = headNode
        else:
            tailNode = Node(node.next.data)
            tail.next = tailNode
            tail=tailNode
        node = node.next
    printLL(newLL.head)

if __name__ == '__main__':

    node = Node(1)
    head = node
    node.next = head
    while node.next is not None:
        print(node.next.data)
    #iterateLinkedList()