class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            complement = target - nums[i]
            if complement in map:
                return [map[complement],i]
            map[num] = i
        return []