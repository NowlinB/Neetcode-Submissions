"""
min(max(L),max(R)) - height[i]
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) == 0:
            return 0
        area = 0
        i, j = (
            0,
            len(height) - 1,
        )  # i is used for the left index and j is used for the right index
        l_max, r_max = 0, 0  # will store the final left and right max
        left, right = 0, 0  # used to store the current left and right values
        i = 0
        while i < j:
            left = height[i]
            l_max = max(l_max, left)  # if left > l_max then left = l_max
            right = height[j]
            r_max = max(r_max, right)  # if right > r_max then r_max = right
            if left < l_max:
                area += l_max - left
            if right < r_max:
                area += r_max - right
            if r_max > l_max:
                i += 1
            else:
                j -= 1
        return area


sol = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = sol.trap(height)
print(result)
