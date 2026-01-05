def gcd(a, b):
    if b == 0:
        return a  #Q10
    return gcd(b, a % b)
print(gcd(6, 4))
# Find GCD(6, 4)
# gcd(6, 4)
# → gcd(4, 6 % 4) → gcd(4, 2)
# gcd(4, 2)
# → gcd(2, 4 % 2) → gcd(2, 0)
# b == 0 → return 2