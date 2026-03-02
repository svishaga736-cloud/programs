def minSwaps(grid):
    n = len(grid)
    # Step 1: Pre-calculate trailing zeros for each row
    trailing_zeros = []
    for row in grid:
        count = 0
        for i in range(n - 1, -1, -1):
            if row[i] == 0:
                count += 1
            else:
                break
        trailing_zeros.append(count)
    
    total_swaps = 0
    # Step 2: Greedy matching for each required position i
    for i in range(n):
        # Row at index i must have at least (n - 1 - i) trailing zeros
        needed = n - 1 - i
        
        # Find the first row at or below i that satisfies this
        found_idx = -1
        for j in range(i, n):
            if trailing_zeros[j] >= needed:
                found_idx = j
                break
        
        # If no such row is found, it's impossible
        if found_idx == -1:
            return -1
        
        # Step 3: Accumulate swaps and move the found row to position i
        total_swaps += (found_idx - i)
        
        # Physically move the row in our list (bubble it up)
        row_count = trailing_zeros.pop(found_idx)
        trailing_zeros.insert(i, row_count)
        
    return total_swaps
