class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord): return 0     # 起点终点字符串长度不一致，不可转换
        n = len(beginWord)     # 获取起点字符串长度
        # 使用哈希表构建单词库，以快速判断单词是否合法
        words_lib = set(wordList)
        if endWord not in words_lib: return 0   # 终点字符串不在单词库中，不可转换
        # 广度优先搜索搜索最短路径
        visited = set([beginWord])      # 记录搜索过的单词, 初始标记起点字符串已搜索（存放到列表中才能加入整个字符串）
        queue = deque()    # 广度优先搜索使用的队列，存储待搜索的单词和到达这个单词经历的单词数（包含这个单词）; 
        queue.append((beginWord, 1))    # 初始起点字符串单词入队，且单词数为1
        while queue:
            curr_word, cnt = queue.popleft()     # 获取队首单词信息
            cnt += 1      # 单词数递增
            # 枚举当前字符串的每一位，尝试以每一种字符可能替换得到新单词
            for i in range(n):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    next_word = curr_word[:i] + ch + curr_word[i+1:] # 替换当前位的字符
                    if next_word not in visited and next_word in words_lib:
                        # next_word这个单词没有处理过且在库里，是一个可转移的节点
                        if next_word == endWord: return cnt
                        visited.add(next_word)
                        queue.append((next_word, cnt))
        return 0
