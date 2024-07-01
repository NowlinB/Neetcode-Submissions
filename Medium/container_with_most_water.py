class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i, j = 0, len(heights) - 1
        currentArea, area = 0, 0
        while i < len(heights):
            j = len(heights) - 1
            while j > 0:
                height1 = heights[i]
                height2 = heights[j]
                if height2 > height1:
                    height = height1
                else:
                    height = height2
                length = j - i
                currentArea = height * length
                if currentArea > area:
                    area = currentArea
                j -= 1
            i += 1
        return area


sol = Solution()
heights = [1, 7, 2, 5, 4, 7, 3, 6]
result = sol.maxArea(heights)
print(result)
