class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = 0
        low = 1 
        high = max(piles)

        while low<=high:
            mid = (low+high)//2

            k = mid 
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k-1)//k
            
            if total_hours<= h:
                ans = mid
                high = mid-1
            else:
                low = mid + 1 
        
        return ans
