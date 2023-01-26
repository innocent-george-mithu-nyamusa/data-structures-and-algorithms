def decimal_to_binary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimal_to_binary(int(n/2))
    
print(decimal_to_binary(-13))
#n              -13 
#n%2            6
#  --  1 0 1 0
#output        1