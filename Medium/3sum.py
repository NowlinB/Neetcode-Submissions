"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i, j, k = 0, 0, 0

        sums = []
        while i < len(nums):
            j = 0
            while j < len(nums):
                k = 0
                while k < len(nums):
                    if (
                        (nums[i] + nums[j] + nums[k] == 0)
                        and (i != j)
                        and (j != k)
                        and (i != k)
                    ):
                        sum = [nums[i], nums[j], nums[k]]
                        sum.sort()
                        if sum not in sums:
                            sums.append(sum)
                    k += 1
                j += 1
            i += 1
        return sums


sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
testSum = sol.threeSum(nums)
print(testSum)
