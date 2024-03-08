from typing import List

"""
3005. Count Elements With Maximum Frequency

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum 
frequency.

The frequency of an element is the number of occurrences of that element in the array.

Example 1:
    Input: nums = [1,2,2,3,1,4]
    Output: 4
    Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
    So the number of elements in the array with maximum frequency is 4.

Example 2:
    Input: nums = [1,2,3,4,5]
    Output: 5
    Explanation: All elements of the array have a frequency of 1 which is the maximum.
    So the number of elements in the array with maximum frequency is 5.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""

#######################
# Solution Attempt #1 #
#######################
"""
Seems like a hashmap problem. Pretty easy implementation with dictionary & list comprehensions but 
the result will likely be very inefficient and perform well. 
"""
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash = dict()
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        print(hash)
        max_freq = max([v for k, v in hash.items()])
        print(max_freq)
        elements_max_freq = len([k for k,v in hash.items() if v == max_freq])*max_freq

        return elements_max_freq

# test case 1
nums = [1,2,2,3,1,4]
expected_output = 4
assert Solution().maxFrequencyElements(nums) == expected_output

# test case 2
nums = [1,2,3,4,5]
expected_output = 5
assert Solution().maxFrequencyElements(nums) == expected_output

"""
Better performance than expected. The last calculation of the number of elements per max freq 
could be improved and probably removed entirely

ACCEPTED
    Runtime 45ms
    Beats 46.82% of users with Python3

    Memory 16.41MB
    Beats 97.35% of users with Python3
"""