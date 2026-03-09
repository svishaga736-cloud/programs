class Solution {
public:
    string reverseWords(string s) {
        // Step 1: Reverse the entire string
        reverse(s.begin(), s.end());

        int n = s.size();
        int idx = 0; 

        for (int start = 0; start < n; ++start) {
            if (s[start] != ' ') {
                // Add a single space before the word (but not for the first word)
                if (idx != 0) s[idx++] = ' '; 

                int end = start;
                // Move the word to the front to handle extra spaces
                while (end < n && s[end] != ' ') {
                    s[idx++] = s[end++];
                }

                // Reverse the current word back to original spelling
                reverse(s.begin() + idx - (end - start), s.begin() + idx);
                
                // Move 'start' pointer to the end of the processed word
                start = end;
            }
        }
        
        // Trim the remaining characters from the end
        s.erase(s.begin() + idx, s.end());
        return s;
    }
};
