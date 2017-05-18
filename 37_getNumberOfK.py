class Solution():
    # 利用index()
    def GetNumberOfK(self, data, k):
        if not data:
            return -1
        try:
            index = data.index(k)
        except ValueError:
            return -1
        count = 0
        while data[index] == k:
            count += 1
            index += 1
            print(count, index)
            if index+1 > len(data):
                break
        return count

    # 二分查找
    def GetNumberOfK2(self, data, k):
        low, high = 0, len(data)-1
        find = False 
        while low <= high and not find:
            mid = (high + low) // 2
            if data[mid] == k:
                find = True
            elif data[mid] > k:
                high = mid -1
            else:
                low = mid + 1
        if not find:
            return 0
        count = 0 
        for a in data[mid::-1]:
            if a == k: count += 1
        for a in data[mid+1:]:
            if a == k: count += 1
        return count



s = Solution()
print(s.GetNumberOfK2([1,2,3,3,3,3], 3))
