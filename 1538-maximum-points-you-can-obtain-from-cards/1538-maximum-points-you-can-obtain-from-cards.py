class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = 0
        right_sum = 0
        n = len(cardPoints)
        if len(cardPoints) == k:
            return sum(cardPoints)

        for i in range(k):
            left_sum += cardPoints[i]

        maximum = left_sum
        right_index = n - 1

        for i in range(k-1,-1,-1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_index]
            maximum = max(maximum, left_sum+right_sum)
            right_index -= 1
        
        return maximum


