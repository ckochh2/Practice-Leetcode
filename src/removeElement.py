class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        '''
        for i in range(len(nums)):
            if(nums[i]==val):
                nums.remove(val)
                nums.append(val)
                count+=1
        '''
        '''
        start = 0
        end = len(nums) - 1
        while (start < end):
            if (nums[end] == val):
                end -= 1
                count += 1
            elif (nums[start] == val):
                count += 1
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            else:
                start += 1

        len1 = len(nums) - count
        return len1
        '''

        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1

        return count

nums = [3,2,2,3]
val=3
ls = Solution()
var=ls.removeElement(nums,val)
for i in range(var):
    print(nums[i])