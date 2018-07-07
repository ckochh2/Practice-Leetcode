import math
matrix = [[41,45],[81,41],[73,81],[47,73],[0,47],[79,76]]

row = len(matrix)
print(math.floor(row/2))
col = len(matrix[0])
b = True
for i in range(row):
    for j in range(col):
        temp = matrix[i][j]
        k = i
        while (k< row-1 and j < col-1):
            if (matrix[k + 1][j + 1] == temp):
                b = True
            else:
                b = False
                break
            j += 1
            k += 1
        if(b==False):
            break

print(b)