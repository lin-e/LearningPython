largest_current = 1
factor_0 = 1
factor_1 = 1
for x in range(100, 999):
    for y in range(100, 999):
        product = str(x * y)
        if (product == product[::-1]):
            if (int(product) > largest_current):
                largest_current = int(product)
                factor_0 = x
                factor_1 = y
print("The highest product is " + str(largest_current) + " which is " + str(factor_0) + " * " + str(factor_1))
