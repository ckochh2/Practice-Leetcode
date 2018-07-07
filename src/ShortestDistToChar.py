class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        list1 = []
        output = []

        for i in range(len(S)):
            if (S[i] == C):
                list1.append(i)

        for i in range(len(S)):
            a=[]
            a[:] = (map(lambda x: x - i, list1))
            a[:] = (map(abs,a))
            var1= min(a)
            output.append(var1)

        return output

S = "loveleetcode"
C="e"
ls = Solution()
var=ls.shortestToChar(S,C)
for i in var:
    print(i);