class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        len1 = len(nums)
        if len1 == 0:
            return 0

        i, j = 0, 0
        prev, pre_prev = nums[0] - 1, nums[0] - 2
        while j < len1:
            if nums[j] == prev and prev == pre_prev:
                nums[i] = nums[j]
            else:
                if i != j:
                    nums[i] = nums[j]
                i += 1
            pre_prev, prev = prev, nums[j]
            j += 1

        return i

nums = [0,0,1,1,1,2,2,3]
ls = Solution()
var=ls.removeDuplicates(nums)
for i in range(var):
    print(nums[i]);
