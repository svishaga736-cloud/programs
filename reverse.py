class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define 32-bit signed integer boundaries
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        
        # Handle sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x != 0:
            # Pop the last digit
            digit = x % 10
            x //= 10
            
            # Build the reversed number
            res = res * 10 + digit
            
        # Apply sign and check overflow
        res *= sign
        if res < MIN_INT or res > MAX_INT:
            return 0
            
        return res
