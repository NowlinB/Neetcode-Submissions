"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        i, j, = 0, 1
        if (len(strs) < 2):
            return [strs]
        inAnagram = False
        mySolution = Solution()
        anagrams = []
        while i != len(strs):
            j = 0
            tempList = []
            for sublist in strs:
                if (j == len(strs)):
                    break
                firstIndex = strs.index(strs[i])
                secondIndex = strs.index(strs[j])
                first = strs[firstIndex]
                second = strs[secondIndex]
                # check if current first and second element are valid anagrams of each other
                result = mySolution.isAnagram(first, second)
                if (result):
                    # check if first is already in the anagrams list
                    inAnagram = mySolution.checkInAnagramList(first, anagrams)
                    # if two elements are exactly the same they are anagrams of each other
                    if (first == second and not inAnagram):
                        tempList.append(first)
                    if (not inAnagram):
                        inTempList = mySolution.checkInAnagramList(
                            first, tempList)
                        if not inTempList:
                            # only append first if it is not in both the anagram and tempList
                            tempList.append(first)
                    # check if second is already in the anagrams list
                    inAnagram = mySolution.checkInAnagramList(second, anagrams)
                    if not inAnagram:
                        inTempList = mySolution.checkInAnagramList(
                            second, tempList)
                        if not inTempList:  # only append second if it is not in the anagram or tempList
                            tempList.append(second)
                j += 1
            if (len(tempList) > 0):  # prevent empty tempLists from being appended into anagrams
                anagrams.append(tempList)
            i += 1
        return anagrams

    # used to check if two strings are valid anagrams of each other
    def isAnagram(self, first: str, second: str) -> bool:
        i = 0
        if len(first) != len(second):
            return False
        for item in first:
            if (first[i] not in second or first.count(first[i]) != second.count(first[i])):
                return False
            i += 1
        return True

    # used to check if a given anagram already exists in the list of anagrams
    def checkInAnagramList(self, first: str, anagrams: list) -> bool:
        for sublist in anagrams:
            if (first in sublist):
                return True
        return False


testSolution = Solution()
testStrings = ["buy", "sid", "dis", "sid", "buy"]
checkAnagram = testSolution.groupAnagrams(testStrings)
print(checkAnagram)
