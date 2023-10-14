class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        summer = 0

        for i, n in enumerate(nums):
            if bin(i).count('1') == k:
                summer += n
        return summer
        