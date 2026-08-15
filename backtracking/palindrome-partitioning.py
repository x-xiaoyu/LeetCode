class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        # 现在 s 未被分割的部分为 [start, n-1]
        # 当前位于下标 i，讨论是否在 i 和 i+1 之间切一刀
        def dfs(i: int, start: int) -> None:
            if i == n:  # s 分割完毕
                ans.append(path.copy())  # 复制 path
                return

            # 不分割
            if i < n - 1:  # i=n-1 时必须分割（这是最后一段），i<n-1 时才可以不分割
                dfs(i + 1, start)

            # 分割，那么得到子串 [start, i]
            t = s[start: i + 1]
            if t == t[::-1]:  # 判断 t 是不是回文串
                path.append(t)
                # 现在 s 未被分割的部分为 [i+1, n-1]
                dfs(i + 1, i + 1)
                path.pop()  # 恢复现场

        dfs(0, 0)
        return ans
