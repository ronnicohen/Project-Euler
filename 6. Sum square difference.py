# https://projecteuler.net/problem=6

# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred
#  natural numbers and the square of the sum.

sum_of_squares = 0
simple_sum = 0
for i in xrange(1, 101):
	sum_of_squares += i ** 2
	simple_sum += i
square_of_the_sum = simple_sum ** 2
difference = square_of_the_sum - simple_sum
print difference