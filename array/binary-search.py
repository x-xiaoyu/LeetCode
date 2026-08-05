class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            # mid[left] < target
            # mid[right] >= target
            mid = (right + left) // 2 
            if nums[mid] < target:
                left = mid + 1 # range [mid + 1, right]
            else:
                right = mid
        
        return left

