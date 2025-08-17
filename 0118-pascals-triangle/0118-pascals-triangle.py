class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]

        while len(result)<numRows:
             row = [1]
             prev = result[-1]
             i = 0
             j = 1
             while j < len(prev):
                sum = prev[i] + prev[j]
                row.append(sum)
                i+=1
                j+=1

             row.append(1)
             result.append(row)
        return result