class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            sum1 += min(nums[i], nums[i + 1])

        return sum1

nums = [2,3,1,4]
ls = Solution()
var=ls.arrayPairSum(nums)
print(var)