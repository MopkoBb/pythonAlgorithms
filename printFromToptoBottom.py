class Solution():
    def __init__(self):
        self.queue = []
    def printFromToptoBottom(self, root):
        result = []
        if not root:
            return []
        self.queue.append(root)
        while self.queue:
            tempNode = self.queue[0]
            result.append(tempNode.val)
            if tempNode.left:
                self.queue.append(tempNode.left)
            if tempNode.right:
                self.queue.append(tempNode.right)
        return result
