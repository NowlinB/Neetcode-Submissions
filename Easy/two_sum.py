class Solution:
    """
    Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
    We assume that every input has exactly one pair of indices i and j that satisfy the condition.
    Returns the answer with the smaller index first. 
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i, j = 1, 0
        # while j is less than the length of nums we know we haven't check every element in nums
        while j <= len(nums):
            i = j+1
            for item in nums:
                # if i == len(nums) than we have checked every element for list[j] amd have not found a match
                if (i == len(nums)):
                    break
                first = nums[j]
                second = nums[i]
                if ((first+second) == target):
                    return [j, i]
                i += 1
            j += 1
        return "-1"


nums = [2, 3, 5, 5]
target = 10
testSolution = Solution()
testSum = testSolution.twoSum(nums, target)
print(testSum)
