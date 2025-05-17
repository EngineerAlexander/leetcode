# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# Constraints: All lowercase English letters.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Categorize by sorted string"""
        sorted_map = {}
        for cur in strs:
            sorted_string = "".join(sorted(cur))
            if sorted_string in sorted_map:
                sorted_map[sorted_string].append(cur)
            else:
                sorted_map[sorted_string] = [cur]

        res = []
        for key in sorted_map:
            res.append(sorted_map[key])

        return res

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Categorize by count"""
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
    
# Complexity Analysis First Solution
# Time complexity: O(nslog(s)), n is the length of strs, s is the max length of a str in strs
# Space complexity: O(ns), the size of res
    
# Complexity Analysis Second Solution
# Time complexity: O(ns), n is the length of strs, s is the max length of a str in strs
# Space complexity: O(ns), the size of res