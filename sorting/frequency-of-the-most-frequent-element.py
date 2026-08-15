class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = s = left = 0
        for right, x in enumerate(nums):
            s += x
            while (right - left + 1) * x - s > k:
                s -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
