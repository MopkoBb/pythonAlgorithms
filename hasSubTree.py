# 1. 设置标志位result = False,一旦匹配成功,返回result = True
# 2. 递归.若根节点相等，递归DoesTree1HasTree2(),如根节点不相等,
# 则判断tree1的左子树和tree2是否相等，tree1右子树和tree2是否相等
# 3.在HasSubtree中，tree1和tree2同时不为空才能进行判断，在DoesTree1HasTree2中，
# 若tree2为空，则说明第二棵树遍历完了，即匹配成功，
# 若tree1为空，有两种情况：(1)若tree2为空，则不匹配(2)若tree2为空，说明匹配。

class Solution():
    def DoesTree1HasTree2(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1HasTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HasTree2(pRoot1.right, pRoot2.right)
    def hasSubTree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HasTree2(pRoot1, pRoot2)
            if not result:
                result = self.DoesTree1HasTree2(pRoot1.left, pRoot2)
            if not result:
                result = self.DoesTree1HasTree2(pRoot1.right, pRoot2)
        return result
