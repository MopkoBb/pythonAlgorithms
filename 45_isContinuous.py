# -*- coding:utf-8 -*-
# 排序后判断有没有除0外重复的数字
class Solution():
    def IsContinuous(self, numbers):
        if len(numbers) != 5:
            return False
        numbers.sort()
        temp = []
        for a in numbers:
            if a != 0:
                temp.append(a)
        length = len(temp)
        for i in range(length-1):
            if temp[i] == temp[i+1]:
                return False
        if temp[length-1] - temp[0] < 5:
            return True

    # 这个方法利用位运算判断是否有除0以外重复的数字
    def IsContinuous2(self, numbers):
        if len(numbers) != 5:
            return False
        flag = 0
        length = len(numbers)
        for i in range(length):
            if flag >> numbers[i] & 1 == 1:
                return False
            flag |= 1 << numbers[i]


s = Solution()
s.IsContinuous([1, 3, 0, 5, 0])
