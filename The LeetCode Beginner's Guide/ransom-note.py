
# https://leetcode.com/problems/ransom-note/
# Time complexity O(m)
# Space complexity O(k)/ O(1)/ O(26) --> number of char

import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
        
