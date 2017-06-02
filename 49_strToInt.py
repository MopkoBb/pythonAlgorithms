# -*- coding:utf-8 -*-
class Solution():
    def StrToInt(self, s):
        if not s:
            return 0
        flag = 1
        if s[0] == '-':
            flag = -1
        a = 0
        if s[0] == '+' or s[0] == '-':
            a = 1
            if len(s) == 1:
                return 0
        for i in range(a, len(s)):
            if not '0' <= s[i] <= '9':
                return 0
            if i == a:
                result = ord(s[i]) - 48
            else:
                result = result * 10 + ord(s[i]) - 48
        return flag * result

s = Solution()
a = s.StrToInt('-')
print(a)