from multipledispatch import dispatch
from Queue import Queue
from Tree import TreeNode, Tree

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
    print(tree.data, lastElement)
    if(lastElement >= tree.data or lastElement==-1):
        return -1
    else:
        lastElement = tree.data
    if(tree.right is not None):
        lastElement=checkBST(tree.right,lastElement)
    if(lastElement==-1):
        return -1
    return lastElement

def checkTreeBalanced(tree):
    if tree is None:
        return -1
    left = checkTreeBalanced(tree.left)
    if left == -100:
        return -100
    right = checkTreeBalanced(tree.right)
    if right == -100:
        return -100
    if (abs(left-right) > 1):
        return -100
    return max(left,right) + 1

class checkBSTClass:
    lastElement = None
    def checkBSTBool(self, tree):
        if tree is None:
            return True
        if not self.checkBSTBool(tree.left):
            return False
        if not self.lastElement is None and self.lastElement>tree.data:
            return False
        self.lastElement = tree.data
        if not self.checkBSTBool(tree.right):
            return False
        return True

def inOrderSuccesor(node):
    #parent = node.parent
    if node.right is not None:
        return findLeftMostElement(node.right)
    else:
        return findLeftBranch(node)

def findLeftMostElement(node):
    while node.left is not None:
        node = node.left
    return node

def findLeftBranch(node):
    parent = node.parent
    if parent is None:
        return #Node is the last one in the tree so there is no succesor
    if parent.left == node:
        return parent
    else:
        findLeftBranch(parent)


if __name__ == '__main__':
    tree = Tree()
    node1 = TreeNode(20)
    node2 = TreeNode(10)
    node3 = TreeNode(10)
    tree.root = node1
    node1.left = node2
    node1.right = node3
    node4 = TreeNode(10)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    #node2.right = node4
    #node4.right = node5
    #node2.right = node6
    #node3.right = node7
    checkBSTClass = checkBSTClass()
    output = checkBSTClass.checkBSTBool(tree.root)
    print("Final:",output)