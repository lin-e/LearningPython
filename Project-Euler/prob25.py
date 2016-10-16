fib_1 = 0
fib_2 = 1
count = 0
while True:
    count += 1
    f_1_t = fib_1
    fib = fib_1 + fib_2
    fib_1 = fib
    fib_2 = f_1_t
    leng = len(str(fib))
    print(str(count) + ": " + str(fib) + " (" + str(leng) + ")")
    if (leng == 1000):
        break
print(str(count))
