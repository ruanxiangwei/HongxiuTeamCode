class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



Input = [0]
tree = [0]
Input = Input + input().split()
cnt = 1
for item in Input:
    tmp = TreeNode(item)
    tree.append(tmp)
for item in tree:
    if item.val == "null":
        continue
    if 2 * cnt <= len(Input) and tree[2*cnt].val != "null":
        item.left = tree[2*cnt]
    if 2 * cnt + 1 <= len(Input) and tree[2*cnt+1].val != "null":
        item.right = tree[2*cnt+1]
    cnt += 1


def preorder(i):
    if tree[i] == 0:
        return
    print(tree[i])
    preorder(2*i)
    preorder(2*i+1)

def inorder(i):
    if tree[i] == 0:
        return
    inorder(2*i)
    print(tree[i])
    inorder(2*i+1)

def postorder(i):
    if tree[i] == 0:
        return
    postorder(2*i)
    postorder(2*i+1)
    print(tree[i])

class TreeNode:
    def __inti__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def __init__(self, tlist):
        self.root = TreeNode(tlist[0])
        for i in tlist[1:]:
            self.insert(i)

    def preorder(self, node):
        if node is None:
            return
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val)