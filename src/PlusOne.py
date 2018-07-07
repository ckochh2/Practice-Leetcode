class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits) - 1
        if (digits[l] < 9):
            digits[l] = digits[l] + 1
            return digits

        b = True
        for j in range(len(digits)):
            if (digits[j] != 9):
                b = False

        if (b == True):
            digits[0] = 1
            for j in range(1,l+1):
                digits[j]=0
            digits.append(0)
            return digits

        for i in range(l, 0, -1):
            if (digits[i] >= 9):
                digits[i] = 0
                digits[i - 1] = digits[i - 1] + 1

        return digits

digits = [8,9,9,9]
ls = Solution()
var=ls.plusOne(digits)
for i in range(len(var)):
    print(var[i]);