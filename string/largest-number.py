class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(lambda a, b: int(b + a) - int(a + b)))
        return "0" if nums[0] == "0" else ''.join(nums)
