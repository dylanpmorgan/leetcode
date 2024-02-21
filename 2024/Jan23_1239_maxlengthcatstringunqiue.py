import unittest
from copy import copy

"""
1239. Maximum Length of a Concatenated String with Unique Characters

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence 
of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements 
without changing the order of the remaining elements.

Example 1:
    Input: arr = ["un","iq","ue"]
    Output: 4
    Explanation: All the valid concatenations are:
    - ""
    - "un"
    - "iq"
    - "ue"
    - "uniq" ("un" + "iq")
    - "ique" ("iq" + "ue")
    Maximum length is 4.

Example 2:
    Input: arr = ["cha","r","act","ers"]
    Output: 6
    Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:
    Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output: 26
    Explanation: The only string in arr has all 26 characters.

Constraints:
    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lowercase English letters.
"""

##########################
# First Solution Attempt #
##########################
"""
Use sets to keep track of seen characters
Iterate over arr of string - check if characters are in the seen set
    iterate over subsequences of string - check for characters are in seen set
        concatenate and add to concat set
"""

# First I just want to create all possible concatenations of strings
arrs = [
    ["un","iq","ue"],
    ["cha","r","act","ers"],
    ["abcdefghijklmnopqrstuvwxyz"],
    ["a", "abc", "d", "de", "def"]
]

def get_combinations(arr):
    cat_arr_set = set()
    for i in range(len(arr)+1):
        for j in range(len(arr)+1):
            if i <= j:
                cat_arr_set.add("+".join(arr[i:j]))
                # print(arr[i:j])
            else:
                continue
            # cat_arr_set.add("+".join(arr[i:j]))
    return cat_arr_set

for arr in arrs:
    print(get_combinations(arr))

# Function to check if characters in string have been seen.
# If seen return empty string if not seen return string and seen chars
def check_seen_chars(input_string, seen=None):
    if not seen:
        seen = set()

    for char in input_string:
        if char in seen:
            return "", seen
        else:
            seen.add(char)

    return input_string, seen

arr = ["cha","r","act","ers"]
concat_arr = []
seen = set()
for input_string in arr:
    output_string, seen = check_seen_chars(input_string, seen)
    if output_string:
        concat_arr.append(output_string)
print("".join(concat_arr))

# Need to combine them now
def concat_arr_unique(arr):
    cat_arr_set = set()
    for i in range(len(arr)+1):
        for j in range(len(arr)+1):
            if i < j:
                seen = set()
                sub_arr = arr[i:j]
                uniq_sub_arr = list()
                for input_string in sub_arr:
                    output_string, seen = check_seen_chars(input_string, seen)
                    if output_string:
                        uniq_sub_arr.append(output_string)
                cat_arr_set.add("".join(uniq_sub_arr))
                # print(arr[i:j])
            else:
                continue
    return cat_arr_set

for arr in arrs:
    uniq_cats = concat_arr_unique(arr)
    print(uniq_cats)
    max_len = max([len(x) for x in uniq_cats])
    print(max_len)
    max_cat = [x for x in uniq_cats if len(x)==max_len][0]
    print(max_cat)

# Function for the full solution
def maxLength_v1(arr):
    uniq_cats = concat_arr_unique(arr)
    # print(uniq_cats)
    max_len = max([len(x) for x in uniq_cats])
    max_cat = [x for x in uniq_cats if len(x)==max_len]
    print(max_len, max_cat)
    return max_len

for arr in arrs:
    print(maxLength_v1(arr))

"""
>> Solution FAILED: Failed test case: ["a", "abc", "d", "de", "def"] -> ["abcdef]
"""

########################
# 2nd Solution Attempt # 
########################
"""
Solution failed due to not capturing all the possible string combinations.
Any easy fix is to use itertools.combinations which I was trying to avoid using.
"""

import itertools

def maxLength_v2(arr):
    combos = list()
    for n in range(1, len(arr)+1):
        combos.extend([x for x in itertools.combinations(arr,n)])

    cat_arr_set = set()
    for combo in combos:
        seen = set()
        uniq_sub_arr = list()
        for input_str in combo:
            output_str, seen = check_seen_chars(input_str, seen)
            if output_str:
                uniq_sub_arr.append(output_str)
            cat_arr_set.add("".join(uniq_sub_arr))
    
    max_len = max([len(x) for x in cat_arr_set])
    max_cat = [x for x in cat_arr_set if len(x)==max_len]
    print(max_len, max_cat)

    return max_len

for arr in arrs:
    print(maxLength_v2(arr))
"""
Accepted but really poor runtime & memory performance:
RUNTIME
    1810ms
    Beats 5.00%of users with Python3
MEMORY
    30.48MB
    Beats 16.94%of users with Python3
"""

#########
# TESTS #
#########
class TestSolution(unittest.TestCase):

    def run_test_case(self, func, test_input, expected):
        self.assertEqual(func(test_input), expected[0])

    def test_all_versions(self):
        test_cases = [
            (["un","iq","ue"], [4]),
            (["cha","r","act","ers"], [6]),
            (["abcdefghijklmnopqrstuvwxyz"], [26]),
            (["a", "abc", "d", "de", "def"], [6])
        ]

        for func in [maxLength_v1, maxLength_v2]:
            print(f"Testing: {str(func)}")
            for test_input, expected in test_cases:
                with self.subTest(func=func, test_input=test_input):
                    try:
                        self.run_test_case(func, test_input, expected)
                    except AssertionError as ae:
                        print(f"{str(func)} failed - {ae}")
                        continue

TestSolution().test_all_versions()

###################
# Better solution #
###################
"""
One of the better solutions that was submitted by another user. This solution understood that this was a depth first search problem
and implemented a classic back-tracking solution. The solution also used recursion, very sweet.
"""
arrs = [
    ["un","iq","ue"],
    ["cha","r","act","ers"],
    ["abcdefghijklmnopqrstuvwxyz"],
    ["a", "abc", "d", "de", "def"]
]
for arr in arrs:
    """
        This line filters out any strings in arr that contain duplicate characters. It's a preliminary step to simplify 
        the problem, as any string with duplicate characters can't be part of the solution.
    """
    arr = [a for a in arr if len(set(a)) == len(a)]

    # Function to perform DFS
    def dfs(index, result):
        """
            When index reaches the length of arr, the function returns the length of the result string. 
            This is the length of a unique character combination formed so far.
        """
        if index == len(arr):
            return len(result)
        """
            Checking for duplicate characters. Here, the function checks if the current string arr[index] has any characters in common 
            with result. If there are common characters (i.e., not disjoint), it skips this string and moves to the next 
            (dfs(index + 1, result)).
        """
        if not set(arr[index]).isdisjoint(set(result)):
            return dfs(index + 1, result)
        """
            The function then makes two recursive calls:
                One that skips the current string (dfs(index + 1, result)).
                One that includes the current string (dfs(index + 1, result + arr[index])), but only if it's valid 
                (i.e., no duplicate characters).
            It takes the maximum of these two calls, effectively keeping the longer unique character string.
        """
        return max(dfs(index + 1, result), dfs(index + 1, result + arr[index]))

    """
        Finally, the DFS is initiated with dfs(0, ""), starting with the first string in arr and an empty result. 
        The function will recursively explore all combinations, and the maximum length of the unique character concatenation 
        is printed for each arr in arrs.
    """
    print(dfs(0, ""))
