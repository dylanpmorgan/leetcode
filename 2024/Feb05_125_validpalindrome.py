"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include 
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""

test_cases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " ",
]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lower case
        s = s.lower()
        # remove alpha numeric characters
        s = [s_i for s_i in s if s_i.isalnum()]
        return True if "".join(s) == "".join(s[::-1]) else False
    
sol = Solution()

for test_case in test_cases:
    print(f"{test_case}", "-", sol.isPalindrome(test_case))

"""
ACCEPTED 
    Runtime
    36ms
    Beats 95.16% of users with Python3

    Memory
    17.82MB
    Beats 44.97% of users with Python3
"""