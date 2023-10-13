class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for user in accounts:
            max_wealth = max(max_wealth,sum(user))

        return max_wealth