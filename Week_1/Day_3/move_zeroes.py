class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert = 0

        for num in nums:
            if num != 0:
                nums[insert] = num
                insert += 1

        for i in range(insert, len(nums)):
            nums[i] = 0