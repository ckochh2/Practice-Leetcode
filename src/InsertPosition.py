import math

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        mid = math.floor(len(nums) / 2)

        if (len(nums) == 1):
            return mid


        if (nums[mid] == target):
            return nums.index(nums[mid])
        elif (target < nums[mid]):
            return self.searchInsert(nums[1:mid], target)
        elif (target > nums[mid]):
            return self.searchInsert(nums[mid+1:], target)
        elif (nums[mid] != target & (len(nums) - 1) == 1):
            return nums.index(nums[mid]) + 1
        '''
        i = 0
        if (target < nums[i]):
            return 0
        #if (target == nums[i]):
        #    return i
        i=1
        while (i< len(nums)):
            if (nums[i-1] == target):
                return i-1
            if (target > nums[i-1] and target < nums[i]):
                return i
            i = i + 1

        return len(nums)

nums = [1,3,5,6]
target = 5
ls = Solution()
var=ls.searchInsert(nums,target)
print(var)