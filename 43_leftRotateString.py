# -*- coding:utf-8 -*-
class Solution():
    def LeftRotateString(self, string, n):
        if not string:
            return ""
        return string[n:] + string[0:n]

