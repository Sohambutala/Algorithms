class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if index[i] >= len(result):
                result.append(nums[i])
            else:
                result = result[:index[i]] + [nums[i]] + result[index[i]:]
        return result