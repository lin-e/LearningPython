number = 100
sum_squares = 0
sum_number = int((number**2+ number) / 2)
for i in range(1, number + 1):
    sum_squares += i**2
print(sum_number**2 - sum_squares)
