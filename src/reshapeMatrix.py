class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        count1 = r * c
        count2 = len(nums)*len(nums[0])
        if (count1 != count2):
            return nums

        reshape = []
        k = 0
        flt_list = [item for sublist in nums for item in sublist]
        print("flat list ",flt_list)
        for m in range(r):
            reshape.append(flt_list[k:k+c])
            k=k+c

        print(reshape)

nums = [[1,2],[3,4],[5,6]]
r=2
c=3
ls = Solution()
var=ls.matrixReshape(nums,r,c)


