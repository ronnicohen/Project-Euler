# https://projecteuler.net/problem=14

# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


longest = [1, 1]
starters = []
lengths = []


def main():
	for i in xrange(1, 1000000):
		current_length = create_collatz(i)
		global starters
		global lengths
		global longest
		starters.append(i)
		lengths.append(current_length)
		if current_length > longest[0]:
			longest[0] = current_length
			longest[1] = i
		if i % 200 == 0:
			print i
	print longest


def create_collatz(starter):
	global starters
	global lengths
	current = starter
	length = 1
	if current == 1:
		return length
	if current not in starters:
		current = next_term(current)
		length += create_collatz(current)
	else:
			length += lengths[starters.index(current)]
	return length


def next_term(current):
	if current % 2 == 0:
		current /= 2
	else:
		current = current * 3 + 1
	return current


main()
