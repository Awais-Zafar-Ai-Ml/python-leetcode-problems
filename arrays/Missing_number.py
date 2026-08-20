# LeetCode Problem: Missing Number
#
# Problem Statement:
# Given an array nums containing n distinct numbers in the range [0, n],
# return the one number that is missing from the array.
#
# Example:
# Input: nums = [0, 1, 3]
# Output: 2
# (n = 3, so the range should be [0, 3], but 2 is missing)
#
# Approach:
# Use the Gauss Sum Formula to calculate what the sum SHOULD be
# if no number was missing, then subtract the ACTUAL sum of the array.
# The difference is the missing number.
#
# Key Insight:
# - If nums has n elements, the complete range is [0, n] (n+1 numbers total)
# - Expected sum of [0, 1, 2, ..., n] = n * (n+1) / 2 (Gauss's Formula)
# - Actual sum = sum(nums)
# - Missing number = expected sum - actual sum
#
# Time Complexity: O(n) — single pass to sum the array
# Space Complexity: O(1) — no extra data structures used
#
# Example Walkthrough:
# nums = [0, 1, 3], n = 3
# Expected sum (0 to 3) = 3 * 4 // 2 = 6
# Actual sum = 0 + 1 + 3 = 4
# Missing number = 6 - 4 = 2 ✓

class Solution:
    def missingNumber(self, nums):
        # Get the length of the array
        n = len(nums)
        
        # Calculate expected sum using Gauss's formula: n*(n+1)/2
        # This gives the sum of all numbers from 0 to n
        x = n * (n + 1) // 2
        
        # Subtract actual sum from expected sum to find the missing number
        return x - sum(nums)