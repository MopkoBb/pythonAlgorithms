# 题目要求：连续子向量，说明并不一定是从第一个数开始

class Solution():
    def FindGreatestSumOfSubArray(self, array):
        maxList = []
        tmp = 0
        for a in array:
            tmp += a
            if tmp > 0:
                maxList.append(tmp)
            else:
                tmp = 0
        if not maxList:
            return -1
        return max(maxList)
