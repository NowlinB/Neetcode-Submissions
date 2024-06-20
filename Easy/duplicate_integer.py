class Solution:
    def hasDuplicate(self, nums: list) -> bool:
        i, j = 0, 0
        subList = nums[i+1:len(nums)]
        while len(subList) != 0:
            first = nums[i]
            subList = nums[i+1:len(nums)]
            if (first in subList):
                return True
            i += 1
        return False


testList = [1, 2, 3, 1, 4]
test = Solution()
checkDuplicate = test.hasDuplicate(testList)
print(checkDuplicate)
