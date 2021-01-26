from Queue import Queue
from multipledispatch import dispatch
class TreeNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def getChildren(self):
        children = []
        if (self.left is not None):
            children.append(self.left)
        if (self.right is not None):
            children.append(self.right)
        return children

class Tree:
    def __init__(self):
        self.root = None


def traverseTreePreOrder(tree):
    print(tree.data)
    if tree.left is not None:
        traverseTreePreOrder(tree.left)
    if tree.right is not None:
        traverseTreePreOrder(tree.right)

def depthFirst(tree):
    print(tree.data)
    children = tree.getChildren()
    for child in children:
        depthFirst(child)

def breadthFirst(tree):
    queue = Queue()
    queue.add(tree)
    while not(queue.isEmpty()):
        node = queue.remove()
        print(node.data)
        children = node.getChildren()
        for child in children:
            queue.add(child)

def traverseTreeInOrder(tree):
    if tree.left is not None:
        traverseTreeInOrder(tree.left)
    print(tree.data)
    if tree.right is not None:
        traverseTreeInOrder(tree.right)

@dispatch(list)
def createBST(arr):
    return createBST(arr, 0, len(arr)-1)

def createBSTPython(arr):
    if len(arr)==0:
        return None
    mid = int(len(arr)/2)
    leftArr = arr[:mid]
    rightArr = arr[mid+1:]
    node = TreeNode(arr[mid])
    node.left = createBSTPython(leftArr)
    node.right = createBSTPython(rightArr)
    return node

@dispatch(list,int,int)
def createBST(arr,start,end):
    if start>end:
        return None
    mid = int((start+end)/2)
    node = TreeNode(arr[mid])
    node.left = createBST(arr,start,mid-1)
    node.right = createBST(arr,mid+1,end)
    return node


if __name__ == '__main__':
    tree = Tree()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    tree.root = node1
    node1.left = node2
    node1.right = node3
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node6.left = TreeNode(8)
    arr = [i for i in range(12)]
    output = createBST(arr)
    #traverseTreeInOrder(output)
    depthFirst(output)