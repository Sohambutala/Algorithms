class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = []
        res.append(first)
        for en in encoded:
            res.append(en^first)
            first = res[-1]
        return res