# https://leetcode.com/problems/contains-duplicate

class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    def containsDuplicate(self, nums):
        # return len(nums) != len(set(nums))
        nums_set = set([])
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False

# Line 6 alone works, but longer version has shorter runtime.