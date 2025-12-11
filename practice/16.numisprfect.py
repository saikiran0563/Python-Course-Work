num = int(input("Enter a number: "))

sum_divisors = 0

# Find divisors from 1 to num-1
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

# Check if perfect
if sum_divisors == num:
    print("Perfect")
else:
    print("Not Perfect")
