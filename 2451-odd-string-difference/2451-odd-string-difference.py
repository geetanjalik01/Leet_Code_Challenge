class Solution:
    def oddString(self, words: List[str]) -> str:
        def pattern(word):
            return tuple(ord(word[i]) - ord(word[i - 1]) for i in range(1, len(word)))

        patterns = {}
        
        for word in words:
            p = pattern(word)
            patterns[p] = patterns.get(p, 0) + 1

        for word in words:
            if patterns[pattern(word)] == 1:
                return word
