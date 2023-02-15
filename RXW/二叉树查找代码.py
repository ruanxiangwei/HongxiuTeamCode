class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, tlist):
        self.root = TreeNode(tlist[0])
        for i in tlist[1:]:
            self.insert(i)

    def search(self, node, parent, data):
        if node is None:
            return 0, node, parent
        elif data == node.data:
            return 1, node, parent
        elif data < node.data:
            return self.search(node.left, node, data)
        else:
            return self.search(node.right, node, data)

    def insert(self, data):
        exist, n, p = self.search(self.root, self.root, data)
        if exist:
            return
        else:
            new_node = TreeNode(data)
            if data > p.data:
                p.right = new_node
            else:
                p.left = new_node

    def getlast(self, node, data, maxn):
        if node in None:
            return 0, maxn
        elif data == node.data:
            if node.left == None:
                return 1, maxn
            else:
                tmp = node.left
                while tmp.right is not None:
                    tmp = tmp.right
                return 1, tmp
        elif data < node.data:
            return self.getlast(node.left, data, maxn)
        else:
            if maxn.data < node.data:
                maxn = node
            return self.getlast(node.right, data, maxn)