# Running sum of an array 


# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.


class Solution:
    def runningSum(self, nums):
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total

        return nums
 