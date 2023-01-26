
def powers(base, power):
    if power == 0:
        return 0
    elif power == 1:
        return base
    else:
        return base * powers(base, power-1)

print(powers(3, 1))