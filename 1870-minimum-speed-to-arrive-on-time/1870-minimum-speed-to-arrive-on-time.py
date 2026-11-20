import math
class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        n = len(dist)
        low = 1
        high = 10**7
        mini_speed = -1
        while low<=high:
            mid = low + (high-low)//2
            summ = 0
            for i in range(n):
                distance = dist[i]
                if i == n-1:
                    summ += distance/mid
                    continue
                summ += math.ceil(distance/mid)
                
            if summ <= hour:
                mini_speed = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return mini_speed