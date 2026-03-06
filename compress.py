from itertools import groupby

# Read input string
S = input().strip()

# Group consecutive characters and format output
output = [(len(list(g)), int(k)) for k, g in groupby(S)]

# Print results separated by space
print(*(output))
