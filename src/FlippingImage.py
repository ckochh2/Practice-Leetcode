class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        flipped = []
        length1 = len(A)
        #Reverse
        for i in range(length1):
            #for j in range(len(A[i])):
            A[i].reverse()
        #Flip
        for i in range(length1):
            for j in range(len(A[i])):
                if(A[i][j]==1):
                    A[i][j]=0
                else:
                    A[i][j]=1
        print(A)

nums = [[1,1,0],[1,0,1],[0,0,0]]
ls = Solution()
var=ls.flipAndInvertImage(nums)
#print(var)