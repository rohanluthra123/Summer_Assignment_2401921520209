class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            l_sq = nums[left] ** 2
            r_sq = nums[right] ** 2

            if l_sq > r_sq:
                result[pos] = l_sq
                left += 1
            else:
                result[pos] = r_sq
                right -= 1

            pos -= 1

        return result