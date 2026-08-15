class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        max_w, sum_w = max(weights), sum(weights)
        l, r = max(max_w, sum_w // D), sum_w
        while l < r:
            mid = (l + r) >> 1
            if self.check(weights, mid, D):
                r = mid
            else:
                l = mid + 1
        return r

    def check(self, ws, t, d):
        n = len(ws)
        i = cnt = 1
        total = ws[0]
        while i < n:
            while i < n and total + ws[i] <= t:
                total += ws[i]
                i += 1
            total = 0
            cnt += 1
        return cnt - 1 <= d
