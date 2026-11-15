class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        
        i,j = 0,0
        m = len(firstList)
        n = len(secondList)
        result = []

        while i<m and j<n:
            maxi = max(firstList[i][0],secondList[j][0])
            mini = min(firstList[i][1],secondList[j][1])

            intersection = [maxi,mini]

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1 
            
            if maxi<= mini:
                result.append(intersection)

        return result


