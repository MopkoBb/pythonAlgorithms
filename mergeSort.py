class Solution():
    sum = 0
    def MergeSort(self,lists):
        if len(lists) <= 1:
            print(lists)
            return lists
        num = int( len(lists)/2 )
        left = self.MergeSort(lists[:num])
        right = self.MergeSort(lists[num:])
        print(left, right)
        print('*****')
        return self.Merge(left, right)

    def Merge(self, left, right):
        r, l=0, 0
        result=[]
        while l<len(left) and r<len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
                self.sum += len(left[l:])
        result += right[r:]
        result+= left[l:]
        return result
s = Solution()
a = s.MergeSort([6,202,100,301,38,8,1])
print(a, s.sum)

