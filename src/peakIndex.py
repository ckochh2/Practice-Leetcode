class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        for mid in range(1, len(A)):
            if (A[mid]>A[mid - 1] and A[mid] < A[mid + 1]):
                print(mid)


A=[0,2,1,0]
ls = Solution()
ls.peakIndexInMountainArray(A)