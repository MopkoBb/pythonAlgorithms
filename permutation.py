# 递归出口：全排列为它本身时，即长度为1
class Solution():
    def Permutation(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        charList = list(ss)
        charList.sort()
        pStr = []
        # 遍历charList, 作为固定节点
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            # 对剩下字符串递归进行全排列
            temp = self.Permutation(''.join(charList[:i]) + ''.join(charList[i + 1:]))
            print(charList[i], temp)

            for j in temp:
                # 固定节点与剩余字符串全排列分别拼接
                pStr.append(charList[i] + j)
            print(pStr)
            print('*****')

        return pStr

    l = []
    def Permutation2(str1):
        str1 = ''.join(sorted(str1))
        for i in str1:
            tmp = str1.replace(i, "")
            l.append(i)
            print(l, i, tmp)
            print('****')
            if len(tmp) > 1:
                self.Permutation2(tmp)
                del l[-1]
            else:
                print(''.join(l) + tmp)
            del l[-1]

s = Solution()
a = s.Permutation('abc')
print(a)
