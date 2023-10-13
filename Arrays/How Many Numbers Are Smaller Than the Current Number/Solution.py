class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic , count= dict() , 0
        for i in sorted(nums):
            if not i in dic:
                dic[i]=count
            count+=1
        return [dic[i] for i in nums]