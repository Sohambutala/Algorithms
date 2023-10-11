class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        output = []
        for n in nums:
            output.append(nums[n])
        return output