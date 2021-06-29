# Sum

# Compound interest

# Factorial

# BASE CONDITION


# Try matrix multiplication

def sum_n(n):
    if n == 1:
        return 1
    return sum_n(n-1) + n

print(sum_n(10))

def compound(amount, p, year):
    if year == 0:
        return amount
    return compound( amount, p, year-1 ) * (100+p)/100

print(compound(1000, 10, 2))

def fact(n):
    if n == 1:
        return 1
    return fact(n-1) * n

print(fact(10))
