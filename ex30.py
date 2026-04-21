from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        res = []
        
        # We only need to start from 0 up to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            count = 0
            
            while right + word_len <= len(s):
                # Extract word from the right
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    count += 1
                    
                    # If word frequency exceeds what's required, shrink from left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # If all words matched
                    if count == num_words:
                        res.append(left)
                else:
                    # Invalid word: reset the window
                    current_count.clear()
                    count = 0
                    left = right
                    
        return res
