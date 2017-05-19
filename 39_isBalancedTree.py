class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class IsBalanced_Solution():
    def DepthTree(self, pRoot):
        if not pRoot:
            return 0
        return max(self.DepthTree(pRoot.left)+1, self.DepthTree(pRoot.right)+1)

    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        left = self.DepthTree(pRoot.left)
        right = self.DepthTree(pRoot.right)
        if abs(left-right) <= 1:
            return True
        else:
            return False


