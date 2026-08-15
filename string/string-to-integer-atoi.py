class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        # 跳过前导空格
        i = 0
        while i < n and s[i] == ' ':
            i += 1

        # 处理正负号
        sign = 1
        if i < n and s[i] in "+-":
            sign = 1 if s[i] == '+' else -1
            i += 1

        # 处理数字
        MX = (1 << 31) - 1
        num = 0
        while i < n and '0' <= s[i] <= '9':
            num = num * 10 + int(s[i])
            if num > MX:  # 最终答案已确定，提前返回
                return MX if sign > 0 else -(1 << 31)
            i += 1

        return sign * num
