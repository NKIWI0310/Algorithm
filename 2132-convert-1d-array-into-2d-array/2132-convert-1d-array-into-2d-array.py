class Solution(object):
    def construct2DArray(self, original, m, n):
        newArr = [[0 for _ in range(n)] for _ in range(m)]

        idx = 0 

        if len(original) != m * n:
            newArr = []
        else: 
            for i in range(m):
                for j in range(n):
                    newArr[i][j] = original[idx]
                    idx+=1

        return newArr