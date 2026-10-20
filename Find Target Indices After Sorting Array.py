class Solution:
   def targetIndices(self, nums: list[int], target: int) -> list[int]:
       n = sorted(nums)
       output = []
       for i in range(len(n)):
