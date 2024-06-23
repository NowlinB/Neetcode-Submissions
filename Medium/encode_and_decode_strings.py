class Solution:
    """Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings."""
    def encode(self, strs: list[str]) -> str:
        i = 0  # used as a counter to determine when we have reached the last element of the list
        encoded_string = ""
        if (len(strs) == 0):
            return strs
        for s in strs:
            # we know that we've reached the last element if i == (len(strs) - 1)
            if (i == (len(strs)-1)):  # prevent adding an additional empty '' element into our list
                encoded_string += s
            else:
                encoded_string += s + "-"  # I am using the "-" as a delimiter
            i += 1
        return encoded_string

    def decode(self, s: str) -> list[str]:
        strs = []
        if (s == ""):  # if the string contains only an empty string we still want to return a list containing the empty string
            strs.append("")
        if (len(s) > 0):  # otherwise split the string into a list by the "-" delimiter
            strs = s.split("-")
        return strs


testSolution = Solution()
testList = ["neet", "code", "love", "you"]
testEncode = testSolution.encode(testList)
testDecode = testSolution.decode(testEncode)
print(testEncode)
print(testDecode)
