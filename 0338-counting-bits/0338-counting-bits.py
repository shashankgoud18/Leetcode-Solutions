class Solution:
    def countBits(self, n: int) -> List[int]:
        # result = []
        # for i in range(0,n+1):
        #     result.append(i.bit_count())
        # return result

        result = [0]*(n+1)
        for i in range(1,n+1):
            if(i%2 != 0):
                result[i] = result[i//2] + 1
            else:
                result[i] = result[i//2]
            
        return result