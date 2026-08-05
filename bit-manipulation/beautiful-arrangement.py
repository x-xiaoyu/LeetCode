from functools import cache


class Solution:
    def countArrangement(self, n: int) -> int:
        # valid[position]保存这个位置可以放哪些数字
        valid = [[] for _ in range(n + 1)]

        for position in range(1, n + 1):
            for number in range(1, n + 1):
                if (
                    number % position == 0
                    or position % number == 0
                ):
                    valid[position].append(number)

        @cache
        def dfs(mask: int) -> int:
            # mask中有多少个1，就表示已经放了多少个数字
            position = mask.bit_count() + 1

            # 所有位置都已经填完
            if position > n:
                return 1

            total = 0

            for number in valid[position]:
                bit = 1 << (number - 1)

                # 这个数字还没有使用
                if mask & bit == 0:
                    total += dfs(mask | bit)

            return total

        return dfs(0)