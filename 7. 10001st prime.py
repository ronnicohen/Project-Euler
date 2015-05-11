# https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10 001st prime number?


def check_primness(prime_candidate):
	for i in xrange(prime_candidate - 1, 1, -1):
		if prime_candidate % i == 0:
			return False
	return True


def run_test():
	primes = []
	range_of_test = int(raw_input('up to which number would you like to '
								  'check'))
	for i in xrange(2, range_of_test + 1):
		if check_primness(i) is True:
			print i
			primes.append(i)
		if len(primes) == 10001:
			print 'The 10001th prime number is' + str(primes[-1])
			return []
	print 'Using this range of test I only found ' + str(len(primes)) + \
		  ' prime numbers'


# it takes a hell of a long time but it works, will need to look for
# something over 100000 to find the 10001th prime (1000000 only gets to 9592
# prime numbers)
run_test()