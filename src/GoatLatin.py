class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """

        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        list1 = S.split(" ")
        print(list1)

        for i in range(len(list1)):
            if(list1[i].startswith(vowels)):
                list1[i]=list1[i]+"ma"
            else:
                firstchar=list1[i][0]
                var1=list1[i][1:]
                var1=var1+firstchar+"ma"
                list1[i]=var1

        print(list1)
        c=1
        for i in range(len(list1)):
            list1[i]=list1[i]+('a'*c)
            c+=1

        print(" ".join(list1))





S = "I speak Goat Latin"
ls = Solution()
var = ls.toGoatLatin(S)
#for i in var:
 #   print(i);