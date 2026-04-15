class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Expand Around Center (中央展開法)

        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        result = ""
        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i+1)
            if len(odd) > len(result): result = odd
            if len(even) > len(result): result = even

        return result

