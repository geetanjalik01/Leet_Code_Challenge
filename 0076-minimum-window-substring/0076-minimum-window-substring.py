from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        have = {}
        
        required = len(need)
        formed = 0
        
        left = 0
        ans = ""
        
        for right in range(len(s)):
            ch = s[right]
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] == need[ch]:
                formed += 1

            while formed == required:
                window = s[left:right + 1]

                if ans == "" or len(window) < len(ans):
                    ans = window

                left_ch = s[left]
                have[left_ch] -= 1

                if left_ch in need and have[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        return ans