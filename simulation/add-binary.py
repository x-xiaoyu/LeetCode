class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        i = len(a) - 1  # 从右往左遍历 a 和 b
        j = len(b) - 1
        carry = 0  # 保存进位

        while i >= 0 or j >= 0 or carry:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            s = x + y + carry  # 计算这一位的加法
            # 例如 s = 10，把 '0' 填入答案，把 carry 置为 1
            ans.append(str(s % 2))
            carry = s // 2
            i -= 1
            j -= 1

        return ''.join(reversed(ans))
