current = 0
found = False
while not found:
    current += 1
    divisible = True
    for i in range(2, 20):
        if not current % i == 0:
            divisible = False
            break
    if divisible:
        found = True
print(str(current))
