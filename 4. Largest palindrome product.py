# https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindrome = [0, 0, 0]
for i in xrange(1, 1000):
	for j in xrange(1, 1000):
		first_half = []
		last_half_reversed = []
		candidate = str(i * j)
		if len(candidate) % 2 == 0:
			mid_from_start = len(candidate) / 2
			mid_from_end = len(candidate) - 1
		else:
			mid_from_start = len(candidate) / 2
			mid_from_end = len(candidate) / 2
		for k in xrange(0, mid_from_start):
			first_half.append(candidate[k])
		for k in xrange(len(candidate) - 1, mid_from_end, -1):
			last_half_reversed.append(candidate[k])
		if first_half == last_half_reversed:
			if int(candidate) > int(palindrome[0]):
				palindrome[0] = int(candidate)
				palindrome[1] = i
				palindrome[2] = j
print '%s and %s are the two 3 digit numbers that multiplied by each other \n ' \
	  'produce the largest palindrome, which is %s' % (palindrome[1],
													   palindrome[2],
													   palindrome[0])
