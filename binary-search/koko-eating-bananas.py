class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left = 0  # 恒为 False
        right = max(piles)  # 恒为 True
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if sum((p - 1) // mid for p in piles) <= h - n:
                right = mid  # 循环不变量：恒为 True
            else:
                left = mid  # 循环不变量：恒为 False
        return right  # 最小的 True

