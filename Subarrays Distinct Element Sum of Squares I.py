class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        subarrays = []
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                sub = []
                for k in range(len(nums) - (j + i)):
                    sub.append(nums[j + k])
                subarrays.append(sub)
        # print(subarrays)
        for s in subarrays:
            sub = set(s)
            total += len(sub) ** 2
        return total

