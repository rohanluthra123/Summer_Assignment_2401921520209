class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        p_count = {}
        window = {}
        result = []

        for c in p:
            p_count[c] = p_count.get(c, 0) + 1

        k = len(p)

        for i in range(len(s)):
            c = s[i]
            window[c] = window.get(c, 0) + 1

            if i >= k:
                out = s[i - k]
                window[out] -= 1
                if window[out] == 0:
                    del window[out]

            if window == p_count:
                result.append(i - k + 1)

        return result