# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from 
# products after each character of searchWord is typed. Suggested 
# products should have common prefix with searchWord. If there are 
# more than three products with a common prefix return the three 
# lexicographically minimums products.

# Return a list of lists of the suggested products after each 
# character of searchWord is typed.

# Constraints:
# All the strings of products are unique.
# All the strings contain only lowercase English letters.

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node = self.root
        
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c] 
            if node.n < 3:
                node.words.append(word)
                node.n += 1
        
    def find_word_by_prefix(self, c):
        if self.node and c in self.node.children: 
            self.node = self.node.children[c] 
            return self.node.words
        else: 
            self.node = None    
            return []
            
            
class Solution:
    def suggestedProducts(self, A: List[str], searchWord: str) -> List[List[str]]:
        A.sort()
        trie = Trie()
        for word in A: trie.add_word(word)
        return [trie.find_word_by_prefix(c) for c in searchWord]
    
# Time complexity: O(n * m) where n is the number of products and m is the length of the longest product name
# Space complexity: O(n * m) for the trie