class Solution:

    def countAndSay(self, n):
        st = '1'
        for _ in range(n - 1):
            st = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), st)
        return st
