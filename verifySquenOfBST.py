# BST： 二叉查询树， 左节点小于根节点小于右节点
# 后序遍历： 遍历顺序为 左子树->右子树->根节点
# 由以上，后序遍历序列A 最后一个元素为根节点，
# A前x元素小于根节点，为左子树；
# 后y个元素小于根节点，为右子树， 递归遍历即可

class Solution():
    def judge(self, squence, l, r):
        if l > r:
            return True
        cursor = l
        # 找出左子树
        for a in squence[l:r]:
            if a < squence[r]:
                cursor += 1
        # 检查序列中剩下的元素是否都大于根节点，若否，返回False
        for i in squence[cursor:r]:
            if i < squence[r]:
                return False
        # 测试
        # print(squence[l: cursor])
        # print(squence[cursor: r])
        # print('$$$$')
        return self.judge(squence, l, cursor-1) and self.judge(squence, cursor, r-1)

    def VerifySquenceOfBST(self, squence):
        if not squence:
            return False
        return self.judge(squence, 0, len(squence)-1)

array = [5, 7, 6, 9, 11, 10, 8]
S = Solution()
print(S.VerifySquenceOfBST(array))

# 测试输出：
# [5, 7, 6]
# [9, 11, 10]
# $$$$

# [5]
# [7]
# $$$$

# []
# []
# $$$$

# []
# []
# $$$$

# [9]
# [11]
# $$$$

# []
# []
# $$$$

# []
# []
# $$$$