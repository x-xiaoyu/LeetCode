UPPER_BOUND = 5000000
cache = [0] * (UPPER_BOUND + 1)        # cache[i]表示小于等于i的质数个数, 同时在循环过程中可以表示i是否为质数(0为质数，-1为非质数)

# 预处理找到[0, UPPER_BOUND)的质数个数，存入cache
for i in range(2, UPPER_BOUND):
    if cache[i] == 0:
        cache[i] = cache[i-1]+1        # 如果i是质数，那么[0,i]的质数个数 = [0,i]的质数个数 + 1个i这个质数
        for j in range(i*i, UPPER_BOUND, i):    
            cache[j] = -1              # 将i的倍数标记为非质数
    else:
        cache[i] = cache[i-1]          # 如果i是非质数，那么[0,i]的质数个数 = [0,i-1]的质数个数

class Solution:
    def countPrimes(self, n: int) -> int:
        # 避免n-1越界
        if n == 0: return 0
        # cache[i]存的是小于等于i的质数个数，题目求小于i的，即小于等于i-1的，所以返回cache[n-1]即可
        return cache[n-1]
