class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        pre = rotateArray[0]
        for num in rotateArray[1:]:
            if pre > num:
                return num
            else:
                pre = num