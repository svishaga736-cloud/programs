class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Current ')' is a mismatch, use it as a new base
                    stack.append(i)
                else:
                    # Valid length is current index minus the index 
                    # before the start of this valid sequence
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
