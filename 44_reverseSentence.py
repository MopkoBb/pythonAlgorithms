# -*- coding:utf-8 -*-
class Solution():
    def ReverseSentence(self, string):
        if not string:
            return False
        sList = string.split(' ')
        sList.reverse()
        return ' '.join(sList)
