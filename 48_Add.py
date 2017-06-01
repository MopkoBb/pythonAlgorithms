# -*- coding:utf-8 -*-
# 记不进位的相加值为A， A = n1 ^ n2
# 记进位值为B, B = (n1 & n2) << 1
class Solution():
    def Add(self, num1, num2):
        while num2:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp
        return num1


s = Solution()
a = s.Add(11569, 111)
print(a)
