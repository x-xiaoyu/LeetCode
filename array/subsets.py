class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        # 选或不选：讨论 nums[i] 是否加入 path
        def dfs(i: int) -> None:
            if i == n:  # 子集构造完毕
                ans.append(path.copy())  # 复制 path，也可以写 path[:]
                return

            # 不选 nums[i]
            dfs(i + 1)  # 考虑下一个数 nums[i+1] 选或不选

            # 选 nums[i]
            path.append(nums[i])
            dfs(i + 1)  # 考虑下一个数 nums[i+1] 选或不选
            path.pop()  # 恢复现场，撤销 path.append(nums[i])

        dfs(0)
        return ans
