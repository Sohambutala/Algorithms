class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ctr = 0
        for h in hours:
            if h >= target:
                ctr+=1
        return ctr