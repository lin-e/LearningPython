total = 0
fib_1 = 1
fib_2 = 0
while True:
    f_1_t = fib_1
    fib = fib_1 + fib_2
    fib_1 = fib
    fib_2 = f_1_t
    print(fib)
    if (fib > 4000000):
        break
    if fib % 2 == 0:
        total += fib
print(total)
