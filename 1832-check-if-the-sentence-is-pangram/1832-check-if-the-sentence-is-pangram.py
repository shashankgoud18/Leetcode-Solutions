class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        n = len(sentence)
        result = [False]*26

        for ch in sentence:
            index = ord(ch) - ord('a')
            result[index] = True
        
        for check in result:
            if check == False:
                return False
        
        return True