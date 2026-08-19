# Problem: Two Sum
# You get a list of numbers and a target number.
# Your job: find two numbers in the list that, when added together,
# equal the target — and return where they are in the list (their indices).
# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]   because nums[0] + nums[1] = 2 + 7 = 9
# Approach: Brute Force
# Try every possible pair of numbers, one by one
# Add the two numbers and check if they equal the target
# The moment we find a pair that works, we return their indices
# Time Complexity: O(n^2)
# This is slow because for every number, we're checking it against
# every other number too (a loop inside another loop)
class Solution:
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y:
                    if nums[x] + nums[y] == target:
                        return [x, y]    