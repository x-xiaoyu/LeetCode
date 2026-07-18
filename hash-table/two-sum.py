class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 目标+ 当前 = target 返回两个indices

        num_map = {}

        for i, num in enumerate(nums):
            complement = target - nums[i]

            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

        return []
