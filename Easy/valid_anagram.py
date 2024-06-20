class Solution:
    """
    Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

    Constraints: s and t consist of lowercase English letters
    """

    def isAnagram(self, s: str, t: str) -> bool:
        i = 0
        if len(s) != len(t):  # if the two strings are the same length we know they cannot be anagrams
            return False
        for item in s:
            if (s[i] not in t or s.count(s[i]) != t.count(s[i])):
                return False  # if the specific letter does not exist or the count of the element in both strings does not match return false
        return True


string1 = "racecar"
string2 = "carrace"

test = Solution()
check_anagram = test.isAnagram(string1, string2)
print(check_anagram)
