# -*- coding:utf-8 -*-
# 利用升序序列中 i, j距离最远乘积最小
# 当temp > tsum, j减一 同理temp < tsum， i加一
class Solution():
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        length = len(array)
        i, j = 0, length - 1
        while i <= j:
            temp = array[i] + array[j]
            if temp == tsum:
                return [array[i], array[j]]
            elif temp > tsum:
                j -= 1
            elif temp < tsum:
                i += 1
        return []

s = Solution()
a = s.FindNumbersWithSum([1,2,4,7,11,15],15)
print(a)
