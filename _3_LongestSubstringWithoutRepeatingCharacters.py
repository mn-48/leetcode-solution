class Solution:
    def lengthOfLongestSubstring(self, s):
        previous, ans, last = {}, 0, -1
        for index, element in enumerate(s):
            #to know enumerate() see the link : https://www.youtube.com/watch?v=bOGmYvtw-kk
            last = max(previous.get(element, -1), last)
            ##to know xyz.get() see the link : https://www.youtube.com/watch?v=y4LXXpekUxs
            ans = max(ans, index - last)
            previous[element] = index
        return ans
#obj = Solution()
#print(obj.lengthOfLongestSubstring("abcabcbb"))
