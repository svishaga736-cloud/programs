def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
    
    res = [0] * (len(num1) + len(num2))
    
    # Reverse iterate through strings
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            # Calculate product of single digits
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            
            # Position in the res array
            p1, p2 = i + j, i + j + 1
            sum_val = mul + res[p2]

            res[p2] = sum_val % 10
            res[p1] += sum_val // 10
            
    # Convert digit array to string, stripping leading zero
    result_str = "".join(map(str, res))
    return result_str.lstrip("0")
