def cyclicRotate(input,k):
    # slice list in two parts and append
    # last element in front of sliced list

    # [input[-1]] --> converts last element pf array into list
    # to append in front of sliced list

    # input[0:-1] --> list of elements except last element
    #print([input[-1]] + input[0:-1])


    '''
    print(input[-1])
    for i in range(k):
        temp=input[-1]
        input.insert(0,temp)
        del(input[len(input)-1])
    '''

    newA = [None] * len(input)
    for i in range(0, len(input)):
        newnum = (i + k) % len(input)
        newA[newnum] = input[i]
    for i in range(len(input)):
        input[i] = newA[i]
    print(input)

# Driver program
if __name__ == "__main__":
    input = [1, 2, 3, 4, 5]
    k=3
    cyclicRotate(input,k)