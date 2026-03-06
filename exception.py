# Read the number of test cases
for _ in range(int(input())):
    try:
        # Read a and b, then perform integer division
        a, b = map(int, input().split())
        print(a // b)
    except (ZeroDivisionError, ValueError) as e:
        # Print the specific error message as required
        print("Error Code:", e)

