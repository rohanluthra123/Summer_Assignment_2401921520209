class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled = s + s
        trimmed = doubled[1:-1]
        return s in trimmed