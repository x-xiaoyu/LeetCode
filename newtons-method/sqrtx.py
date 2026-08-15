SQRT_MAX = isqrt(2 ** 31 - 1)

class Solution:
    def mySqrt(self, x: int) -> int:
        # 开区间 (left, right)
        left, right = 0, min(x, SQRT_MAX) + 1
        while left + 1 < right:  # 开区间不为空
            # 循环不变量：left^2 <= x
            # 循环不变量：right^2 > x
            m = (left + right) // 2
            if m * m <= x:
                left = m
            else:
                right = m
        # 循环结束时 left+1 == right
        # 此时 left^2 <= x 且 right^2 > x
        # 所以 left 最大的满足 m^2 <= x 的数
        return left
