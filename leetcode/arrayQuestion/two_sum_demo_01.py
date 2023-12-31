# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

class Solution:
    def two_sum(self, nums, target):
        numMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement],i]
            numMap[nums[i]] = i
            print(numMap)
        return []

s = Solution()

print(s.two_sum([2,7,11,15], 9))