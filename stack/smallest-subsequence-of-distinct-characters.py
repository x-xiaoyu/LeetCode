# Python3 字典统计+栈模拟
from collections import Counter
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = list()
        dic = Counter(s)
        slen = len(s)
        for i in range(slen):
            while stack and stack[-1] > s[i] and dic[stack[-1]] > 0 and s[i] not in stack:
                stack.pop()
            if s[i] not in stack:
                stack.append(s[i])
            dic[s[i]] -= 1
        return "".join(stack)
