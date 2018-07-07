class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        dic1 = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }

        list1 = []
        k=0
        for i in words:
            #list2 = []
            s=""
            for j in i:
                #list2.append(dic1[j])
                s+=dic1[j]

  #          list1.append(str(list2))
            list1.append(s)
            #k+=1
        print(list1)

        count=0
        result=[]
        for x in list1:
            if x not in result:
                result.append(x)

        print(len(result))

words= ["gin", "zen", "gig", "msg"]
ls = Solution()
ls.uniqueMorseRepresentations(words)