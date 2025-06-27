class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        numLen = len(nums)
        for i in range(numLen):
            sum = sum + nums[i]
            nums[i] = sum
        return nums