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

prevElement = None

def checkBST(tree):
    global prevElement
    if (tree is None):
        return 1
    out = checkBST(tree.left)
    if(out == 0):
        return 0
    if prevElement is not None and prevElement >= tree.data:
        return 0
    prevElement = tree.data
    out=checkBST(tree.right)
    if(out == 0):
        return 0
    return 1

def createListOfListsPerLevel(root):
    levels = []
    i=0
    parent = [root]
    levels.append(parent)
    while not len(levels[i])==0:
        i=i+1
        currentLevel = []
        for node in levels[i-1]:
            children = node.getChildren()
            for child in children:
                currentLevel.append(child)
        if not(len(currentLevel)==0):#code enters once after last level but there are no children in currentLevel,
            levels.append(currentLevel)#so breadking out of loop else the levels[i] index i doesnt exist and
        else:# there is a index out of bounds exception during next loop
            break
    return levels

def checkBalanced(root):
    if root is None:
        return 0
    leftLength = checkBalanced(root.left)
    if(leftLength==-1):
        return -1
    rightLength = checkBalanced(root.right)
    if (rightLength==-1):
        return -1
    heightDiff = rightLength - leftLength
    if(abs(heightDiff)>1):
        return -1
    else:
        return max(leftLength, rightLength) + 1

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
    #node4.left = node5
    #node3.right = node6
    #node2.right = node5
    #node3.left = node6
    #node3.right = node7
    #node6.left = TreeNode(8)
    arr = [i for i in range(12)]
    output = createBSTPython(arr)
    out = createListOfListsPerLevel(output)
    print(out)
    #print(map)
    #depthFirst(output)