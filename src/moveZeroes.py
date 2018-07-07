class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) - 1

        while(left<right):
            if(nums[left]!=0):
                left+=1
            


        for i in nums:
            if (i == 0):




nums = [2, 3, 1, 1, 4]
ls = Solution()
var = ls.canJump(nums)
print(var)