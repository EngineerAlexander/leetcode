# Design a data structure that supports adding new words and 
# finding if a string matches any previously added string.
# Implement the WordDictionary class:
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure 
# that matches word or false otherwise. word may contain dots '.' where dots 
# can be matched with any letter.

# Constraints:
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['$'] = {}
        # Time complexity: O(n) for adding a word
        # Space complexity: O(n) for the trie

    def search(self, word: str) -> bool:
        def search_subword(word, cur):
            for i, char in enumerate(word):
                if char not in cur:
                    # search all substrings
                    if char == ".":
                        for x in cur:
                            if (x != "$") and search_subword(word[i+1:], cur[x]):
                                return True
                    return False
                else:
                    cur = cur[char]
            return "$" in cur

        return search_subword(word, self.trie)
        # Time complexity: O(m) for searching a word (since we have at most 2 dots)
        # Space complexity: O(n) for the trie

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)