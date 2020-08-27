#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums, target):
        def bin_find(nums, target, low=0, high=None):
            if high is None:
                high = len(nums) - 1
            if low > high:
                return -1
            if low == high:
                if nums[low] == target:
                    return low
                else:
                    return -1
            guess = (high + low) // 2
            if nums[guess] == target:
                return guess
            if nums[guess] >= nums[0]:   # lower sub-list sorted
                if nums[0] <= target and nums[guess] >= target:
                    return bin_find(nums, target, low, guess-1)
                else:
                    return bin_find(nums, target, guess+1, high)
            else:   # upper sub-list sorted
                if nums[guess] <= target and nums[-1] >= target:
                    return bin_find(nums, target, guess+1, high)
                else:
                    return bin_find(nums, target, low, guess-1)
        return bin_find(nums,target)

soln = Solution()
print(soln.search([3,4,7,0,1], 4))
print(soln.search([4,5,6,7,0,1,2], 0))
print(soln.search([4,5,6,7,0,1,2], 3))
print(soln.search([1,3], 3))
