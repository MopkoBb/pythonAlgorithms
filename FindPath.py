# 1、将当前节点压入栈list，并expectNumber减去当前节点的val
# 2、当节点压入，判断是否叶子节点且expectNumber==0，若是，这是一条路径，压入result
# 3、判断结束，递归左孩子，右孩子
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution():
    def __init__(self):
        self.list = []
        self.result = []

    def FindPath(self, root, expectNumber):
        if not root:
            return []
        expectNumber -= root.val
        self.list.append(root.val)
        if expectNumber == 0 and not root.left and not root.left:
            newList = list(self.list)
            self.result.append(newList)

        self.FindPath(root.left, expectNumber)
        self.FindPath(root.right, expectNumber)
        # 退回父节点，继续遍历
        self.list.pop()jjj
        return self.result

pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5


S = Solution()
print(S.FindPath(pNode1, 22))
