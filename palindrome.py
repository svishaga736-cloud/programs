class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # A must be the shorter array to ensure O(log(min(m, n)))
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = (total + 1) // 2
        
        l, r = 0, len(A)
        while l <= r:
            i = (l + r) // 2  # Partition index for A
            j = half - i      # Partition index for B
            
            # Boundary values around the partition
            Aleft = A[i - 1] if i > 0 else float("-infinity")
            Aright = A[i] if i < len(A) else float("infinity")
            Bleft = B[j - 1] if j > 0 else float("-infinity")
            Bright = B[j] if j < len(B) else float("infinity")
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements
                if total % 2:
                    return float(max(Aleft, Bleft))
                # Even total elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
