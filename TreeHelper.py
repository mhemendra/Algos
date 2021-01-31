from multipledispatch import dispatch
from Queue import Queue
from Tree import TreeNode

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
@dispatch(list,int,int)
def createBST(arr,start,end):
    if start>end:
        return None
    mid = int((start+end)/2)
    node = TreeNode(arr[mid])
    node.left = createBST(arr,start,mid-1)
    node.right = createBST(arr,mid+1,end)
    return node

def createDictofLevels(tree):
    rootNode = tree
    levels = {}
    i=0
    levels.setdefault(i, [])
    levels[i].append(rootNode)
    while not len(levels[i])==0:
        i=i+1
        levels.setdefault(i, [])
        for node in levels[i-1]:
            children = node.getChildren()
            levels[i].extend(children)
    return levels

def checkBST(tree,lastElement=-100):
    if(tree.left is not None):
        lastElement=checkBST(tree.left,lastElement)
    if(lastElement >= tree.data or lastElement==-1):
        return -1
    else:
        lastElement = tree.data
    if(tree.right is not None):
        lastElement=checkBST(tree.right,lastElement)
    if(lastElement==-1):
        return -1
    return lastElement