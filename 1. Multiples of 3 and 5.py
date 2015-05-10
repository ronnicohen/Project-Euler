# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

current5 = 0
current3 = 0
sum5 = 0
sum3 = 0
while current5 < 1000:
	current5 += 5
	sum5 += current5
while current3 < 1000:
	current3 += 3
	sum3 += current3
total_sum = sum5 + sum3
print total_sum