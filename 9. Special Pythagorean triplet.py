# https://projecteuler.net/problem=9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a ** 2 + b ** 2 = c ** 2
# For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 5 ** 22.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def find_triplet():
	for a in xrange(999, 0, -1):
		for b in xrange(999, 0, -1):
			if a + b < 1000 and a < b:
				for c in xrange(999, 0, -1):
					if a + c < 1000 and b + c < 1000 and b < c:
						print str(a) + '  ' + str(b) + '  ' + str(c)
						if a + b + c == 1000 and a < b < c:
							if a ** 2 + b ** 2 == c ** 2:
								print 'a = %s \n b = %s \n c = %s' % (a, b, c)
								return []


# Takes a while but it works. a = 200, b = 375 c = 425
find_triplet()