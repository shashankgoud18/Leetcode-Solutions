class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        freq = {}
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                key = i+j
                if key in freq:
                    freq[key].append(mat[i][j])
                else:
                    freq[key] = [mat[i][j]]

        result = []
        flag = False
        for key,val in freq.items():
            if flag:
                result.extend(val)
            else:
                result.extend(val[::-1])
            
            flag = not flag
        return result
