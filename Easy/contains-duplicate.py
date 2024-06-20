
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = 0  # used to hold the count of each index of the list ie. if the number 1 appears twice anywhere in the list we will return false
    # start the first index of the list and go until the last index
        j = 0
        nums.sort()
        print(nums.count(nums[-1]))
        min, max = nums[0], nums[-1]
        duplicate = False
        if (len(nums) == 2):
            count = nums.count(nums[j])
            if (count > 1):
                duplicate = True
        for i in range(min, max):
            if (j < len(nums)):
                count = nums.count(nums[j])
            if (count > 1):
                duplicate = True
                break
            j += 1
        return duplicate


testList = [1, 2, 3, 4, 5, 5]
testSolution = Solution()
print(testSolution.containsDuplicate(testList))
