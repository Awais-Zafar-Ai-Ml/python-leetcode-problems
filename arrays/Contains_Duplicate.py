# LeetCode Problem: Contains Duplicate
# 
# Problem Statement:
# Given an integer array nums, return True if any value appears at least twice 
# in the array. Return False if all elements are unique.
#
# Example:
# Input: nums = [1, 2, 3, 1]
# Output: True (1 appears twice)
#
# Approach:
# Use a Set data structure to exploit its unique-value property.
# A set automatically removes duplicates when created from an array.
# If the set size is smaller than the original array, duplicates exist.
#
# Key Insight:
# - set(nums) removes all duplicates
# - If len(nums) > len(set(nums)), duplicates were removed → return True
# - If len(nums) == len(set(nums)), no duplicates existed → return False
#
# Time Complexity: O(n) — iterating through nums to build the set
# Space Complexity: O(n) — storing up to n elements in the set
#
# Example Walkthrough:
# nums = [1, 2, 3, 1]
# set(nums) = {1, 2, 3}  ← duplicate 1 is removed
# len(nums) = 4, len(set(nums)) = 3
# 4 != 3 → return True ✓

class Solution(object):
    def containsDuplicate(self, nums):
        # Convert array to set to remove all duplicates
        x = set(nums)
        
        # Compare lengths: if they differ, duplicates existed
        if len(nums) != len(x):
            return True
        else:
            return False


# One-liner alternative (more Pythonic):
# class Solution(object):
#     def containsDuplicate(self, nums):
#         return len(nums) != len(set(nums))