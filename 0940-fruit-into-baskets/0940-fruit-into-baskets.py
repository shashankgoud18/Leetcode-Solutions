class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        n = len(fruits)
        maximum = 0
        my_dict = {}
        while right < n:
            if fruits[right] in my_dict:
                my_dict[fruits[right]] += 1
            else:
                my_dict[fruits[right]] = 1
            
            if len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1
                
            if len(my_dict) <= 2:
                maximum = max(maximum, right-left + 1)
            right += 1
        
        return maximum