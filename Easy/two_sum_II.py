"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, 0
        result = []
        while i < len(numbers):
            j = 0
            while j < len(numbers):
                if numbers[i] + numbers[j] == target:
                    result = [i + 1, j + 1]
                    return result
                j += 1
            i += 1
        return result


sol = Solution()
numbers = [-5, -3, 0, 2, 4, 6, 8]
target = 5
testSum = sol.twoSum(numbers, target)
print(testSum)
