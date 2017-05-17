class Solution():
    # 暴力搜索
    def InversePairs(self, data):
        if not data:
            return 0
        pairs = 0
        for index in range(len(data)-1):
            for a in data[index+1:]:
                if data[index] > a:
                    pairs += 1
        return pairs
    # 归并排序

    def __init__(self):
        self.count = 0

    def mergeSort(self, data):
        if len(data) <= 1:
            return data
        mid = int(len(data)/2)
        left = self.mergeSort(data[:mid])
        right = self.mergeSort(data[mid:]) 
        return self.merge(left, right)

    def merge(self, left, right):
        l, r = 0, 0 
        mergeList = []
        while l < len(left) and r < len(right):
            if left[l] > right[r]:
                self.count += len(left[l:])
                mergeList.append(right[r])
                r += 1
            else:
                mergeList.append(left[l])
                l += 1
        mergeList += left[l:]
        mergeList += right[r:]
        return mergeList

    def InversePairs2(self, data):
        self.mergeSort(data)
        return self.count

    def InversePairs3(self, data):
        if len(data) <= 0:
            return 0
        count = 0
        copy = []
        for i in range(len(data)):
            copy.append(data[i])
        copy.sort()
        i = 0
        while len(copy) > i:
            count += data.index(copy[i])
            data.remove(copy[i])
            i += 1
        return count

    def InversePairs4(self, data):
        length = len(data)
        if data == None or length <= 0:
            return 0
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]

        count = self.InversePairsCore(data, copy, 0, length - 1)
        return count

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) // 2
        left = self.InversePairsCore(copy, data, start, start + length)
        right = self.InversePairsCore(copy, data, start + length + 1, end)

        # i初始化为前半段最后一个数字的下标
        i = start + length
        # j初始化为后半段最后一个数字的下标
        j = end

        indexCopy = end
        count = 0
        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start + length + 1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1

        return left + right + count

s = Solution()
a = s.InversePairs4([6,202,100,301,38,8,1])
print(a)
