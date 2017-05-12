# 将BST按照前序遍历压入栈stack，得到的是已排序的顺序
# 接着只需要讲左孩子指针指向栈左边元素，右孩子指向右边元素
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def __init__(self):
        self.stack = []

    def pre(self, pRootOfTree):
        if not pRootOfTree:
            return None
        if pRootOfTree.left:
           self.pre(pRootOfTree.left)
        self.stack.append(pRootOfTree)
        if pRootOfTree.right:
            self.pre(pRootOfTree.right)

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        self.pre(pRootOfTree)
        pRootOfTree = self.stack[0]
        preNode = self.stack[0]
        preNode.left = None
        for a in self.stack[1:]:
            preNode.right = a
            a.left = preNode
            preNode = a
        preNode.right = None
        return pRootOfTree


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
nlist = S.Convert(pNode1)
print(nlist)
