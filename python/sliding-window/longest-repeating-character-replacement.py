# You are given a string s and an integer k. You can choose any character 
# of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter 
# you can get after performing the above operations.

# Constraints:
# s consists of only uppercase English letters.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        c_frequency = {}
        longest_str_len = 0
        for r in range(len(s)):
            c_frequency[s[r]] = c_frequency.get(s[r], 0) + 1
            
            # Replacements cost = cells count between left and right - highest frequency
            cells_count = r - l + 1
            if cells_count - max(c_frequency.values()) <= k:
                longest_str_len = max(longest_str_len, cells_count)
                
            else:
                c_frequency[s[l]] -= 1
                if not c_frequency[s[l]]:
                    del c_frequency[s[l]]
                l += 1
        
        return longest_str_len
    
# Time complexity: O(n)
# Space complexity: O(1) because we have a fixed number of characters.
