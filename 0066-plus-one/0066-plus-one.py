class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        integer = 0
        for num in digits:
            integer = integer*10 + int(num)
        
        integer += 1 

        lst = [int(d) for d in str(integer)]
        return lst