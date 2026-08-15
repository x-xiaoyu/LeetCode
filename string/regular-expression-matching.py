class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            is_match = i < len(s) and (p[j] == '.' or p[j] == s[i])

            # 匹配零个或多个
            if j + 1 < len(p) and p[j + 1] == '*':  # p[j] 和 p[j+1] 是一个整体
                return (dfs(i, j + 2) or  # 匹配零个
                        is_match and dfs(i + 1, j))  # 匹配一个，交给 dfs(i+1, j) 继续匹配

            # s[i] 与 p[j] 匹配
            return is_match and dfs(i + 1, j + 1)

        return dfs(0, 0)
