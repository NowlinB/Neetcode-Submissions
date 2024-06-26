"""

Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sequences = []
        length = 0
        if len(nums) == 0:
            return 0
        sol = Solution()
        sequence = []
        i, j = 0, 0
        sorted_nums = sol.quicksort(nums)
        sequence.append(sorted_nums[0])
        print(sorted_nums)
        while i < len(sorted_nums) - 1:
            if sorted_nums[i] + 1 == sorted_nums[i + 1]:
                sequence.append(sorted_nums[i + 1])
                j += 1
            elif sequence[j] == sorted_nums[i + 1]:
                print("", end="")
            else:
                sequences.append(sequence)
                sequence = []
                sequence.append(sorted_nums[i + 1])
                j = 0
            i += 1
        sequences.append(sequence)
        i = 0
        for item in sequences:
            if len(sequences[i]) > length:
                length = len(sequences[i])
            i += 1
        print(sequences)
        return length

    def quicksort(self, nums: list[int]) -> list[int]:
        sol = Solution()
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]
            less = [i for i in nums[1:] if i <= pivot]
            greater = [i for i in nums[1:] if i > pivot]
            return sol.quicksort(less) + [pivot] + sol.quicksort(greater)


sol = Solution()
nums = [2, 20, 4, 10, 3, 4, 5]
result = sol.longestConsecutive(nums)
print(result)
