# https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums):
        found_nums = set([])
        for i in range(len(nums)):
            if nums[i] in found_nums:
                return nums[i]
            else:
                found_nums.add(nums[i])