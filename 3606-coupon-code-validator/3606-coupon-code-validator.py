class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        res = []

        for c, b, a in zip(code, businessLine, isActive):
            if not a:
                continue
            if b not in order:
                continue
            if not c:
                continue
            if not all(ch.isalnum() or ch == "_" for ch in c):
                continue
            res.append((order[b], c))

        res.sort()
        return [c for _, c in res]
