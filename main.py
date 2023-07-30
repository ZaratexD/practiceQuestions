nums = [2,7,11,15]
target = 9
print(nums)

class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            for j in nums[i + 1:]:
                print(i, j)
