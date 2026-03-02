def twoSum(nums, target):
    # Dictionary to store value: index
    prev_map = {}
    
    for i, v in enumerate(nums):
        complement = target - v
        
        # If complement exists, we found the pair
        if complement in prev_map:
            return [prev_map[complement], i]
        
        # Otherwise, store the current number's index
        prev_map[v] = i
