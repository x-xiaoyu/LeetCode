class Solution:
    # 2271. 毯子覆盖的最多白色砖块数
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        ans = cover = left = 0
        for tl, tr, c in tiles:
            cover += (tr - tl + 1) * c
            carpet_left = tr - carpetLen + 1
            while tiles[left][1] < carpet_left:
                cover -= (tiles[left][1] - tiles[left][0] + 1) * tiles[left][2]
                left += 1
            uncover = max((carpet_left - tiles[left][0]) * tiles[left][2], 0)
            ans = max(ans, cover - uncover)
        return ans

    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort(key=lambda c: c[0])
        ans = self.maximumWhiteTiles(coins, k)

        coins.reverse()
        for t in coins:
            t[0], t[1] = -t[1], -t[0]
        return max(ans, self.maximumWhiteTiles(coins, k))
