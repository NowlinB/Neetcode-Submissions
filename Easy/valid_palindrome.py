"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatString = "" #used to store the formatted string with no spaces, no punctuation, and no numbers
        stringAsList = s.lower().split()
        formatWithNums = "" #used to store the formatted string with no spaces, and no punctuation
        for each in stringAsList:
            for c in each:
                if c.isalpha():
                    formatString += c
                if c.isalnum():
                    formatWithNums += c
        print(formatString)
        print(formatWithNums)
        if formatString == formatWithNums[::-1]:
            return True
        return False


sol = Solution()
s = "0P"
test = sol.isPalindrome(s)
print(test)
