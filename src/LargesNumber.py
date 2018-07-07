class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max1 = max(nums)
        maxindex = 0
        for i in range(len(nums)):
            if (max1 != nums[i]):
                if(max1 < 2 * nums[i]):
                    return -1
            else:
                maxindex = i

        return maxindex

nums = [1,0]
ls = Solution()
var=ls.dominantIndex(nums)
print(var)