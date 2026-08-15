class Solution:
    def rob(self, nums: List[int]) -> int:
        # dfs(i) 表示从 nums[0] 到 nums[i] 最多能偷多少
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> int:
            if i < 0:  # 递归边界（没有房子）
                return 0
            return max(dfs(i - 1), dfs(i - 2) + nums[i])

        return dfs(len(nums) - 1)  # 从最后一个房子开始思考
