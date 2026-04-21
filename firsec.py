import bisect

class Solution:
    def searchRange(self, nums, target):
        # Find the leftmost insertion point
        left = bisect.bisect_left(nums, target)
        # Find the rightmost insertion point
        right = bisect.bisect_right(nums, target) - 1
        
        # Check if the target actually exists in the array
        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]
        
        return [-1, -1]
