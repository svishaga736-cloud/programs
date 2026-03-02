def reverse(x: int) -> int:
    MAX_INT = 2147483647  # 2^31 - 1
    MIN_INT = -2147483648 # -2^31
    
    res = 0
    while x != 0:
        # Get the last digit
        # Note: In Python, % on negative numbers works differently than C++/Java
        # We handle the sign manually for consistency with 32-bit logic
        digit = int(math.fmod(x, 10)) 
        x = int(x / 10)
        
        # Check for Overflow
        if res > MAX_INT // 10 or (res == MAX_INT // 10 and digit > 7):
            return 0
        
        # Check for Underflow
        if res < int(MIN_INT / 10) or (res == int(MIN_INT / 10) and digit < -8):
            return 0
            
        res = (res * 10) + digit
        
    return res
