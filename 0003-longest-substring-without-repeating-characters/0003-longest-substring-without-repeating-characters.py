class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 256 
        left = 0
        max_len = 0

        for right in range(len(s)):
            if last_seen[ord(s[right])] != -1:
                left = max(left, last_seen[ord(s[right])] + 1)

            last_seen[ord(s[right])] = right
            max_len = max(max_len, right - left + 1)

        return max_len