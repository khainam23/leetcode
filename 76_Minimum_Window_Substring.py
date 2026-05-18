'''
Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

 

Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.

'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have = 0
        res = [-1, -1]
        resLen = float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in countT:
                countT[c] -= 1
                if countT[c] == 0:
                    have += 1

            while have == len(countT):
                # update our result
                length = r - l + 1
                if length < resLen:
                    res = [l, r]
                    resLen = length
                # pop from the left of our window
                if s[l] in countT:
                    countT[s[l]] += 1
                    if countT[s[l]] > 0:
                        have -= 1
                l += 1

        if resLen == float("inf"):
            return ""
        
        return s[res[0]: res[1] + 1]

from TestCase import TestCase

test_case = TestCase()
test_case.test_case([
    [Solution().minWindow("ADOBECODEBANC", "ABC"), "BANC"],
    [Solution().minWindow("a", "a"), "a"],
    [Solution().minWindow("a", "aa"), ""],
])