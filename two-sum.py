#https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums, target):
        ind_dict = {}
        for ind in range(len(nums)):
            if nums[ind] in ind_dict:
                ind_dict[nums[ind]].append(ind)
            else:
                ind_dict[nums[ind]] = [ind]
        for num in nums:
            if target == 2 * num:
                if len(ind_dict[num]) > 1:
                    return [ind_dict[num][i] for i in [0,1]]
            elif (target - num) in ind_dict:
                return [ind_dict[num][0], ind_dict[target - num][0]]
        return None