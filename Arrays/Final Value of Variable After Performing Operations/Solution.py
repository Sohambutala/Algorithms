class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res: int = 0
        for ops in operations:
            if ops in ['--X', 'X--']:
                res -= 1
            elif ops in ['++X', 'X++']:
                res += 1

        return res
            