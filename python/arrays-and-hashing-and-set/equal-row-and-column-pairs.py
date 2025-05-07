# Given a 0-indexed n x n integer matrix grid, 
# return the number of pairs (ri, cj) such that 
# row ri and column cj are equal.

# A row and column pair is considered equal if 
# they contain the same elements in the same 
# order (i.e., an equal array).

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = {}

        R = len(grid)
        C = len(grid[0])

        pairs = 0

        # put in rows
        for r in range(R):
            row = grid[r]
            s = []
            for char in row:
                s.append(str(char))
            s = ",".join(s)

            if s in freq:
                freq[s] += 1
            else:
                freq[s] = 1

        # calculate pairs with each column
        for c in range(C):
            s = []
            for r in range(R):
                s.append(str(grid[r][c]))
            s = ",".join(s)

            if s in freq:
                pairs += freq[s]

        return pairs
    
# Time complexity: O(n^2) We iterate over each row and column only once, 
# converting one array of length n into a hashable object takes O(n) time.
# Space complexity: O(n^2) We store each row of the grid in the hash map, 
# in the worst-case scenario, row_counter might contains n distinct rows of length n.