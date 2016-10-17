def get_divisor_count(n):
    count = 2
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            count += 1
            if not i*i == n:
                count += 1
    return count
index = 0
last = 0
while True:
    index += 1
    last += index
    print(last)
    if get_divisor_count(last) > 500:
        break
print(last)
