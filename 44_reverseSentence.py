# -*- coding:utf-8 -*-
class Solution():
    def ReverseSentence(self, string):
        if not string:
            return ""
        sList = string.split(' ')
        sList.reverse()
        return ' '.join(sList)
