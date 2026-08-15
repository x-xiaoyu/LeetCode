class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 频率 次数 -》hashmap

        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        fre_bucket = [[] for _ in range(len(nums)+ 1)]
        for num, freq in count_map.items():
            fre_bucket[freq].append(num)

        result = []
        for i in range(len(fre_bucket)):
            for num in fre_bucket[i]:
                result.append(num)
                if (len(result)) == k:
                    return result