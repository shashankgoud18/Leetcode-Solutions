class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in "({[":           # opening bracket
                stack.append(ch)
            else:                     # closing bracket
                if not stack:         # stack empty → no match
                    return False
                if stack[-1] != pairs[ch]:  # top doesn’t match
                    return False
                stack.pop()           # matched → pop

        return len(stack) == 0 