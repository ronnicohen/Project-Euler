# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
#  numbers from 1 to 20?

def divides_by(number):
	if number % 2 == 0:
		if number % 3 == 0:
			if number % 4 == 0:
				if number % 5 == 0:
					if number % 7 == 0:
						if number % 9 == 0:
							if number % 11 == 0:
								if number % 13 == 0:
									if number % 17 == 0:
										return number


def run_numbers():
	up_to = raw_input('up to which number would you like to check?')
	for i in xrange(20, int(up_to)):
		candidate = divides_by(i)
		if not candidate == None:
			print candidate
			return []

# the check needs to be run up to 10000000 in order to find the number
run_numbers()