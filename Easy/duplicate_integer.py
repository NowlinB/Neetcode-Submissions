class Solution:
    """
    Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
    """

    def hasDuplicate(self, nums: list) -> bool:
        i, j = 0, 0
        # The sublist is used to check if a given element exists somewhere else in the list
        subList = nums[i+1:len(nums)]
        while len(subList) != 0:
            first = nums[i]
            subList = nums[i+1:len(nums)]
            if (first in subList):  # if the given index exists in the sublist than we know that the list does infact contain a duplicate
                return True
            i += 1
        return False


testList = [1, 2, 3, 1, 4]
test = Solution()
checkDuplicate = test.hasDuplicate(testList)
print(checkDuplicate)
