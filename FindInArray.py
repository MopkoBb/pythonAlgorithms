# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here

        return self.buildTree(pre, tin, 0, len(pre) - 1, 0, len(tin)-1)


    def buildTree(self,pre, tin, pstart, pend, tstart, tend):
        if pstart > pend:
            return None

        treeNode = TreeNode(pre[pstart])
        num = tstart
        for a in tin[tstart:tend+1]:
            if pre[pstart] == a:
                break
            num = num + 1

        len = num - tstart
        treeNode.left = self.buildTree(pre, tin, pstart + 1, pstart + len, tstart, num - 1)
        treeNode.right = self.buildTree(pre, tin, pstart + len + 1, pend, num + 1, tend)
        return treeNode


