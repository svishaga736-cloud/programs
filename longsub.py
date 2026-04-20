class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            # Check if char is in the current window
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            
            char_map[s[end]] = end
            current_window_size = end - start + 1
            if current_window_size > max_length:
                max_length = current_window_size

        return max_length
