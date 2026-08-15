class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for p in range(1,27):
            cnt = Counter()
            left = 0
            tot = 0 # 记录当前窗口内有多少种不同字符
            less = 0 # 记录当前窗口，次数小于k的种类
            for i, x in enumerate(s):
                cnt[x] += 1

                if cnt[x] == 1:
                    tot += 1
                    less += 1
                if cnt[x] == k:
                    less -= 1
                #窗口种类超过p
                while tot > p:
                    if cnt[s[left]] == k:
                        less += 1
                    if cnt[s[left]] == 1:
                        tot -= 1
                        less -= 1
                    cnt[s[left]] -= 1
                    left += 1
                # 窗口内种类刚好为p
                if less == 0:
                    ans = max(ans,i-left+1)
        return ans
