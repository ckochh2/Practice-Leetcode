class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (len(nums) <= 2):
            return -1

        leftsum = nums[0]
        rightsum = sum(nums) - nums[0]
        if (leftsum == rightsum):
            return 0
        for i in range(1, len(nums)):
            rightsum = rightsum - nums[i]
            if (leftsum == rightsum):
                return i
            else:
                leftsum += nums[i]

        return -1

nums = [-1,-1,-1,-1,1,1]
ls = Solution()
var=ls.pivotIndex(nums)
print(var)