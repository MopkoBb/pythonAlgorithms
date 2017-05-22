# -*- coding:utf-8 -*-
class Solution():
    def LeftRotateString(self, string, n):
        if not string:
            return False
        while n:
            string = string[1:] + string[0]
            n -= 1
        return string
