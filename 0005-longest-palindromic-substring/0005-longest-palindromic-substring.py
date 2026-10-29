class Solution:
    def longestPalindrome(self, s: str) -> str:
        # n = len(s)

        # mid = n//2
        # if n%2==0:
        #     left = mid-1
        #     right = mid
        # else:
        #     left = mid-1
        #     right = mid + 1

        # result = ''
        # while right < n and left>=0:
        #     if s[left] == s[right]:
        #         if len(result) < right-left+1:
        #             result = s[left:right+1]
        #     right += 1 
        #     left -= 1
        
        # return result


        n = len(s)
        result = ''
        for i in range(n):
            left = i
            right = i+1
            while left>=0 and right<n and s[left] == s[right]:
                if len(result) < right -left +1:
                    result = s[left:right+1]
                left -= 1 
                right +=1 

            left = i
            right = i
            while left>=0 and right<n and s[left] == s[right]:
                if len(result) < right -left +1:
                    result = s[left:right+1]
                left -= 1 
                right +=1

            
        return result

            