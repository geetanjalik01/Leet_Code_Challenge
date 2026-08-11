class Solution:
    def findSubstring(self, s, words):
        n = len(words[0])
        total = n * len(words)
        required = Counter(words)
        ans = []

        for i in range(len(s) - total + 1):
            part = s[i:i + total]

            current = [
                part[j:j + n]
                for j in range(0, total, n)
            ]

            if Counter(current) == required:
                ans.append(i)

        return ans