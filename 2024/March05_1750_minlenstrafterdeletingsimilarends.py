"""
1750. Minimum Length of String After Deleting Similar Ends

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following
algorithm on the string any number of times:
    Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
    Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
    The prefix and the suffix should not intersect at any index.
    The characters from the prefix and suffix must be the same.
    Delete both the prefix and the suffix.

Return the minimum length of s after performing the above operation any number of times (possibly zero 
times).

Example 1:
    Input: s = "ca"
    Output: 2
    Explanation: You can't remove any characters, so the string stays as is.

Example 2:
    Input: s = "cabaabac"
    Output: 0
    Explanation: An optimal sequence of operations is:
    - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
    - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
    - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
    - Take prefix = "a" and suffix = "a" and remove them, s = "".

Example 3:
    Input: s = "aabccabba"
    Output: 3
    Explanation: An optimal sequence of operations is:
    - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
    - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

Constraints:
    1 <= s.length <= 105
    s only consists of characters 'a', 'b', and 'c'.

"""

##################
# First Approach #
##################
# I first tried to do a recursive approach but it was too cimplicated and I couldn't figure it out in time
def get_prefix_suffix(s, prefix='', suffix=''):
    print(f"input_string: {s}")
    newprefix = prefix + s[0]
    newsuffix = suffix + s[-1]
    print(f"prefix: {newprefix}")
    print(f"suffix: {newsuffix}")

    if (len(set(newprefix)) == 1) and (len(set(newsuffix)) == 1) and (set(newprefix) == set(newsuffix)):
        # suffix and prefix match so remove first and last element of s and try again
        s = s[1:-1]
        print("matching")
        return get_prefix_suffix(s, newprefix, newsuffix)
    elif len(set(newprefix)) == 1 and (set(newprefix) == set(suffix)):
        s = s[1:]
        print("only prefix match")
        return get_prefix_suffix(s, newprefix, suffix)
    elif len(set(newsuffix)) == 1 and (set(prefix) == set(newsuffix)):
        s = s[:-1]
        print("only suffix match")
        return get_prefix_suffix(s, prefix, newsuffix)
    else:
        return s

###################
# Second Approach #
###################
    # I had to use ChatGPT's help on this one. My first thought to solving this problem was to use left and right 
    # pointers but I couldn't figure out a way to skip past  similar characters so I moved to the recursive
    # approach which also didn't work either

class Solution:
    def minimumLength(self, s: str) -> int:
        # Start with pointers on either end
        left, right = 0, len(s) - 1

        while (left < right) and s[left] == s[right]:
            # skip all characters that are equal on the left
            current_char = s[left]
            while left <= right and s[left] == current_char:
                left += 1
            while right >= left and s[right] == current_char:
                right -= 1

        return right - left + 1 if left <= right else 0


# test case 1
input = "ca"
output = 2
assert Solution().minimumLength(input) == output

# test case 2
input = "cabaabac"
output = 0
assert Solution().minimumLength(input) == output

# test case 3
input = "aabccabba"
output = 3
assert Solution().minimumLength(input) == output