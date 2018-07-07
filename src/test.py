class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        l = len(nums)
        if (l == 1 & nums[0] == 1):
            return True
        newindex = 0
        # print(l)
        
        for i in range(l):
            if (newindex <= l):
                newindex = newindex + nums[newindex]
            if (newindex == l - 1):
                return True
            if (newindex >= len(nums)):
                break
        return False
        '''
        lastpos = len(nums) - 1
        n=len(nums)-1
        for i in range(n,-1,-1):
            if(i+nums[i]>=lastpos):
                lastpos=i

        return lastpos == 0


nums = [2,3,1,1,4]
ls = Solution()
var=ls.canJump(nums)
print(var)