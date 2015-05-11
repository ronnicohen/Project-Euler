# https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def check_primness(prime_candidate):
	for i in xrange(prime_candidate - 1, 1, -1):
		if prime_candidate % i == 0:
			return False
	return True


def run_test():
	primes = []
	range_of_test = 2000000
	for i in xrange(2, range_of_test + 1):
		if check_primness(i) is True:
			print i
			primes.append(i)
	return primes

def sum_primes():
	primes = run_test()
	summation = 0
	for i in primes:
		summation += i


# I used a lot of the code for 7. 10001th prime here. Quite sure it will work
#  properly but also that it will take a heck of a long time