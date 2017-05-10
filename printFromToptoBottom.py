# 思路就是利用栈， self.queue来记录节点顺序，直到所有的节点遍历完，非常巧妙
class Solution():
    def __init__(self):
        self.queue = []
    def printFromToptoBottom(self, root):
        result = []
        if not root:
            return []
        self.queue.append(root)
        while self.queue:
            tempNode = self.queue.pop(0)
            result.append(tempNode.val)
            if tempNode.left:
                self.queue.append(tempNode.left)
            if tempNode.right:
                self.queue.append(tempNode.right)
        return result
