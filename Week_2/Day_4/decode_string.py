class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)

            elif c == '[':
                stack.append((current_str, k))
                current_str = ""
                k = 0

            elif c == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + num * current_str

            else:
                current_str += c

        return current_str