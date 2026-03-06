from itertools import product

# Read K and M
K, M = map(int, input().split())

# Read the K lists (skipping the first element which is the count Ni)
lists = [list(map(int, input().split()))[1:] for _ in range(K)]

# Precompute squares modulo M to optimize (optional but helpful)
# We use x**2 for the sum and then perform the final modulo
def solve():
    max_val = 0
    # Generate all combinations picking one from each list
    for combo in product(*lists):
        # Calculate sum of squares modulo M
        current_sum = sum(x**2 for x in combo) % M
        if current_sum > max_val:
            max_val = current_sum
    return max_val

print(solve())

