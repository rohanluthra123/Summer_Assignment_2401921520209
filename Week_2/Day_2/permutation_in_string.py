class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window = {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        k = len(s1)

        for i in range(len(s2)):
            c = s2[i]
            window[c] = window.get(c, 0) + 1

            if i >= k:
                out = s2[i - k]
                window[out] -= 1
                if window[out] == 0:
                    del window[out]

            if window == s1_count:
                return True

        return False