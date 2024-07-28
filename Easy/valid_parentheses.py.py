"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
"""

LEFT = ["(", "[", "{"]
RIGHT = [")", "]", "}"]


class Solution:
    def isValid(self, s: str) -> bool:
        if (
            len(s) == 0 or len(s) == 1 or len(s) % 2 != 0
        ):  # given the conditions a valid length is a length > 2 and that is even
            return False
        i = 0
        values_seen = []
        left_count, right_count = 0, 0
        while i < len(s):
            values_seen.append(s[i])
            if (
                s[i] == ")" and "(" not in values_seen
            ):  # we must see the left before the right to form a valid pair
                return False
            if s[i] == "]" and "[" not in values_seen:
                return False
            if s[i] == "}" and "{" not in values_seen:
                return False
            distance = len(s) - 1 - i
            if i < len(s) - 1:  # prevent i+1 error when i == len(s)-1
                if s[i] == "(":
                    left_count += 1
                    if s[i + 1] != ")" and s[distance] != ")" and s[distance] in RIGHT:
                        return False
                if s[i] == "[":
                    left_count += 1
                    if s[i + 1] != "]" and s[distance] != "]" and s[distance] in RIGHT:
                        return False
                if s[i] == "{":
                    left_count += 1
                    if s[i + 1] != "}" and s[distance] != "}" and s[distance] in RIGHT:
                        return False
                if s[i] not in LEFT and s[i] not in RIGHT:  # value not acceptable
                    return False
            if s[i] in RIGHT:
                right_count += 1
            i += 1
        if left_count != right_count:
            return False
        return True


s = "([])"
sol = Solution()
result = sol.isValid(s)
print(result)
