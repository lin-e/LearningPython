def get_divisors_sum(n):
    total = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            total += i
    return total
def sum_not_exceed(n, d):
    total = 0
    for i in range(1, n + 1):
        if get_divisors_sum(i) % d == 0:
            total += i
    return total
print(str(sum_not_exceed(100000000000, 2017)))
