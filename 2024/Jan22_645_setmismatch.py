import unittest
from copy import copy

"""
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-01-22

You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
    Input: nums = [1,2,2,4]
    Output: [2,3]

Example 2:
    Input: nums = [1,1]
    Output: [1,2]

Constraints:

    2 <= nums.length <= 104
    1 <= nums[i] <= 104
"""

#################
# First attempt #
#################
"""
First attempt would be to do a while loop and start from the back and subtract each adjacent element and look for the
diff to be == 0
"""
def findErrorNums_v1(nums):
    missing = None
    duped_element = None

    # First we can check if 1 is missing since list goes from 1->n
    print(nums[0])
    if nums[0] != 1:
        return [2, 1]
    
    # Second edge case is if the dupes are in the end of the list
    if nums[-1] == nums[-2]:
        return [nums[-1], nums[-1] -1]

    while nums:
        # print(nums)
        last_element = nums.pop(-1)
        try:
            diff = last_element - nums[-1]
        except IndexError:
            break

        if diff > 0:
            continue
        else:
            duped_element = last_element
            missing = last_element + 1
            break

    return [duped_element, missing]

##################
# Second Attempt #
##################
"""
First attempt messed up the edge cases of when len(nums) == 2 and is either [1, 1] or [2, 2].

For the second attempt, I'm going to just iterate over a range with the same length and take action whenever they don't match
"""
def findErrorNums_v2(nums):
    # First sort the array
    nums.sort()

    # Get length of nums
    n = len(nums)

    for i in range(1, n+1):
        if i == nums[i-1]:
            continue
        else:
            return [nums[i-1], i]        


#################
# Third Attempt #
#################
"""
I asssumed that the list was pre-sorted and that the duplicated integer was adjacent to the missing integer. Seeing more
test cases it appears like this is not the case and the duplicated number can occur anywhere in the range and doesn't have to be adjacent
to the missing value. Also the list isn't necessarily pre-sorted.
"""

def findErrorNums_v3(nums):
    dupe_value = None
    missing_value = None

    # Find the duplicated value
    nums_sorted_dupe = sorted(nums)
    while nums_sorted_dupe:
        last = nums_sorted_dupe.pop(-1)
        try:
            next = nums_sorted_dupe[-1]
            if last == next:
                dupe_value = last
                break
        except IndexError:
            break
    
    # Find the missing value
    try:
        missing_value = [i for i in range(1, len(nums)+1) if i not in nums][0]
    except IndexError:
        pass

    return [dupe_value, missing_value]


#################
# Testing suite #
#################
class TestFindErrorNums(unittest.TestCase):

    def run_test_case(self, func, test_input, expected):
        self.assertEqual(func(test_input), expected)

    def test_all_versions(self):
        test_cases = [
            ([1, 2, 2, 4], [2, 3]),
            ([1, 1], [1, 2]),
            ([1, 2, 3, 4, 5, 6], [None, None]),
            ([2, 2], [2, 1]),
            ([1, 3, 3], [3, 2]),
            ([3, 2, 2], [2, 1]),
            ([3, 2, 3, 4, 6, 5], [3, 1])
        ]

        for func in [findErrorNums_v1, findErrorNums_v2, findErrorNums_v3]:
            for test_input, expected in test_cases:
                with self.subTest(func=func, test_input=test_input):
                    self.run_test_case(func, test_input, expected)

if __name__ == '__main__':
    unittest.main()