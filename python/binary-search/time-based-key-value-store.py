# Design a time-based key-value data structure that can store multiple values 
# for the same key at different time stamps and retrieve the key's value at a 
# certain timestamp.
# Implement the TimeMap class:
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with 
# the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was 
# called previously, with timestamp_prev <= timestamp. If there are multiple 
# such values, it returns the value associated with the largest timestamp_prev. 
# If there are no values, it returns "".
# Constraints:
# key and value consist of lowercase English letters and digits.
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.

class TimeMap:

    def __init__(self):
        # key -> list of sets (timestamp, value)
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        cur_set = (timestamp, value)
        if key in self.map:
            self.map[key].append(cur_set)
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            time_series = self.map[key]
            if time_series[0][0] > timestamp:
                return ""
        else:
            return ""

        low = 0
        high = len(time_series) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_timestamp = time_series[mid][0]
            mid_value = time_series[mid][1]

            if mid_timestamp == timestamp:
                return mid_value

            # if we are at a timestamp greater than given, we need to shift left
            elif mid_timestamp > timestamp:
                high = mid - 1

            # if we are at a timestamp less than given, we could be at solution or too left
            else:
                low = mid + 1

        if high >= 0:
            return time_series[mid][1]
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)