class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0                   # 统计质数个数
        for i in range(2, n):
            si = isqrt(i)
            is_prime = True         # 初始认为i是质数
            for factor in range(2, si + 1):   # 枚举i的因子，如果i能被因子整除，那么i不是质数
                if i % factor == 0:
                    is_prime = False
                    break
            count += is_prime       # 如果i是质数，那么count+1
        return count        
