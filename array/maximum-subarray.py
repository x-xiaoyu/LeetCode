class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化 负无穷或者第一个数
        max_sum =nums[0] 
        # cur_sum为0
        cur_sum = 0


        for x in nums:
            # 最新的cur_sum = 当前input数 与cur_sum + input数对比取最大
            cur_sum = max(x, cur_sum + x)
            # 再对比当前sum与历史最高sum 取最大 更新max_sum
            max_sum = max(max_sum, cur_sum)

        return max_sum