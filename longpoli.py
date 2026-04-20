class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # Odd length palindromes (like "aba")
            p1 = self.expand(s, i, i)
            if len(p1) > len(res): res = p1
            
            # Even length palindromes (like "abba")
            p2 = self.expand(s, i, i + 1)
            if len(p2) > len(res): res = p2
        return res

    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
