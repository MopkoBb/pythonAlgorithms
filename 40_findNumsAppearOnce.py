class Solution():
    def FindNumsAppearOnce(self, array):
        if not array:
            return -1
        string = ''
        while array:
            string += str(array.pop(0))
        result = []
        for a in string:
            strCopy = string.replace(a, '')
            if len(strCopy) + 1 == len(string) and len(result) < 2:
                result.append(int(a))
        print(result)
        return result

    # 采用异或
    def FindNumsAppearOnce2(self, array):
        # 1. 将所有的数异或保存至bitResult，结果是两个只出现一次数相互已获得结果
        bitResult = 0
        for a in array:
            bitResult ^= a
        # 2. 寻找bitResult最低位的1，保存至index
        index = 0
        while bitResult & 1 == 0 and index < 32:
            index += 1
            bitResult >>= 1
        # 3. 对array进行分组异或，即index位相同的数异或至num1，不同的保存至num2
        num1, num2 = 0, 0
        for a in array:
            if (a >> index) & 1 == 1:
                num1 ^= a
            else:
                num2 ^= a
        return num1, num2

s = Solution()
a = s.FindNumsAppearOnce([2,4,3,6,3,2,5,5])
