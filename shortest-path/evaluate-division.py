class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己，自己 * 1 = 自己
        self.fa = list(range(n))  # 代表元
        self.mul = [1.0] * n  # x 的值 * mul[x] = x 的代表元的值

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        fa = self.fa
        if fa[x] != x:
            root = self.find(fa[x])
            self.mul[x] *= self.mul[fa[x]]  # 更新 x 到其代表元的 mul 值
            fa[x] = root
        return fa[x]

    # 判断 x 和 y 是否在同一个集合
    def same(self, x: int, y: int) -> bool:
        # 如果 x 的代表元和 y 的代表元相同，那么 x 和 y 就在同一个集合
        # 这就是代表元的作用：用来快速判断两个元素是否在同一个集合
        return self.find(x) == self.find(y)

    # 合并 from 和 to，新增信息 to / from = value
    # 其中 to 和 from 表示未知量，下文的 x 和 y 也表示未知量
    def merge(self, from_: int, to: int, value: float) -> None:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return
        #    x --------- y
        #   /           /
        # from ------- to
        # 已知 x/from = mul[from] 和 y/to = mul[to]，现在合并 from 和 to，新增信息 to/from = value
        # 由于 y/from = (y/x) * (x/from) = (y/to) * (to/from)
        # 所以 y/x = (y/to) * (to/from) / (x/from) = mul[to] * value / mul[from]
        self.mul[x] = self.mul[to] * value / self.mul[from_]
        self.fa[x] = y


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 把不同字符串映射为不同的数字，方便使用并查集
        variable_to_id = {}
        for equation in equations:
            for s in equation:
                if s not in variable_to_id:
                    variable_to_id[s] = len(variable_to_id)

        # 初始化并查集
        uf = UnionFind(len(variable_to_id))
        for (a, b), value in zip(equations, values):
            uf.merge(variable_to_id[b], variable_to_id[a], value)

        # 回答询问
        ans = []
        for c, d in queries:
            c = variable_to_id.get(c, -1)
            d = variable_to_id.get(d, -1)
            if c != -1 and d != -1 and uf.same(c, d):
                #    c * mul[c] = d * mul[d] = 代表元的值
                # => c / d = mul[d] / mul[c]
                ans.append(uf.mul[d] / uf.mul[c])
            else:
                ans.append(-1.0)
        return ans
