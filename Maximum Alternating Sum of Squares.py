class Solution:
   def maxAlternatingSum(self, nums: List[int]) -> int:
       for n in range(len(nums)):
           nums[n] = nums[n]**2
       nums = sorted(nums)
       total = 0
       while len(nums) > 1:
           total += (nums[len(nums)-1]-nums[0])
           nums.pop(0)
           nums.pop(len(nums) - 1)
       if len(nums) == 1:
           total += nums[0]
       return total




