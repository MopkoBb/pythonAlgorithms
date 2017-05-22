# -*- coding:utf-8 -*-
class Solution():
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            reutrn False
        length = len(array)
        result = []
        for i in range(length):
            if array[i] < tsum:
                for j in range(i, length):
                    if array[j] < tsum and array[i] + array[j] == tsum:
                        result.append(array[i] * array[j])
        return min(result)


