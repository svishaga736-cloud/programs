import re

# Read dimensions
n, m = map(int, input().split())

# Read the matrix rows
matrix = [input() for _ in range(n)]

# 1. Transpose the matrix to read column-wise
# zip(*matrix) takes characters from each column
decoded_string = "".join(["".join(column) for column in zip(*matrix)])

# 2. Replace non-alphanumeric characters between alphanumeric ones
# The pattern looks for a sequence of non-alphanumeric chars ([^a-zA-Z0-9]+)
# that is preceded and followed by an alphanumeric char ((?<=\w) and (?=\w))
final_output = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_string)

print(final_output)

