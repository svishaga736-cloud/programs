def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the shorter array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        partition1 = (low + high) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        # Boundary conditions: use -inf/inf if partition is at the ends
        l1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
        r1 = nums1[partition1] if partition1 < m else float('inf')
        
        l2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
        r2 = nums2[partition2] if partition2 < n else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            # Correct partition found
            if (m + n) % 2 == 1:
                return float(max(l1, l2))
            else:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            # Move left in nums1
            high = partition1 - 1
        else:
            # Move right in nums1
            low = partition1 + 1
