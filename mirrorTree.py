class Solution():
    def Mirror(self, root):
        if not root:
            return False
        mid = root.left
        root.left = root.right
        root.right = mid
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        return root
