# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.
# Constraints:
# k is in the range [1, the number of unique elements in the array]
# It is guaranteed that the answer is unique.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # get frequeny map
        freq_map = {}
        for num in nums:
            if num in freq_map.keys():
                freq_map[num] = freq_map[num] + 1
            else:
                freq_map[num] = 1


        # get all frequencies and sort
        frequency_list = []
        for val in freq_map.values():
            frequency_list.append(val)
        
        frequency_list.sort(reverse = True)
        valid_frequencies = frequency_list[0:k]

        # assemble results
        results = []
        for val, freq in freq_map.items():
            if freq in valid_frequencies:
                results.append(val)

        pass
        return results
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # get frequeny map
        freq_map = {}
        for num in nums:
            if num in freq_map.keys():
                freq_map[num] = freq_map[num] + 1
            else:
                freq_map[num] = 1


        # since we are guaranteed a unique answer, we can add values based
        # on frequency to an array, then answer is last k indexes of array
        freq_array = [[] for i in range(len(nums) + 1)]
        for val, freq in freq_map.items():
            freq_array[freq].append(val)

        # obtain results
        res = []
        for i in range(len(freq_array) - 1, -1, -1):
            for n in freq_array[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
# Complexity Analysis First Solution
# Time complexity: O(nlog(n)), because of the sort
# Space complexity: O(n)
                
# Complexity Analysis Second Solution
# Time complexity: O(n), only interate through nums, freq_array prop to nums
# Space complexity: O(n)