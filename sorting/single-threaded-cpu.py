from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[duration, i, start] for i, (start, duration) in enumerate(tasks)]
        tasks.sort(key=lambda x: (x[2]))                # 按照开始时间将各个任务排序
        time = tasks[0][2]                              # 当前时间
        res = []                                        # 最终结果
        queue = []                                      # 优先队列，先按照持续时间排序，后按照下标排序，最后按照开始时间排序
        n = len(tasks)                                  # 任务总数
        idx = 0                                         # 当前的任务索引下标
        while len(res) != n:                            # 只要还没凑够n个任务，就要继续
            while idx < n and tasks[idx][2] <= time:    # 对于当前时间time，将tasks中所有开始时间小于等于time的任务入队
                heapq.heappush(queue, tasks[idx])       #
                idx += 1
            if not queue:                               # 如果优先队列中没有任务，则快进到下一个任务开始时间
                time = tasks[idx][2]
                continue
            duration, index, start = heapq.heappop(queue)   # 按照持续时间从低到高，下标从低到高的顺序，获取优先队列中的元素
            res.append(index)                           # 执行任务
            time = time + duration                      # 任务结束后的当前时间
        return res
