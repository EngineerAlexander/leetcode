# Given a string s and a dictionary of strings wordDict, 
# return true if s can be segmented into a space-separated 
# sequence of one or more dictionary words.

# Note that the same word in the dictionary may be 
# reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False]*(length + 1)
        dp[length] = True

        for i in range(length - 1, -1, -1):
            for word in wordDict:
                length_word = len(word)
                if (i + length_word <= length) and (s[i:i + length_word] == word):
                    dp[i] = dp[i + length_word]
                if dp[i]:
                    break
            
        return dp[0]
    
# Time complexity: O(s*w)
# Space complexity: O(s)