from typing import List

"""
1184. Distance Between Bus Stops

A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of 
neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.

Example 1:
    Input: distance = [1,2,3,4], start = 0, destination = 1
    Output: 1
    Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Example 2:
    Input: distance = [1,2,3,4], start = 0, destination = 2
    Output: 3
    Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

Example 3:
    Input: distance = [1,2,3,4], start = 0, destination = 3
    Output: 4
    Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.

Constraints:
    1 <= n <= 10^4
    distance.length == n
    0 <= start, destination < n
    0 <= distance[i] <= 10^4
"""

#################
# First attempt #
#################
# This just seems like a question to iterate through the list forward and reverse. Not sure what it being 
# a circle has to do with it.
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            clockwise = sum(distance[start:])+sum(distance[:destination])
        else:
            clockwise = sum(distance[start:destination])
        
        if start > destination:
            counterclockwise = sum(distance[::-1][destination:start])
        else:
            counterclockwise = sum(distance[::-1][0:len(distance)-destination])
        return min(clockwise, counterclockwise)
    

##################
# Second attempt #
##################
# My initial attempt didn't work because I couldn't manage going from end of list to start and from start to end in the different directions.
# This try, I'm going to double the size of the list and this way I should be able to traverse the edge of the list both backwards
# and forwards without dealing the end of the list index, I just need to worry about adjusting ny start and destinations
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # Double the length of distance so we can iterate through it at least once from any start point
        newdistance = distance*2

        # foward (clockwise)
        if destination < start:
            forward_destination = destination + len(distance)
        else:
            forward_destination = destination
        forward = sum(newdistance[start:forward_destination])

        # backward (counterclockwise)
        if destination > start:
            backward_start = start + len(distance)
            backward = sum(newdistance[destination:backward_start])
        else:
            backward_start = start
            backward = sum(newdistance[destination:backward_start])

        return min(forward, backward)

# Test Case 1
distance = [1,2,3,4]
start = 0
destination = 1
expected_output = 1
result = Solution().distanceBetweenBusStops(distance, start, destination)
print(f"Expected: {expected_output}\nResult: {result}")

# Test Case 3
distance = [1,2,3,4]
start = 0
destination = 3
expected_output = 4
result = Solution().distanceBetweenBusStops(distance, start, destination)
print(f"Expected: {expected_output}\nResult: {result}")

# Failed Test Case 15
distance = [7,10,1,12,11,14,5,0]
start = 7
destination = 2
expected_output = 17
result = Solution().distanceBetweenBusStops(distance, start, destination)
print(f"Expected: {expected_output}\nResult: {result}")

# Failed Test Case 22
distance = [14,13,4,7,10,17,8,3,2,13]
start = 2
destination = 9
expected_output = 40
result = Solution().distanceBetweenBusStops(distance, start, destination)
print(f"Expected: {expected_output}\nResult: {result}")

# Failed test case 31
distance = [25,20,35,6,13,0,23,34,1,4,3,38,29,0,31,26,33,20,3,14]
start = 17
destination = 16
expected_output = 33
result = Solution().distanceBetweenBusStops(distance, start, destination)
print(f"Expected: {expected_output}\nResult: {result}")

"""
SUCCESS
    Runtime 41ms
    Beats 92.11% of users with Python3

    Memory 17.54MB
    Beats 61.95% of users with Python3
"""