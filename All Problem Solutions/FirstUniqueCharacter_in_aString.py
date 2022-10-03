from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch_count = Counter(s)
        for i in range(len(s)):
            if ch_count[s[i]] == 1:
                return i
        return -1