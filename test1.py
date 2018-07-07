class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0

        for i in range(len(nums)-1, -1,-1):
            if (nums[i] >= nums[i - 1]):
                continue
            else:
                count += 1

            if (count >= 2):`
                return False
        '''
        prev = 0
        curr = 1
        while (curr < len(nums)):
            if (nums[prev] <= nums[curr]):
                prev += 1
                curr += 1
            else:
                count += 1

            if (count == 1):
                curr += 1
            elif (count >= 2):
                return False
        '''

        return True

nums = [4,2,1]
ls = Solution()
var=ls.checkPossibility(nums)
print(var)