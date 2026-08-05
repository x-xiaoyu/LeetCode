class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)

        # min_suffix[i] 表示从 s[i] 到最后的最小字符
        min_suffix = list(s)

        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(min_suffix[i], min_suffix[i + 1])

        t = []
        p = []

        for i, char in enumerate(s):
            # s 的第一个字符进入 t 的末尾
            t.append(char)

            # s 剩余部分的最小字符
            if i + 1 < n:
                remaining_min = min_suffix[i + 1]
            else:
                remaining_min = "{"

            # t只能从最后一个字符取
            while t and t[-1] <= remaining_min:
                p.append(t.pop())

        return "".join(p)