class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = set()
        for i in nums:
            if i not in arr:
                arr.add(i)
            else:
                return True
        return False