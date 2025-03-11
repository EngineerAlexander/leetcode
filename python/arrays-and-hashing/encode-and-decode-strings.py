# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded 
# back to the original list of strings.
# Constraints:
# strs[i] contains any possible characters out of 256 valid ASCII characters.

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes all sizes first and then all strings.
        """
        res = ""

        num_strings = len(strs)
        for i in range(num_strings):
            string_size = len(strs[i])
            res += "{}".format(string_size)
            if i != (num_strings-1):
                res += ","
            else:
                res += "*"
        
        for i in range(num_strings):
            res += "{}".format(strs[i])

        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        split_string = s.split("*")
        sizes_string = split_string[0]

        all_sizes = []
        cur_str = ""
        cur_str_index = 0
        for i in range(len(sizes_string)):
            char = sizes_string[i]
            if (char != ","):
                cur_str += char
            else:
                all_sizes.append(int(cur_str))
                cur_str = ""
                cur_str_index += 1

            if (i == (len(sizes_string) - 1)):
                all_sizes.append(int(cur_str))
                cur_str = ""
                cur_str_index += 1
            
        end_size_index = i + 2

        res = []
        cur_str_start = end_size_index
        for i in range(len(all_sizes)):
            cur_size = all_sizes[i]
            cur_string = s[cur_str_start:cur_str_start+cur_size]
            res.append(cur_string)
            cur_str_start += cur_size
        
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# Time complexity: O(n), n is the number of strings
# Space complexity: O(n), n is the number of strings