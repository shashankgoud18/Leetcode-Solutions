class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        
        def possible(capacity):
            count = 1
            weight_sum = 0
            for weight in weights:
                if weight_sum + weight <= capacity:
                    
                    weight_sum += weight
                else:
                    weight_sum = 0
                    count += 1
                    weight_sum += weight
            
            return count <= days

        low = max(weights)
        high = sum(weights)

        while low<high:
            mid = low + (high-low)//2
            if possible(mid):
                high = mid
            else:
                low = mid + 1
        return low

        
                