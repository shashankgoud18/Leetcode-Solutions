class Solution(object):
    char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
    }

    def solve(self,index,subset,digits,result):
        if index >= len(digits):
            result.append("".join(subset))
            return
        for char in self.char_map[digits[index]]:
            subset.append(char)
            self.solve(index+1,subset,digits,result)
            subset.pop()


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        result =[]
        self.solve(0,[],digits,result)
        return result