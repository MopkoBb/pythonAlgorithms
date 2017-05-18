class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    # 层序遍历
    def TreeDepth(self, pRoot):
        depth = 0
        stack = []
        if not pRoot:
            return 0
        stack.append(pRoot)
        while stack:
            size = len(stack)
            depth += 1
            while size:
                node = stack.pop(0)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                size -= 1
        return depth

    # 递归遍历
    def TreeDepth2(self, pRoot):
        if not pRoot:
            return 0
        return max(1+self.TreeDepth2(pRoot.left), 1+self.TreeDepth2(pRoot.right))

