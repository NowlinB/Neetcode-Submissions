"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.
"""


class Solution():
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if (len(nums) < 2):
            return nums
        map = {}  # a dictionary that uses each unique key and maps the key to the count of occurences in the nums list
        count = 0  # keeps track of the current count of the element we are currently counting
        i = 0
        top = []  # used to store k number of the highest frequently occuring elements
        while i < len(nums):
            # represents the current index we are actively determining the count of
            currentIndex = nums[i]
            count = 0
            j = 0
            for j in range(0, len(nums)):
                if (currentIndex == nums[j]):
                    count += 1
                    j += 1
            # we must store the key as a string represntation
            map.update({str(currentIndex): count})
            i += 1
        sorted_map = {k: v for k, v in sorted(
            map.items(), key=lambda item: item[1])}  # sorts the key:value pairs in the map by their value from lowest to highest
        i = 0
        keys = list(sorted_map.keys())  # get the keys from the sorted map
        while i < k:
            if (i < len(keys)):
                # append the most frequent values k # of times
                top.append(int(keys[-1-i]))
            i += 1
        top.reverse()  # reverse elements so that the list is in ascending order
        return top


sol = Solution()
nums = [1, 2]
k = 2
result = sol.topKFrequent(nums, k)
print(result)
