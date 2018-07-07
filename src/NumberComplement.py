class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num1 = list(bin(num))
        print("before changed", type(num1))
        output=[]
        for i in range(len(num1)):
            if(num1[i]=='1'):
                output.append(0)
            elif(num1[i]=='0'):
                output.append(1)
            else:
                output.append(num1[i])

        output = output[2:]
        print("changed", output)
        newStr=''.join(str(x) for x in output)
        print("changed str", newStr)
        #newInt = int(newStr)
        numDecimal = int(newStr, 2)
        return numDecimal
        '''
        newvalue=str(output)
        num11, num12 = newvalue.split('b')
        print("num11 ",num11)
        print("num12 ", num12)
        print("num12 type ", type(num12))
        num12 = int(num12)
        print("num12 type ", type(num12))
        num12 = ~num12
        print(num12)
        print(type(num_convert2))
        num_convert2 = int(num_convert2, 2)
        '''
        return num_convert

x=5

ls = Solution()
var=ls.findComplement(x)
print(var)