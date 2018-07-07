class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xlist = list(bin(x))
        xlist = xlist[2:]
        ylist = list(bin(y))
        ylist = ylist[2:]
        # print(xlist)
        # print(ylist)

        # if(len(xlist)>len(ylist))):
        #   ylist.append(0)

        i = len(xlist) - 1
        j = len(ylist) - 1

        count = 0
        # max1=max(i,j)
        while (i >= 0 or j >= 0):
            if (xlist[i] != ylist[j] and i>=0 and j>=0):
                count += 1
                i -= 1
                j -= 1
            elif (i <0 and j >= 0):
                if(ylist[j] == "1"):
                    count += 1
                j -= 1
            elif (j <0 and i >= 0):
                if (xlist[i] == "1"):
                    count += 1
                i -= 1
            else:
                i -= 1
                j -= 1

        return count

#words= ["gin", "zen", "gig", "msg"]
x=1
y=4
ls = Solution()
var=ls.hammingDistance(x,y)
print(var)