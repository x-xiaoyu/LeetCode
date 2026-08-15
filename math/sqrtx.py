class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid
            else:
                right = mid - 1
        # 退出循环以后，left = right，此时 return right 也对
        return left  
