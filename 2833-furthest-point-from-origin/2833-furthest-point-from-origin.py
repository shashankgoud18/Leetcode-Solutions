class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # count = 0
        # for move in moves:
        #     if move == 'L':
        #         count -= 1 
        #     elif move == 'R':
        #         count += 1 
        #     elif move == "_":
        #         if count <= 0:
        #             count -= 1 
        #         else:
        #             count += 1 
        
        # return abs(count)


        left = 0
        right = 0
        blank = 0
        for move in moves:
            if move == 'L':
                left += 1 
            elif move == 'R':
                right += 1 
            else:
                blank += 1 
        
        return abs(right-left) + blank