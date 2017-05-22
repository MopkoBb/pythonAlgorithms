# -*- coding:utf-8 -*-
class Solution():
    def FindContinuousSquence(sum):
        if not sum:
            return False
        n = 2
        while True:
            an = (2 * sum - n * n + n) / 2.0 * n
            if type(an) == int: break
            n += 1
        result = []
        for i in range(n):
            result.append(an)
            an += 1
        return result
