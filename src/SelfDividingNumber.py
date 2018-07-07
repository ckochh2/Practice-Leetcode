class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        output = []
        for i in range(left, right + 1):
            if(i%10==0):
                continue
            else:
                b = False
                r = i
                while (r > 0):
                    rem = r % 10
                    if(rem==0):
                        b=True
                        break
                    if (i % rem != 0):
                        b = True
                        break
                    r = int(r / 10)
            if (b == False):
                output.append(i)

        return output

x=66
y=708
var=[]
ls = Solution()
var=ls.selfDividingNumbers(x,y)
print(var)