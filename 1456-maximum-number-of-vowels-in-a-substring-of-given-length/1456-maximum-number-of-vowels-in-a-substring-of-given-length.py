class Solution: 
    def maxVowels(self, s: str, k: int) -> int:
        
        #Brute Force
        # vowels = ['a','e','i','o','u']
        # n = len(s)
        # max_vowels = 0

        # for i in range(n):
        #     count = 0
        #     for j in range(i,n):
        #         if s[j] in vowels:
        #             count += 1 
        #         if j-i+1 ==k:
        #             max_vowels = max(count,max_vowels)
        #             break
        
        # return max_vowels


        left = 0
        right = 0
        n = len(s)
        max_vowels = 0
        vowels = ['a','e','i','o','u']
        count = 0
        while right < n:
            
            if s[right] in vowels:
                count += 1 

            if right-left+1 >k:
                if s[left] in vowels:
                    count -= 1
                left += 1 
            
            if right-left+1 == k:
                max_vowels = max(max_vowels,count)

            right += 1 

        return max_vowels

                 



