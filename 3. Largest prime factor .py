# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


biggie = float(600851475143)
from itertools import count
for i in count(3, 1):
	if i < biggie:
		while biggie % i == 0:
			if biggie < i:
				break
			biggie = float(biggie) / i
	else:
		break
print 'the largest prime number of 600851475143 is %s' % (str(biggie))

