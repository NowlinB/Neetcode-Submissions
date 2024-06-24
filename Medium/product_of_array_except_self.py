"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer. 
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        i, j = 0, 0
        product = 1  # stores the current product
        products = []  # stores the list of products
        while i < len(nums):
            j = 0
            product = 1
            while j < len(nums):
                if j != i: #prevent multiply the product of nums[i]
                    product *= nums[j]
                j += 1
            i += 1
            products.append(product)
        return products


sol = Solution()
nums = [-1, 0, 1, 2, 3]
testProduct = sol.productExceptSelf(nums)
print(testProduct)
